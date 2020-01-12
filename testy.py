from owslib.wfs import WebFeatureService
import os

wfs = WebFeatureService(url='http://localhost:8080/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities', version='1.1.0')
response = wfs.getfeature(typename='wowGIS:v_broken_isles', srsname='urn:x-ogc:def:crs:EPSG:4087')

os.chdir("C:\\Users\\osko1\\OneDrive\\Zalaczniki_email\\Pulpit")
out = open('data.gml', 'wb')
out.write(bytes(response.read(), 'UTF-8'))
out.close()