<template>
  <div class="hello">
    <div id="app" class="container">
      <div class="row">
        <div class="col-md-9">
          <!-- The map goes here -->
          <div id="map" class="map"></div>
        </div>
        <div class="col-md-3">
          <!-- The layer checkboxes go here -->
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
    data: {
      map: null,
      tileLayer: null,
      layers: [],
    },
    methods: {
      initMap() {
        this.map = L.map('map').setView([38.63, -90.23], 12);
        this.tileLayer = L.tileLayer(
          'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
          }
        );
        this.tileLayer.addTo(this.map);
      },
      initLayers() {},
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