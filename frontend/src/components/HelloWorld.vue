<template>
  <div class="hello">
    <div id="app" class="container">
      <div class="row">
        <div class="col-md-9">
          <!-- The map goes here -->
          <div id="map" class="map"></div>
        </div>
        <div class="col-md-3">
          <h4 style="margin-top: 2rem;">Envio de shape zipado</h4>
          <div style="margin-top: 2rem; margin-bottom: 2rem;">
            <input type="file">
          </div>
          <div>
            <button type="button" class="btn btn-raised btn-primary" @click="sendShape()">Enviar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String
    },
    data() {
      return {
        map: null,
        tileLayer: null,
        layers: [],
      }
    },
    methods: {
      initMap() {
        this.map = L.map('map').setView([-1.45502, -48.5024], 4);
        this.tileLayer = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        });
        this.tileLayer.addTo(this.map);
      },
      initLayers() {},
      sendShape() {
        console.log("TESTE");
        
      }
    },
    mounted() {
      this.initMap();
      this.initLayers();
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .map {
    height: 600px;
    margin-top: 2rem;
  }
</style>