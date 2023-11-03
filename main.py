if __name__ == '__main__':
    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import Point  # Import the Point class if it's not already imported

    inputfile = "DMR5G.xyz"
    df = pd.read_table(inputfile, skiprows=0, delim_whitespace=True, names=['x', 'y', 'z'])
    print(df.head(3))

    from sqlalchemy import create_engine
    engine = create_engine("postgresql://postgres:fr24Password@localhost:5432/pdb")

    # Create a GeoSeries with Point objects from the x and y columns
    geometry = [Point(x, y) for x, y in zip(df['x'], df['y'])]

    # Create the GeoDataFrame and set the geometry column
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    #gdf = gdf.set_geometry()
    gdf.to_postgis("pilsen", engine, if_exists="append", chunksize=10000)

