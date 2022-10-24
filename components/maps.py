import geopandas as gpd
import pandas as pd
import json

# state geoJSOn
with open('./state-geojson/states_india.geojson') as f:
    all_states_geojson = pd.DataFrame(json.load(f))


