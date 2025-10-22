import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd # / GeoPandas
st.set_page_config(layout="wide")
st.title("Leafmap 國界")

with st.sidebar:
 st.header("底圖選擇")
 option = st.selectbox(
 "選擇底圖 ?",
 ("OpenTopoMap", "Esri.WorldImagery", "CartoDB.DarkMatter")
 )

url = "jiayi_kaohsung.geojson"
gdf = gpd.read_file(url)
st.dataframe(gdf.head())
m = leafmap.Map(center=[0, 0])
m.add_basemap(option)
m.add_gdf(gdf, 
          layer_name="Country Interest",
          style={"color": "black", "weight": 5})
m.add_layer_control() 
m.to_streamlit(height=700)
