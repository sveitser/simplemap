# simplemap
============
###Overview
This Python library allows you to plot GPS coordinates on a standalone google map contained in an HTML file. Functionality is focused around mapping of points, so other google maps API features will not be implemented (i.e. directions, reverse geocoding, etc).  

My plans for features to be implemented in the mediate future are:
* Google map interface event callbacks
* Custom marker labels
* Custom marker text
* Customer marker images

=======

###Installation
Installation is very straightforward. Simply clone the repository and install the necessary requirements 
```sh
git clone https://github.com/patrick--/simplemap/
cd simplemap
pip install -r requirements.txt
```

=========

###Prequsites

Before using this library you will need to obtain a Google Maps Javascript API key. The following link has instructions on getting a key
* [Get a Google Maps API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)


Once you get a key, make sure to put it in the `config.json` file. Any problems with API authentication will result in an error popup in your `output.html` file. 

![API Error Example](http://i.imgur.com/g6aG2Zk.png "API Error")



=======

###Usage

First, import the simplemap library
```py
import simplemap
```

Next,  initialize your map object: `simplemap.Map()`
#####Parameters:

* `title`  - The title of the HTML map webpage
* `center` - `list` object containing the latitude and longitude of where the map should be centered
* `zoom` - Zoom level of the map, defaults to 11 - Optional
* `markers` - `list` of markers, where a marker is a `list`: optional hovertext, lat and lon - Optional
* `html_template` - HTML template used to generate a map. Currently the default value of `basic.html` is the only option - Optional
* `config_file` - JSON file containing the google maps `api_key`, defaults to `config.json` - Optional

Finally, write the map to an HTML file: `Map.write()`
#####Parameters:
* `output_file_name`  - Filename that HTML will be written to


###Examples

An example showing typical usage

```py
import simplemap

map_title = 'Example Map'
center_point  = [34.5124, -118.1111]
gps_markers = [ ['Example text', 34.4563,-118.1241], [34.6432,-118.1554] ]

example_map = simplemap.Map(map_title, center_point, markers=gps_markers)
example_map.write('example.html')

```

This example demonstrates that `markers` is a property of the `Map()` class - so it can be given a value after initialization

```py
import simplemap

example_map = simplemap.Map('Test Title', [34.5124, -118.1111])
example_map.markers = [ ['Example text', 34.4563,-118.1241], [34.6432,-118.1554] ]
example_map.write('example.html')

```