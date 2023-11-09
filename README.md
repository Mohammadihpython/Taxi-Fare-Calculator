# Taxi Fare Calculator Service

# setup Valhalla Service And FastAPI

### It is start valhalla service with latest data of iran

```
docker-compose up -build
```

### Set up Only valhalla with docker 

### download a file to custom_files and start valhalla

```
mkdir custom_files
```

```
wget -O custom_files/iran-latest.osm.pbf https://download.geofabrik.de/asia/iran.html
```
```
docker run -dt --name valhalla_gis-ops -p 8002:8002 -v $PWD/custom_files:/custom_files ghcr.io/gis-ops/docker-valhalla/valhalla:latest

```


### or let the container download the file for you

```
docker run -dt --name valhalla_gis-ops -p 8002:8002 -v $PWD/custom_files:/custom_files -e tile_urls=<https://download.geofabrik.de/asia/iran-latest.osm.pbf> ghcr.io/gisops/valhalla/
```

