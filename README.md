# wow gis - version 0.1.1
**QGIS Plugin** importing spatial data from **World of Warcraft** game to your computer!

Plugin can import both raster and vector data by running WFS and WMS requests to geoserver. 
Currently it's fairy simple and can be considered as proof of concept, but in the future can be easly developed by adding more importable layers, like rivers, dungeon locations, mountain ranges etc. 

## About WOW maps
Because some maps in World of Warcraft are poorly scaled, we cannot achieve 100% compability. Diffrent continents and isles looks much bigger or smaller compared to others depending of map scale (I'm looking at you, Broken Isles!). I tried to achieve the best possible esitmation of where continents are, using world map as reference. 
Measurement of world were done using WeakAuras2 addon, as it can calculate range. 

All maps are made based on World of Warcraft Battle of Azeroth 8.2.5 version of the game. 

The only world mapped right now is Azeroth.

The CRS used is WGS 84 / Plate Carree (EPSG:32662). You can read more about it here: https://epsg.io/32662
It was choosen because its simplicity.

## Layers avaible right now:
### Vector
- Every continent with separate zones 
- Major cities with information about their affiliation (horde/alliance/neutral)
### Raster
- Georeferenced world map of Azeroth
- Georeferenced maps of every continent.

## Contact
If you have any question, issue or just want to help by making few more layers by yourself, by all means you are welcome to do so. Just contact me here on github :) 
