<script>
  export let card;
</script>

<div class="card">
  <div class="card-content">
    <div class="card-image-area">
      <img src={card.imagePath} alt={card.text} />
    </div>
    <div class="card-text-area">
      {card.text}
    </div>
  </div>
</div>

<style>
  .card {
    width: 170px;
    height: 170px;
    background: #444;
    border-radius: 15px;
    padding: 5px;
    display: flex;
    flex-direction: column;
  }

  .card-content {
    background: white;
    border-radius: 10px;
    height: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  .card-image-area {
    height: 135px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    overflow: hidden;
  }

  .card-image-area img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }

  .card-text-area {
    height: 25px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    font-size: 12px;
    font-weight: bold;
    color: #333;
    text-align: center;
    padding: 0 5px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
</style>