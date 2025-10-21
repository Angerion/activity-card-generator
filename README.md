# Activity Card Generator

A web component for generating printable A4 pages with activity cards from images. Cards are automatically duplicated based on count extracted from filenames.

## Features

- 📤 **Drag-and-drop** or click to select images
- 🔢 **Auto-count extraction** from filenames (e.g., `koupání_12.png` → "Koupání" printed 12 times)
- 📄 **A4 page layout** with centered 4×6 grid (24 cards per page)
- 🎨 **Styled cards**: 170×170px, 15px radius, #444 background, 5px inner padding
- 🖼️ **Smart content layout**: 135px image area + 25px text area
- 🖨️ **Print-ready** with proper page breaks

## Usage

### Basic Usage

1. Open `index.html` in your browser
2. Drag and drop images or click to select them
3. Images should follow the naming pattern: `activityname_count.png`
   - Example: `koupání_12.png` → Card named "Koupání" printed 12 times
   - Without count: `reading.png` → Card named "Reading" printed 1 time
4. Click "Generate Cards" to create the printable pages
5. Click "Print" to print the cards

### Demo

Open `demo.html` for a working demo with sample images. Click "Load Demo Images" to see example cards.

### Filename Format

```
activityname_count.extension
```

**Examples:**
- `koupání_12.png` → "Koupání" × 12 cards
- `běhání_6.png` → "Běhání" × 6 cards
- `reading.png` → "Reading" × 1 card (default count)

## Card Specifications

- **Page Size**: A4 (210mm × 297mm)
- **Grid Layout**: 4 columns × 6 rows (24 cards per page)
- **Grid Gap**: 10px
- **Card Size**: 170px × 170px
- **Border Radius**: 15px
- **Background**: #444
- **Inner Padding**: 5px
- **Content Area**: White background
  - **Image Area**: 135px (top)
  - **Text Area**: 25px (bottom, centered)

## Development

The project consists of plain HTML, CSS, and JavaScript with no build step required:

- `index.html` - Main application with drag-and-drop functionality
- `demo.html` - Demo version with sample images pre-loaded
- `examples/` - Sample images for testing

### Running Locally

Simply open the HTML files in a web browser. For testing with local images, use a local web server:

```bash
python3 -m http.server 8080
```

Then navigate to `http://localhost:8080/`

## Browser Compatibility

Works in all modern browsers with support for:
- CSS Grid
- FileReader API
- Drag and Drop API
- Print styles (@page)

## License

MIT