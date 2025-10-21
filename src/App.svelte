<script>
  import CardList from './lib/CardList.svelte';
  import CardGrid from './lib/CardGrid.svelte';

  let cards = [];
  let generatedCards = [];

  function handleFilesSelected(event) {
    cards = event.detail;
  }

  function handleGenerateCards() {
    // Duplicate cards based on count
    const allCards = [];
    cards.forEach(card => {
      for (let i = 0; i < card.count; i++) {
        allCards.push({
          imagePath: card.imagePath,
          text: card.text
        });
      }
    });
    generatedCards = allCards;
  }

  function handlePrint() {
    window.print();
  }

  function handleCardUpdate(event) {
    const { index, field, value } = event.detail;
    cards = cards.map((card, i) => 
      i === index ? { ...card, [field]: value } : card
    );
  }

  function handleCardRemove() {
    generatedCards = [];
  }
</script>

<div class="app">
  <div class="controls">
    <h1>Activity Card Generator</h1>
    <CardList 
      bind:cards 
      on:filesSelected={handleFilesSelected}
      on:generateCards={handleGenerateCards}
      on:print={handlePrint}
      on:cardUpdate={handleCardUpdate}
      on:cardRemove={handleCardRemove}
    />
  </div>

  {#if generatedCards.length > 0}
    <CardGrid cards={generatedCards} />
  {/if}
</div>

<style>
  :global(*) {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  :global(body) {
    font-family: Arial, sans-serif;
    padding: 20px;
    background: #f0f0f0;
  }

  .app {
    width: 100%;
  }

  .controls {
    margin-bottom: 20px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .controls h1 {
    margin-bottom: 15px;
    color: #333;
  }

  /* Print Styles */
  @media print {
    :global(body) {
      padding: 0;
      background: white;
    }

    .controls {
      display: none;
    }
  }

  @page {
    size: A4;
    margin: 0;
  }
</style>
