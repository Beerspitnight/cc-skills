import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def luminance(rgb):
    rs, gs, bs = [x / 255.0 for x in rgb]
    rs, gs, bs = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in (rs, gs, bs)]
    return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs

def contrast_ratio(hex1, hex2):
    lum1 = luminance(hex_to_rgb(hex1))
    lum2 = luminance(hex_to_rgb(hex2))
    bright = max(lum1, lum2)
    dark = min(lum1, lum2)
    return (bright + 0.05) / (dark + 0.05)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python color_check.py <hex_foreground> <hex_background>")
    else:
        fg, bg = sys.argv[1], sys.argv[2]
        ratio = contrast_ratio(fg, bg)
        
        status = "FAIL"
        if ratio >= 7: status = "AAA (Perfect)"
        elif ratio >= 4.5: status = "AA (Pass)"
        elif ratio >= 3: status = "Large Text Only"
        
        print(f"Contrast: {ratio:.2f}:1")
        print(f"WCAG Status: {status}")
