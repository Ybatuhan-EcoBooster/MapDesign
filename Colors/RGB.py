# Core Libraries
import pandas as pd 

# For Colors
import webcolors

def Colors():
    # Dataframes 
    df = pd.read_csv("colorhexa_com.csv")
    df_2 = pd.read_csv("wikipedia_color_names.csv")

    Color = pd.concat([df,df_2],ignore_index=True,join="inner")


    # Dataframe Cleaning
    Color = Color.drop_duplicates(subset=["Hex (24 bit)"])
    Color = Color.reset_index(drop=True)
    Color["Hex"] = Color["Hex (24 bit)"]
    Color = Color[["Name","Hex (24 bit)","Hex","Red (8 bit)","Green (8 bit)","Blue (8 bit)"]]
    Color.columns = ["Name","Colors","Hex","R","G","B"]
    Color["RGB"] = Color["R"].astype(str) + "," + Color["G"].astype(str) + "," + Color["B"].astype(str)
    Color["RGB"] = [tuple(map(int, item.split(","))) for item in Color["RGB"]]


    # Colors Style
    # Define a function to apply the CSS style to hex color codes
    def color_styler(hex_code):
        style = f'background-color: {hex_code}; color: {hex_code};'
        return style

    # Apply the CSS style to the 'Color' column
    style = Color.style.applymap(color_styler, subset=['Colors'])


    # Save as Excel file
    style.to_excel('styled_dataframe.xlsx', index=False)

    # Save as HTML file
    style.to_html('styled_dataframe.html', index=False)

    return style