import geopandas as gpds
import pandas as pd

gpds.tools.geocode("Rio Bonito, RJ",provider = "nominatim",user_agent = "my_app")