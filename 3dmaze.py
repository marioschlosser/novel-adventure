def draw3d_PIL(draw, map, rot, posx, posy, width=960, height=960):
    import numpy as np
    from PIL import Image, ImageDraw

    for i in range(60):
        rot_i = rot + np.deg2rad(i - 30)
        x, y = (posx, posy)
        sin, cos = (0.02 * np.sin(rot_i), 0.02 * np.cos(rot_i))
        n = 0
        while True:
            x, y = (x + cos, y + sin)
            n = n+1
            if map[int(x)][int(y)] != 0:
                dist = np.sqrt((x - posx)**2 + (y - posy)**2)
                h = 1/(dist + 0.00001)
                c = np.asarray(map[int(x)][int(y)]) * (0.3 + 0.7/(dist**2+1))
                break

        x_coord = int(i * width / 60)
        x0, y0 = x_coord, height // 2 - h * height // 2
        x1, y1 = x_coord, height // 2 + h * height // 2
        draw.line([x0, y0, x1, y1], fill=tuple((c * 255).astype(int)), width=16)
