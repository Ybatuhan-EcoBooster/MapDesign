# Core Libraries
import pandas as pd
import numpy as np

#For Colors
from Colors.BgColorName import ColorConverter

# Map Libraries And Visulazation
import osmnx as ox
from WaterMap import WaterAdd 

# To stick to  maps
from PIL import Image, ImageOps, ImageColor, ImageFont, ImageDraw 
from ImageName import *

# Color Selection Web Site
# https://htmlcolorcodes.com/


def Map(self = None, dist = None, background = None, Water_Graph = None , Water_color = None):

    if type(self[0]) == float:
        LocationPoint = ox.graph_from_point(self, dist=dist , retain_all=True, 
                                            simplify = True, network_type='all',dist_type="bbox")
    else:
        LocationPoint = ox.graph_from_place(self,  retain_all=True, 
                                            simplify = True, network_type='all')
    
    # Data Highway parameter names defination web site https://wiki.openstreetmap.org/wiki/Map_features
    # dist = sacale of map distance from sky vison
    # network_type : 
    '''
    - `drive` - get drivable public streets (but not service roads)
    - `drive_service` - get drivable streets, including service roads
    - `walk` - get all streets and paths that pedestrians can use (this network type ignores one-way directionality)
    - `bike` - get all streets and paths that cyclists can use
    - `all` - download all non-private OSM streets and paths
    - `all_private` - download all OSM streets and paths, including private-access ones
    '''
    empty = []
    empty_1 = []
    empty_2 = []
    LocationPoint_data = []
        
    for trash, trash_1, trash_2, data in LocationPoint.edges(keys=True, data=True):
        empty.append(trash)
        empty_1.append(trash_1)
        empty_2.append(trash_2)
        LocationPoint_data.append(data)    

    # Lists to store colors and widths 
    roadColors = []
    roadWidths = []

    LocationPoint_data = pd.DataFrame(LocationPoint_data)

    # Colors and Way Width
    for item in LocationPoint_data["length"]:
        if item <= 100: 
            linewidth = 0.09
            color = "#111111"
                
        elif item > 100 and item <= 200:
            linewidth = 0.11 
            color = "#111111"
                
        elif item > 200 and item <= 400:
            linewidth = 0.20 
            color = "#111111"
                
        elif item > 400 and item <= 800:
            color = "#111111"
            linewidth = 0.25  
        else:
            color = "#000000"
            linewidth = 0.40         

                
        roadColors.append(color)
        roadWidths.append(linewidth)

    # File  Colors Name Assign 
    if type(background) is list:
        R = background[0] 
        G = background[1]
        B = background[2]
        FileNameColor = ColorConverter.ColorName(R,G,B)
        bgcolor = ColorConverter.RGBHex(R,G,B)
    elif type(background) is tuple:
        R = background[0] 
        G = background[1]
        B = background[2]
        FileNameColor = ColorConverter.ColorName(R,G,B)
        bgcolor = ColorConverter.RGBHex(R,G,B)
    else:
        FileNameColor = ColorConverter.ColorName(background)
        bgcolor = background

    # Image 
    fig, ax = ox.plot_graph(LocationPoint,node_size=0,figsize=(108, 160),
                                dpi = 1000,bgcolor = bgcolor,
                                save = False,edge_color=roadColors,
                                edge_linewidth=roadWidths, edge_alpha=1)
    fig.tight_layout(pad=0)
    fig.savefig(f".\Images/{FileNameColor}Basic.jpg", dpi=1000, bbox_inches='tight', format="jpg", 
                facecolor=fig.get_facecolor(), transparent=False)

    # For Water Image
    if Water_Graph == True:
        WaterGraph = WaterAdd.Water(point = self,distance = dist, watercolor = Water_color)
        
        # Main Image + Water Image Combine 

        img_road  = Image.open(f"D:\dosyalar\Github\MapDesign\Images\{FileNameColor}Basic.jpg")
        img_water_name = FileName()
        img_water = Image.open(f"D:\dosyalar\Github\MapDesign\Images/{img_water_name}.png")

        # Paste the first image onto the combined image

        # Create a new image with the same size as the first image
        combined_image = Image.new("RGBA", img_road.size)
        # Paste the first image onto the combined image
        combined_image.paste(img_road, (0, 0))

        # Paste the second image with transparency onto the combined image
        combined_image.paste(img_water, (0, 0), mask=img_water)

        # Save the combined image
        combined_image.save("D:\dosyalar\Github\MapDesign\Images/result.png")
    else:
        pass

    return fig,WaterGraph
