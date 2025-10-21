<script>
  import { createEventDispatcher } from 'svelte';
  import DropZone from './DropZone.svelte';
  import CardItem from './CardItem.svelte';

  export let cards = [];

  const dispatch = createEventDispatcher();

  function parseFilename(filename) {
    const nameWithoutExt = filename.replace(/\.[^/.]+$/, '');
    const match = nameWithoutExt.match(/^(.+)_(\d+)$/);

    if (match) {
      const name = match[1];
      const count = parseInt(match[2], 10);
      const text = name.charAt(0).toUpperCase() + name.slice(1);
      return { text, count };
    } else {
      const text = nameWithoutExt.charAt(0).toUpperCase() + nameWithoutExt.slice(1);
      return { text, count: 1 };
    }
  }

  function handleFiles(files) {
    const imageFiles = files.filter(file => file.type.startsWith('image/'));

    const promises = imageFiles.map(file => {
      return new Promise((resolve) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          const imagePath = e.target.result;
          const { text, count } = parseFilename(file.name);

          resolve({
            imagePath,
            text,
            count
          });
        };
        reader.readAsDataURL(file);
      });
    });

    Promise.all(promises).then(newCards => {
      cards = [...cards, ...newCards];
      dispatch('filesSelected', cards);
    });
  }

  async function loadDemoData() {
    const demoImages = [
      { path: '/examples/koupání_12.png', text: 'Koupání', count: 12 },
      { path: '/examples/běhání_6.png', text: 'Běhání', count: 6 },
      { path: '/examples/skákání_8.png', text: 'Skákání', count: 8 },
      { path: '/examples/čtení_4.png', text: 'Čtení', count: 4 }
    ];

    cards = [];

    for (const img of demoImages) {
      try {
        const response = await fetch(img.path);
        const blob = await response.blob();
        const reader = new FileReader();

        await new Promise((resolve) => {
          reader.onload = (e) => {
            cards = [...cards, {
              imagePath: e.target.result,
              text: img.text,
              count: img.count
            }];
            resolve();
          };
          reader.readAsDataURL(blob);
        });
      } catch (error) {
        console.error(`Failed to load ${img.path}:`, error);
      }
    }

    dispatch('filesSelected', cards);
  }

  function handleGenerateCards() {
    dispatch('generateCards');
  }

  function handlePrint() {
    dispatch('print');
  }

  function handleCardUpdate(event) {
    dispatch('cardUpdate', event.detail);
  }

  function handleDrop(event) {
    handleFiles(event.detail);
  }

  function handleCardRemove(event) {
    const { index } = event.detail;
    cards = cards.filter((_, i) => i !== index);
    dispatch('cardRemove', { index });
  }

  function handleFileInput(event) {
    const files = Array.from(event.target.files);
    handleFiles(files);
  }

  let fileInput;

  function openFileDialog() {
    fileInput.click();
  }
</script>

<DropZone on:drop={handleDrop} on:click={openFileDialog} />

<input
  type="file"
  accept="image/*"
  multiple
  bind:this={fileInput}
  on:change={handleFileInput}
  style="display: none;"
/>

<div class="buttons">
  <button class="button" on:click={openFileDialog}>
    Select Images
  </button>
  <button class="button secondary" on:click={handleGenerateCards}>
    Generate Cards
  </button>
  <button class="button secondary" on:click={handlePrint}>
    Print
  </button>
  <button class="button secondary" on:click={loadDemoData}>
    Load Demo
  </button>
</div>

<div class="card-list">
  {#if cards.length === 0}
    <p style="color: #999;">No cards added yet</p>
  {:else}
    {#each cards as card, index}
      <CardItem
        {card}
        {index}
        on:update={handleCardUpdate}
        on:remove={handleCardRemove}
      />
    {/each}
  {/if}
</div>

<style>
  .buttons {
    margin-bottom: 15px;
  }

  .button {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    margin-right: 10px;
  }

  .button:hover {
    background: #45a049;
  }

  .button.secondary {
    background: #2196F3;
  }

  .button.secondary:hover {
    background: #0b7dda;
  }

  .card-list {
    margin-top: 15px;
    max-height: 300px;
    overflow-y: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    background: #fafafa;
  }
</style>