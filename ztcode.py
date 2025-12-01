import hashlib
from PIL import Image

def txt_to_tri(s):
    tri_str = ""
    for ch in s.encode("utf-8"):
        n = ch
        t = ""
        while n > 0:
            t = str(n % 3) + t
            n //= 3
        if len(t) < 6:
            t = ("0" * (6 - len(t))) + t
        tri_str += t
    return tri_str

def make_ztcode(txt, fname="ztcode.png", pix=10, pad=1):
    tri = txt_to_tri(txt)

    colors = {
        "0": (255, 255, 255),
        "1": (0, 0, 0),
        "2": (0, 255, 0)
    }

    side = int(len(tri)**0.5)
    while side * side < len(tri):
        side += 1

    W = (side + pad * 2) * pix
    H = (side + pad * 2) * pix

    im = Image.new("RGB", (W, H), (255, 255, 255))
    p = im.load()

    i = 0
    for val in tri:
        c = colors[val] if val in colors else (120, 120, 120)
        gx = i % side
        gy = i // side
        sx = (gx + pad) * pix
        sy = (gy + pad) * pix
        for dx in range(pix):
            for dy in range(pix):
                xx = sx + dx
                yy = sy + dy
                if xx < W and yy < H:
                    p[xx, yy] = c
        i += 1

    im.save(fname)
    print("saved:", fname)
    return fname

if __name__ == "__main__":
    t = input("text for ztcode: ")
    f = make_ztcode(t, pix=5, pad=5)
    print("done:", t)
