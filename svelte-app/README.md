# Activity Card Generator (Svelte)

A modern Svelte implementation of the Activity Card Generator with editable card properties.

## New Features

- 🎯 **Built with Svelte** - Modern reactive framework for better performance
- ✏️ **Editable Cards** - Edit card text and count after uploading
- 🎨 **Same Design** - Maintains all original specifications (A4, 4×6 grid, 170×170px cards)
- ⚡ **Hot Module Replacement** - Instant feedback during development

## Getting Started

### Installation

```bash
cd svelte-app
npm install
```

### Development

```bash
npm run dev
```

Open http://localhost:5173 in your browser.

### Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

### Preview Production Build

```bash
npm run preview
```

## Usage

1. Click "Load Demo" to load sample images, or
2. Click "Select Images" to upload your own images
3. **Edit the card text and count** directly in the list
4. Click "Generate Cards" to create printable pages
5. Click "Print" to print the cards

## Card Specifications

Same as the original implementation:
- **Page Size**: A4 (210mm × 297mm)
- **Grid Layout**: 4 columns × 6 rows (24 cards per page)
- **Card Size**: 170px × 170px
- **Border Radius**: 15px
- **Background**: #444
- **Inner Padding**: 5px
- **Image Area**: 135px
- **Text Area**: 25px (centered)
- **Grid Gap**: 10px

## Components

- `App.svelte` - Main application container
- `CardList.svelte` - Card list with file upload and demo loader
- `CardItem.svelte` - Individual editable card item
- `DropZone.svelte` - Drag and drop upload zone
- `CardGrid.svelte` - A4 page grid layout
- `Card.svelte` - Individual printable card

## Technologies

- [Svelte](https://svelte.dev/) - Component framework
- [Vite](https://vitejs.dev/) - Build tool and dev server
