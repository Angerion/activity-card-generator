<script>
  import { createEventDispatcher } from 'svelte';

  export let card;
  export let index;

  const dispatch = createEventDispatcher();

  function handleTextChange(event) {
    dispatch('update', {
      index,
      field: 'text',
      value: event.target.value
    });
  }

  function handleCountChange(event) {
    const value = parseInt(event.target.value, 10);
    if (!isNaN(value) && value > 0) {
      dispatch('update', {
        index,
        field: 'count',
        value
      });
    }
  }
</script>

<div class="card-item">
  <img src={card.imagePath} alt={card.text} />
  <div class="card-item-info">
    <input 
      type="text" 
      class="card-item-name-input" 
      value={card.text}
      on:input={handleTextChange}
      placeholder="Card name"
    />
    <div class="card-item-count-container">
      <label for="count-{index}">Count:</label>
      <input 
        type="number" 
        id="count-{index}"
        class="card-item-count-input" 
        value={card.count}
        on:input={handleCountChange}
        min="1"
      />
    </div>
  </div>
</div>

<style>
  .card-item {
    display: flex;
    align-items: center;
    padding: 8px;
    margin-bottom: 5px;
    background: white;
    border-radius: 4px;
    border: 1px solid #e0e0e0;
  }

  .card-item img {
    width: 40px;
    height: 40px;
    object-fit: cover;
    margin-right: 10px;
    border-radius: 4px;
  }

  .card-item-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 5px;
  }

  .card-item-name-input {
    font-weight: bold;
    color: #333;
    border: 1px solid #ddd;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 14px;
    transition: border-color 0.2s;
  }

  .card-item-name-input:focus {
    outline: none;
    border-color: #4CAF50;
  }

  .card-item-count-container {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .card-item-count-container label {
    color: #666;
    font-size: 12px;
  }

  .card-item-count-input {
    width: 60px;
    border: 1px solid #ddd;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 12px;
    transition: border-color 0.2s;
  }

  .card-item-count-input:focus {
    outline: none;
    border-color: #4CAF50;
  }
</style>