<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let isDragOver = false;

  function handleDragOver(event) {
    event.preventDefault();
    isDragOver = true;
  }

  function handleDragLeave() {
    isDragOver = false;
  }

  function handleDrop(event) {
    event.preventDefault();
    isDragOver = false;
    const files = Array.from(event.dataTransfer.files);
    dispatch('drop', files);
  }

  function handleClick() {
    dispatch('click');
  }
</script>

<div 
  class="drop-zone"
  class:dragover={isDragOver}
  on:dragover={handleDragOver}
  on:dragleave={handleDragLeave}
  on:drop={handleDrop}
  on:click={handleClick}
  role="button"
  tabindex="0"
  on:keydown={(e) => e.key === 'Enter' && handleClick()}
>
  <p>Drag and drop images here or click to select</p>
  <p style="font-size: 12px; color: #666; margin-top: 10px;">
    Filename format: name_count.png (e.g., koupání_12.png)
  </p>
</div>

<style>
  .drop-zone {
    border: 3px dashed #ccc;
    border-radius: 8px;
    padding: 40px;
    text-align: center;
    background: #fafafa;
    transition: all 0.3s;
    cursor: pointer;
    margin-bottom: 15px;
  }

  .drop-zone.dragover {
    border-color: #4CAF50;
    background: #e8f5e9;
  }

  .drop-zone:hover {
    border-color: #999;
  }
</style>