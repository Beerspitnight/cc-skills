# Design Principles & Axioms

## 1. Typography
- **Modular Scale:** Use a scale (e.g., Major Third 1.250) for font sizes to ensure harmony.
- **Line Height:**
  - Headings: 1.1 - 1.2
  - Body text: 1.4 - 1.6
- **Measure (Line Length):** Keep body text between 45-75 characters per line for readability.
- **Pairing:** Combine a Serif (for headings) with Sans-Serif (for body), or use a "Superfamily" with varying weights.
- **Optical Margin Alignment:** Use hanging punctuation for a visually clean text block edge.
- **Optical vs. Geometric Sizing:** Adjust type for screens where scaling isn’t uniform.
- **Font Rendering Differences:** Test typography across macOS, Windows, and mobile.
- **Micro-typography:** Kerning, ligatures, contextual alternates—fine-tune especially in large headings.

## 2. Color Theory
- **60-30-10 Rule:**
  - 60% Primary neutral
  - 30% Secondary brand color
  - 10% Accent color
- **Accessibility:** Meet WCAG AA (4.5:1) contrast minimums.
- **Saturation:** Avoid pure black/grey—use slightly tinted darks.
- **Color Temperature:** Warm/cool dynamics should match emotional tone.
- **Luminance Control:** Ensure a clear hierarchy even without hues.
- **Brand Color Expansion:** Define tints, shades, and semantic colors.
- **Dark/Light Mode Parity:** Colors should remain consistent across themes.

### Emotional Resonance (Psychology)
- **Red:** Urgency, passion, food/retail (CTAs, Sales).
- **Blue:** Trust, security, corporate, finance.
- **Green:** Growth, health, money, eco-friendly.
- **Yellow:** Optimism, caution, highlights.
- **Purple:** Luxury, wisdom, creative, spiritual.
- **Black:** Sophistication, luxury, editorial.

### Accessibility
- **WCAG AA:** 4.5:1 ratio for normal text.
- **WCAG AAA:** 7:1 ratio for normal text.

## 3. Layout & Hierarchy
- **CRAP Principle:**
  - **Contrast:** Make differences bold and intentional.
  - **Repetition:** Create unity through recurring elements.
  - **Alignment:** Every element should visually relate to another.
  - **Proximity:** Group related items; separate unrelated ones.
- **Whitespace:** Use whitespace as an active design tool.
- **Grid Systems:** Use 8pt/4pt grids for digital; 12-column grids for web layouts.
- **Golden Ratio / Rule of Thirds:** Use for balanced composition.
- **Hierarchy Maps:** Define permissible levels of text hierarchy.
- **Visual Flow:** Choose F-pattern, Z-pattern, or narrative flow as appropriate.

## 4. UI/UX Specifics
- **Touch Targets:** Minimum 44x44px for mobile.
- **Consistency:** Matching radius, padding, and spacing across components.
- **Interaction Design Principles:** Feedback, Affordances, Signifiers, Constraints, Mapping.
- **System States:** Loading, error, success, skeleton, disabled.
- **Motion as Meaning:**
  - UI animation duration: 100–300ms.
  - Easing: ease-out for UI, ease-in-out for motion.
- **Design Tokens:** Centralized values for spacing, colors, typography.

## 5. Branding & Identity
- **Logo Use:** Correct proportions and clear space.
- **Tone & Voice via Visuals:** Visual identity should reflect brand personality.
- **Cross-Media Behavior:** Adapting brand for print, mobile, widescreen.
- **Asset Governance:** Versioning, naming, distribution of brand kits.

## 6. Accessibility
- **Alt Text Strategy:** Provide functional, purpose-driven alt text.
- **Keyboard Navigation:** Ensure usable focus states.
- **Motion Sensitivity:** Provide reduced-motion alternatives.
- **Readable Scaling:** Test at 125% and 150% zoom.

## 7. Workflow & Quality Control
- **Review Levels:**
  - L1: Personal check
  - L2: Team critique
  - L3: Cross-functional review
- **Exporting:**
  - SVG optimization
  - PNG-8/PNG-24 distinctions
  - WebP for modern web assets
- **File Naming Conventions:** Standardized and consistent.
- **Design Version Control:** Use Figma branching or Git-based systems.

## 8. Cognitive & Behavioral Design
- **Cognitive Load:** Reduce friction by chunking and simplifying choices.
- **Visual Anchors:** Use contrast, faces, or motion to guide attention.
- **Framing & Priming:** Understand how colors and spacing affect perception.

## 9. Cultural & Globalization Considerations
- **RTL Logic:** Support right-to-left layouts.
- **Localization Expansion:** Plan for text that expands 30–50%.
- **Cultural Iconography:** Ensure symbols translate globally.

## 10. Technical Format Guide
| Format | Type | Best For | Transparency? |
|--------|------|----------|---------------|
| **JPG** | Raster | Photos, complex gradients | No |
| **PNG** | Raster | UI elements, screenshots | Yes |
| **WebP** | Raster | Modern web delivery (highly compressed) | Yes |
| **SVG** | Vector | Icons, logos, illustrations | Yes |
| **PDF** | Vector | Print documents, sharing | Yes |

