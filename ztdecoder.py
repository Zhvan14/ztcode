from PIL import Image

COLOR_MAP = {
    (255, 255, 255): "0",
    (0, 0, 0): "1",
    (0, 255, 0): "2"
}

TRI_PER_BYTE = 6

def tri_to_txt(tri):
    if len(tri) % TRI_PER_BYTE != 0:
        raise ValueError("bad trinary length")

    out_bytes = []
    for i in range(0, len(tri), TRI_PER_BYTE):
        chunk = tri[i:i+TRI_PER_BYTE]
        n = 0
        p = 0
        for d in reversed(chunk):
            n += int(d) * (3 ** p)
            p += 1
        out_bytes.append(n)

    return bytes(out_bytes).decode("utf-8")

def read_ztcode(fname, pix=5, pad=5):
    try:
        img = Image.open(fname).convert("RGB")
    except Exception as e:
        return f"error opening file: {e}"

    px = img.load()

    usable = img.width - (pad * 2 * pix)
    side = usable // pix

    tri = ""
    for gy in range(side):
        for gx in range(side):
            cx = pad * pix + gx * pix + pix // 2
            cy = pad * pix + gy * pix + pix // 2
            if cx >= img.width or cy >= img.height:
                break
            c = px[cx, cy]
            d = COLOR_MAP.get(c)
            if d is not None:
                tri += d

    if not tri:
        return "no data found"

    end = len(tri) - 1
    while end >= 0 and tri[end] == "0":
        end -= 1

    if end >= 0:
        raw_len = end + 1
        need = ((raw_len + TRI_PER_BYTE - 1) // TRI_PER_BYTE) * TRI_PER_BYTE
        need = min(need, len(tri))
        tri = tri[:need]
    else:
        tri = ""

    try:
        if tri:
            return tri_to_txt(tri)
        return "no usable data"
    except Exception as e:
        return f"decode error: {e}"

if __name__ == "__main__":
    fn = "ztcode.png"
    p = 5
    bp = 5

    print("decoding:", fn)
    result = read_ztcode(fn, pix=p, pad=bp)
    print("decoded:", result)
