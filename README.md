# Activity Card Generator

Modern Svelte application for generating printable A4 pages with activity cards from uploaded images. Card counts are automatically inferred from filenames and remain editable before printing.

## Features

- 📤 **Drag-and-drop** or click to select images
- 🔢 **Auto-count extraction** from filenames (e.g., `koupání_12.png` → "Koupání" printed 12 times)
- ✏️ **Editable cards** – adjust text and counts inline before generating pages
- �️ **Removable entries** – drop any uploaded card before generating
- �📄 **A4 layout** with centered 4×6 grid (24 cards per page)
- 🎨 **Consistent styling**: 170×170px cards, 15px radius, #444 border, 5px padding
- ️ **Print-ready** layout with proper page breaks

## Getting Started

```bash
npm install
npm run dev
```

Open the dev server URL (defaults to <http://localhost:5173>) to interact with the editor. Use `npm run build` to produce a production-ready bundle, and `npm run preview` to serve the built output locally.

## Usage

1. Click **Select Images** or drag and drop files into the page.
2. Filenames should follow `activity_name_count.png`:
  - `koupání_12.png` → 12 cards labeled “Koupání”.
  - `reading.png` → single “Reading” card (count defaults to 1).
3. Adjust card text or counts in the list as needed, or remove entries you no longer want.
4. Click **Generate Cards** to lay out the printable pages.
5. Click **Print** to invoke the browser print dialog.
6. Optional: Use **Load Demo** to preload sample assets from `public/examples/`.

## Card Specifications

- **Page Size**: A4 (210×297 mm)
- **Grid Layout**: 4 columns × 6 rows (24 cards per page)
- **Grid Gap**: 10 px
- **Card Size**: 170×170 px with 15 px border radius
- **Inner Padding**: 5 px around the card content
- **Image Area**: 135 px tall
- **Text Area**: 25 px tall, centered

## Assets & Utilities

- `public/examples/` contains ready-to-use demo images and `create_test_images.py` for generating more samples.
- `examples/` mirrors the same assets for convenience outside the build pipeline.

## License

MIT