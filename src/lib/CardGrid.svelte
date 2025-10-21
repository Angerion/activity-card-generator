<script>
  import Card from './Card.svelte';

  export let cards = [];

  const cardsPerPage = 24;
  
  // Group cards into pages
  $: pages = Array.from(
    { length: Math.ceil(cards.length / cardsPerPage) },
    (_, i) => cards.slice(i * cardsPerPage, (i + 1) * cardsPerPage)
  );
</script>

<div id="pages">
  {#each pages as pageCards}
    <div class="page-container">
      <div class="card-grid">
        {#each pageCards as card}
          <Card {card} />
        {/each}
      </div>
    </div>
  {/each}
</div>

<style>
  #pages {
    width: 100%;
  }

  .page-container {
    width: 210mm;
    height: 297mm;
    background: white;
    margin: 20px auto;
    padding: 15mm;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    position: relative;
  }

  @media print {
    .page-container {
      margin: 0;
      box-shadow: none;
      page-break-after: always;
    }

    .page-container:last-child {
      page-break-after: auto;
    }
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(4, 170px);
    grid-template-rows: repeat(6, 170px);
    gap: 10px;
    width: fit-content;
  }
</style>