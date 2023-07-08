#Core Libraries
import pandas as pd

# for Water Map
import networkx as nx
import osmnx as ox

#for Colors
from Colors.BgColorName import *

# Color Selection Web Site
# https://htmlcolorcodes.com/

class WaterAdd():
    def Water(point = None, distance = None, watercolor = None):
        '''
        point and distance are same as MapCode file
        '''
        if type(point[0]) == float:
            G1 = ox.graph_from_point(point, distance, dist_type='bbox', network_type='all', 
                                    simplify=True, retain_all=True, truncate_by_edge=False, clean_periphery=False, 
                                    custom_filter='["natural"~"water"]')
            G2 = ox.graph_from_point(point, distance, dist_type='bbox', network_type='all', 
                                    simplify=True, retain_all=True, truncate_by_edge=False, clean_periphery=False, 
                                    custom_filter='["waterway"~"river"]')
            Gwater = nx.compose(G1, G2)
        else:
            G1 = ox.graph_from_place(point, retain_all=True, simplify = False, custom_filter='["natural"~"water"]')
            G2 = ox.graph_from_place(point, retain_all=True, simplify = False,custom_filter='["waterway"~"river"]')
            Gwater = nx.compose(G1, G2)

        empty = []
        empty_1 = []
        empty_2 = []
        LocationData = []
        
        for trash, trash_1, trash_2, data in Gwater.edges(keys=True, data=True):
            empty.append(trash)
            empty_1.append(trash_1)
            empty_2.append(trash_2)
            LocationData.append(data)    
        
        LocationData = pd.DataFrame(LocationData)

        # Image 
        if type(watercolor) is list:
            R = watercolor[0] 
            G = watercolor[1]
            B = watercolor[2]
            FileNameColor = ColorConverter.ColorName(R,G,B)
            wcolor = ColorConverter.RGBHex(R,G,B)
        
        elif type(watercolor) is tuple:
            R = watercolor[0] 
            G = watercolor[1]
            B = watercolor[2]
            FileNameColor = ColorConverter.ColorName(R,G,B)
            wcolor = ColorConverter.RGBHex(R,G,B)
        
        else:
            FileNameColor = ColorConverter.ColorName(watercolor)
            wcolor = watercolor
        
        # List to store colors
        WaterColors = []
        WaterWidths = []

        # Colors and Water way Width
        for item in LocationData["length"]:
            if item > 400: 
                color = wcolor
                linewidth = 2.6
            elif item <= 400:
                color = wcolor
                linewidth = 1.1
            else:
                color = wcolor
                linewidth = 1.1

            WaterColors.append(color)    
            WaterWidths.append(linewidth)


        fig, ax = ox.plot_graph(Gwater, node_size=0,figsize=(108, 160), 
                                dpi = 10000, save = False, edge_color=WaterColors,
                                edge_linewidth=WaterWidths, edge_alpha=1)

        fig.tight_layout(pad=0)
        fig.savefig(f".\Images/{FileNameColor}water.png", dpi=1000, bbox_inches='tight', format="png", 
                    facecolor=fig.get_facecolor(), transparent=True)
        
        return fig
