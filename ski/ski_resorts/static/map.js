const osm = "https://www.openstreetmap.org/copyright";
const copy = `© <a href='${osm}'>OpenStreetMap</a>`;
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });

map
  .locate()
  .on("locationfound", (e) =>
    map.setView(e.latlng, 8)
  )
  .on("locationerror", () =>
    map.setView([0, 0], 5)
  );
const layerGroup = L.layerGroup().addTo(map)


async function load_markers() {
  const markers_url = `/api/skiareas/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response = await fetch(
    markers_url
  );
  const geojson = await response.json();
  return geojson;
}

async function render_markers() {
  const markers = await load_markers();
  layerGroup.clearLayers();
  L.geoJSON(markers,{
    pointToLayer: function(feature,latlng){
      return L.marker(latlng, { icon: createSvgIcon(feature) });
    },
    onEachFeature: (feature, layer) => {
      const group = feature.properties.passaffiliation; 
      if (layerGroups[group]) {
          layer.addTo(layerGroups[group]);
      }
      // Add a pop-up for each feature
      if (feature.properties && feature.properties.passaffiliation) {
        layer.bindPopup(() => {
            let popupContent = `<b>${feature.properties.name}</b><br>`;
            // Add website link if it exists
            if (feature.properties.website) {
                popupContent += `<a href="${feature.properties.website}" target="_blank">Ski Resort Website</a><br>`;
            }
            // Add trail map link if it exists
            if (feature.properties.id) {
                popupContent += `<a href=https://skimap.org/skiareas/view/${feature.properties.id} target="_blank">Trail Map</a>`;
            }
        
            return popupContent;
        });
      }
  }

      
  }
  )
}

map.on("moveend", render_markers);
// Layer groups
const layerGroups = {
  "Ikon": L.layerGroup().addTo(map),
  "Indy": L.layerGroup().addTo(map),
  "Epic": L.layerGroup().addTo(map),
  "Unaffiliated": L.layerGroup().addTo(map)
};
const layerControl = L.control.layers(null, layerGroups).addTo(map);

function createSvgIcon(feature) {
  switch(feature.properties.passaffiliation) {
    case "Ikon":
      return L.icon({
        iconUrl: 'static/Ikon.svg',
        iconSize:     [16, 16],
        iconAnchor:   [22, 22],
        popupAnchor:  [-3, -26]})
    case "Epic":
      return L.icon({
        iconUrl: 'static/Epic.svg',
        iconSize:     [16, 16], 
        iconAnchor:   [22, 22], 
        popupAnchor:  [-3, -26]})
    case "Indy":
      return L.icon({
        iconUrl: 'static/indypass.svg',
        iconSize:     [16, 16], 
        iconAnchor:   [22, 22],
        popupAnchor:  [-3, -26]})
    default:
      return L.icon({
        iconUrl: 'static/skiier.svg',
        iconSize:     [16, 16], 
        iconAnchor:   [22, 22],
        popupAnchor:  [-3, -26]})
          
  }

}