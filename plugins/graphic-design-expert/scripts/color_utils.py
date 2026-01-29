import sys
import colorsys

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

def generate_palette(base_hex):
    try:
        r, g, b = hex_to_rgb(base_hex)
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        
        # Generate a complementary color
        comp_h = (h + 0.5) % 1.0
        comp_r, comp_g, comp_b = colorsys.hls_to_rgb(comp_h, l, s)
        comp_hex = '#{:02x}{:02x}{:02x}'.format(int(comp_r*255), int(comp_g*255), int(comp_b*255))
        
        ratio = contrast_ratio(base_hex, '#FFFFFF')
        wcag = "FAIL"
        if ratio >= 7: wcag = "AAA"
        elif ratio >= 4.5: wcag = "AA"
        elif ratio >= 3: wcag = "Large Text Only"
        
        return f"Base: {base_hex}\nComplementary: {comp_hex}\nContrast (Base vs White): {ratio:.2f}:1 ({wcag})"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(generate_palette(sys.argv[1]))
    else:
        print("Please provide a hex code.")
