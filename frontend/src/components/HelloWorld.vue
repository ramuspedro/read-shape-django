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
            <input type="file" ref="file" accept=".zip">
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
        let map = this.map;
        
        let files = this.$refs.file.files;
        if (files.length == 0) {
          alert("Nothing sent!")
          return; //do nothing if no file given yet
        }

        let file = files[0];

        handleZipFile(file);

        //More info: https://developer.mozilla.org/en-US/docs/Web/API/FileReader
        function handleZipFile(file) {          
          let reader = new FileReader();
          reader.onload = function () {            
            if (reader.readyState != 2 || reader.error) {
              return;
            } else {
              convertToLayer(reader.result);
            }
          }
          reader.readAsArrayBuffer(file);
        }

        function convertToLayer(buffer){
          console.log("map", map);
          
          // console.log("buffer", shp(buffer));
          shp(buffer).then(function(geojson){	//More info: https://github.com/calvinmetcalf/shapefile-js
            var layer = L.shapefile(geojson).addTo(map);//More info: https://github.com/calvinmetcalf/leaflet.shapefile
            console.log(layer);
          });
        }
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