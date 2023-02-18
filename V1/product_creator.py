from PIL import Image
import os
import csv

"""GBLOBAL VARIABLES"""

garmentdict = {"Mens":
               {'type': 'T-SHIRT',
        'folder': 'SHIRT/',
        'size':['Small', 'Medium', 'Large', 'Extra Large'],
        'weight':454,
        'price':25.00,
        'Front':{'xx':595,'yy':335,'r': 0.5,'sx': 810,'sy':1026,'mask':'NONE'},
        'Back':{'xx':601,'yy':209,'r':0.0,'sx': 810,'sy':1026,'mask':'NONE'},
        'tag':{'Red':'Red_Tag.png','Blue':'Blue_Tag.png','Orange':'Orange_Tag.png','Maroon':'Maroon_Tag.png'},
        'Color_Front':{'Aqua' : 'Mens_Aqua_Front.png',	'Ash' : 'Mens_Ash_Front.png',	'Asphalt' : 'Mens_Asphalt_Front.png',	'Athletic Heather' : 'Mens_Athletic_Heather_Front.png',	'Autumn' : 'Mens_Autumn_Front.png',	'Berry' : 'Mens_Berry_Front.png','Black' : 'Mens_Black_Front.png','Brown' : 'Mens_Brown_Front.png','Canvas Red' : 'Mens_Canvas_Red_Front.png','Cardinal' : 'Mens_Cardinal_Red_Front.png','Coral' : 'Mens_Coral_Front.png','Dark Grey' : 'Mens_Dark_Grey_Front.png','Deep Teal' : 'Mens_Deep_Teal_Front.png','Forest' : 'Mens_Forest_Front.png',	'Gold' : 'Mens_Gold_Front.png',	'Kelly' : 'Mens_Kelly_Front.png',	'Leaf' : 'Mens_Leaf_Front.png',	'Light Blue' : 'Mens_Light_Blue_Front.png',	'Maroon' : 'Mens_Maroon_Front.png',	'Mint' : 'Mens_Mint_Front.png',	'Mustard' : 'Mens_Mustard_Front.png',	'Navy' : 'Mens_Navy_Front.png',	'Ocean Blue' : 'Mens_Ocean_Blue_Front.png',	'Olive' : 'Mens_Olive_Front.png',	'Orange' : 'Mens_Orange_Front.png',	'Pink' : 'Mens_Pink_Front.png',	'Red' : 'Mens_Red_Front.png',	'Silver' : 'Mens_Silver_Front.png',	'Soft Cream' : 'Mens_Soft_Cream_Front.png',	'Steel Blue' : 'Mens_Steel_Blue_Front.png',	'Teal' : 'Mens_Teal_Front.png',	'Team Purple' : 'Mens_Team_Purple_Front.png',	'Blue' : 'Mens_True_Royal_Front.png',	'Turqouise' : 'Mens_Turquoise_Front.png',	'White' : 'Mens_White_Front.png',	'Yellow' : 'Mens_Yellow_Front.png'},
        'Color_Back':{'Aqua' : 'Mens_Aqua_Back.png',	'Ash' : 'Mens_Ash_Back.png',	'Asphalt' : 'Mens_Asphalt_Back.png',	'Athletic Heather' : 'Mens_Athletic_Heather_Back.png',	'Autumn' : 'Mens_Autumn_Back.png',	'Berry' : 'Mens_Berry_Back.png',	'Black' : 'Mens_Black_Back.png',	'Brown' : 'Mens_Brown_Back.png',	'Canvas Red' : 'Mens_Canvas_Red_Back.png',	'Cardinal' : 'Mens_Cardinal_Red_Back.png',	'Coral' : 'Mens_Coral_Back.png',	'Dark Grey' : 'Mens_Dark_Grey_Back.png',	'Deep Teal' : 'Mens_Deep_Teal_Back.png',	'Forest' : 'Mens_Forest_Back.png',	'Gold' : 'Mens_Gold_Back.png',	'Kelly' : 'Mens_Kelly_Back.png',	'Leaf' : 'Mens_Leaf_Back.png',	'Light Blue' : 'Mens_Light_Blue_Back.png',	'Maroon' : 'Mens_Maroon_Back.png',	'Mint' : 'Mens_Mint_Back.png',	'Mustard' : 'Mens_Mustard_Back.png',	'Navy' : 'Mens_Navy_Back.png',	'Ocean Blue' : 'Mens_Ocean_Blue_Back.png',	'Olive' : 'Mens_Olive_Back.png',	'Orange' : 'Mens_Orange_Back.png',	'Pink' : 'Mens_Pink_Back.png',	'Red' : 'Mens_Red_Back.png',	'Silver' : 'Mens_Silver_Back.png',	'Soft Cream' : 'Mens_Soft_Cream_Back.png',	'Steel Blue' : 'Mens_Steel_Blue_Back.png',	'Teal' : 'Mens_Teal_Back.png',	'Team Purple' : 'Mens_Team_Purple_Back.png',	'True Royal' : 'Mens_True_Royal_Back.png',	'Turqouise' : 'Mens_Turquoise_Back.png',	'White' : 'Mens_White_Back.png',	'Yellow' : 'Mens_Yellow_Back.png'},
        'shopify_tags':"T-Shirt",
        'sku':{'brand':'A'}},

        "Womens":
               {'type': 'T-SHIRT',
        'folder': 'SHIRT/',
        'size':['Small', 'Medium', 'Large', 'Extra Large'],
        'weight':454,
        'price':25.00,
        'Front':{'xx':595,'yy':335,'r': 0.5,'sx': 810,'sy':1026,'mask':'NONE'},
        'Back':{'xx':601,'yy':209,'r':0.0,'sx': 810,'sy':1026,'mask':'NONE'},
        'tag':{'Red':'Red_Tag.png','Blue':'Blue_Tag.png','Orange':'Orange_Tag.png','Maroon':'Maroon_Tag.png'},
        'Color_Front':{'Aqua' : 'Mens_Aqua_Front.png',	'Ash' : 'Mens_Ash_Front.png',	'Asphalt' : 'Mens_Asphalt_Front.png',	'Athletic Heather' : 'Mens_Athletic_Heather_Front.png',	'Autumn' : 'Mens_Autumn_Front.png',	'Berry' : 'Mens_Berry_Front.png','Black' : 'Mens_Black_Front.png','Brown' : 'Mens_Brown_Front.png','Canvas Red' : 'Mens_Canvas_Red_Front.png','Cardinal' : 'Mens_Cardinal_Red_Front.png','Coral' : 'Mens_Coral_Front.png','Dark Grey' : 'Mens_Dark_Grey_Front.png','Deep Teal' : 'Mens_Deep_Teal_Front.png','Forest' : 'Mens_Forest_Front.png',	'Gold' : 'Mens_Gold_Front.png',	'Kelly' : 'Mens_Kelly_Front.png',	'Leaf' : 'Mens_Leaf_Front.png',	'Light Blue' : 'Mens_Light_Blue_Front.png',	'Maroon' : 'Mens_Maroon_Front.png',	'Mint' : 'Mens_Mint_Front.png',	'Mustard' : 'Mens_Mustard_Front.png',	'Navy' : 'Mens_Navy_Front.png',	'Ocean Blue' : 'Mens_Ocean_Blue_Front.png',	'Olive' : 'Mens_Olive_Front.png',	'Orange' : 'Mens_Orange_Front.png',	'Pink' : 'Mens_Pink_Front.png',	'Red' : 'Mens_Red_Front.png',	'Silver' : 'Mens_Silver_Front.png',	'Soft Cream' : 'Mens_Soft_Cream_Front.png',	'Steel Blue' : 'Mens_Steel_Blue_Front.png',	'Teal' : 'Mens_Teal_Front.png',	'Team Purple' : 'Mens_Team_Purple_Front.png',	'Blue' : 'Mens_True_Royal_Front.png',	'Turqouise' : 'Mens_Turquoise_Front.png',	'White' : 'Mens_White_Front.png',	'Yellow' : 'Mens_Yellow_Front.png'},
        'Color_Back':{'Aqua' : 'Mens_Aqua_Back.png',	'Ash' : 'Mens_Ash_Back.png',	'Asphalt' : 'Mens_Asphalt_Back.png',	'Athletic Heather' : 'Mens_Athletic_Heather_Back.png',	'Autumn' : 'Mens_Autumn_Back.png',	'Berry' : 'Mens_Berry_Back.png',	'Black' : 'Mens_Black_Back.png',	'Brown' : 'Mens_Brown_Back.png',	'Canvas Red' : 'Mens_Canvas_Red_Back.png',	'Cardinal' : 'Mens_Cardinal_Red_Back.png',	'Coral' : 'Mens_Coral_Back.png',	'Dark Grey' : 'Mens_Dark_Grey_Back.png',	'Deep Teal' : 'Mens_Deep_Teal_Back.png',	'Forest' : 'Mens_Forest_Back.png',	'Gold' : 'Mens_Gold_Back.png',	'Kelly' : 'Mens_Kelly_Back.png',	'Leaf' : 'Mens_Leaf_Back.png',	'Light Blue' : 'Mens_Light_Blue_Back.png',	'Maroon' : 'Mens_Maroon_Back.png',	'Mint' : 'Mens_Mint_Back.png',	'Mustard' : 'Mens_Mustard_Back.png',	'Navy' : 'Mens_Navy_Back.png',	'Ocean Blue' : 'Mens_Ocean_Blue_Back.png',	'Olive' : 'Mens_Olive_Back.png',	'Orange' : 'Mens_Orange_Back.png',	'Pink' : 'Mens_Pink_Back.png',	'Red' : 'Mens_Red_Back.png',	'Silver' : 'Mens_Silver_Back.png',	'Soft Cream' : 'Mens_Soft_Cream_Back.png',	'Steel Blue' : 'Mens_Steel_Blue_Back.png',	'Teal' : 'Mens_Teal_Back.png',	'Team Purple' : 'Mens_Team_Purple_Back.png',	'True Royal' : 'Mens_True_Royal_Back.png',	'Turqouise' : 'Mens_Turquoise_Back.png',	'White' : 'Mens_White_Back.png',	'Yellow' : 'Mens_Yellow_Back.png'},
        'shopify_tags':"T-Shirt",
        'sku':{'brand':'A'}},

        "SWEATSHIRT":
            {'type': 'Unisex Hooded Sweatshirt',
          'folder': 'SWEATSHIRT/',
        'size':['Extra Small','Small', 'Medium', 'Large', 'Extra Large'],
        'weight':1360,
        'price':45.00,
        'Front':{'xx':590,'yy':650,'r': 0.5,'sx': 810,'sy':1026,'mask':'hoodie_mask_front.png'},
        'Back':{'xx':601,'yy':700,'r':0.0,'sx': 790,'sy':1000,'mask': 'hoodie_mask_back.png'},
        'Color_Front':{'Black' : 'hoodie_black_front.png',	'Royal Blue' : 'hoodie_blue_front.png',	'Blue Aqua' : 'hoodie_blueaqua_front.png',	'Charcoal' : 'hoodie_charcoal_front.png',	'Navy' : 'hoodie_navy_front.png',	'Red' : 'hoodie_red_front.png',	'Sandstone' : 'hoodie_sandstone_front.png'},
        'Color_Back':{'Black' : 'hoodie_black_back.png',	'Royal Blue' : 'hoodie_blue_back.png',	'Blue Aqua' : 'hoodie_blueaqua_back.png',	'Charcoal' : 'hoodie_charcoal_back.png',	'Navy' : 'hoodie_navy_back.png',	'Red' : 'hoodie_red_back.png',	'Sandstone' : 'hoodie_sandstone_back.png'},
        'tag':{'Red':'','Blue':'','Orange':'','Maroon':''},
        'shopify_tags':"Unisex,2019,Hooded Sweatshirt"},
        "TANK-TOP":
            {'type': 'Unisex Tank Top',
          'folder': 'Tank Top/',
        'size':['Extra Small','Small', 'Medium', 'Large', 'Extra Large'],
        'weight':454,
        'price':25.00,
        'Front':{'xx':545,'yy':595,'r': 0.5,'sx': 810,'sy':1026,'mask':'NONE'},
        'Back':{'xx':550,'yy':239,'r':0.0,'sx': 810,'sy':1026,'mask':'NONE'},
        'tag':{'Red':'tanktop_red.png','Blue':'tanktop_blue.png','Orange':'tanktop_orange.png','Maroon':'tanktop_maroon.png'},
        'Color_Front':{'Ash': 'TankTop_Ash_Front.png','Asphalt' : 'TankTop_Asphalt_Front.png',	'Athletic Heather' : 'TankTop_Athletic_Heather_Front.png',	'Black' : 'TankTop_Black_Front.png',	'Black Heather' : 'TankTop_Black_Heather_Front.png',	'Dark Grey' : 'TankTop_Dark_Grey_Front.png',	'Gold' : 'TankTop_Gold_Front.png',	'Kelly' : 'TankTop_Kelly_Front.png',	'Leaf' : 'TankTop_Leaf_Front.png',	'Navy' : 'TankTop_Navy_Front.png',	'Orange' : 'TankTop_Orange_Front.png',	'Red' : 'TankTop_Red_Front.png',	'Silver' : 'TankTop_Silver_Front.png',	'Teal' : 'TankTop_Teal_Front.png',	'True Royal' : 'TankTop_True_Royal_Front.png',	'White' : 'TankTop_White_Front.png'},
        'Color_Back':{'Ash' : 'TankTop_Ash_Back.png','Asphalt' : 'TankTop_Asphalt_Back.png',	'Athletic Heather' : 'TankTop_Athletic_Heather_Back.png',	'Black' : 'TankTop_Black_Back.png',	'Black Heather' : 'TankTop_Black_Heather_Back.png',	'Dark Grey' : 'TankTop_Dark_Grey_Back.png',	'Gold' : 'TankTop_Gold_Back.png',	'Kelly' : 'TankTop_Kelly_Back.png',	'Leaf' : 'TankTop_Leaf_Back.png',	'Navy' : 'TankTop_Navy_Back.png',	'Orange' : 'TankTop_Orange_Back.png',	'Red' : 'TankTop_Red_Back.png',	'Silver' : 'TankTop_Silver_Back.png',	'Teal' : 'TankTop_Teal_Back.png',	'True Royal' : 'TankTop_True_Royal_Back.png',	'White' : 'TankTop_White_Back.png'},
        'shopify_tags':"Unisex,2019,Tank Top"}}


art_folder = os.path.join('/home/gbenneth/mysite','static',)
templ_folder = os.path.join('/home/gbenneth/mysite','templates','mockup_templates')
root_path = "/home/gbenneth/mysite"

def image_name(name,garm,color,view):
    item_simple = name.replace(' ','-').replace("'","").replace('_','').lower()
    garm_simple = garm.replace(' ','-').replace("'","").replace('_','').lower()
    color_simple = color.replace(' ','-').replace("'","").replace('_','').lower()
    view_simple = view.replace(' ','-').replace("'","").replace('_','').lower()
    return(item_simple + '-' + garm_simple + '-' + color_simple + '-' + view_simple + '.jpg')


def createmock(color,garm,art_file,name,project_folder,view):
    g = garmentdict[garm]
    artwork = Image.open(os.path.join(project_folder, art_file)).resize((g[view]['sx'],g[view]['sy']),Image.ANTIALIAS)
    colorandloc = "Color_" + view
    base_file = g[colorandloc][color]
    base = Image.open(os.path.join(templ_folder, g['folder'],base_file))
    artwork.rotate(g[view]['r'])
    new_img = base.copy()
    mask = g[view]['mask']
    if mask == 'NONE':
        new_img.paste(artwork,(g[view]['xx'],g[view]['yy']),artwork)
    else:
        mask_img = Image.open(os.path.join(templ_folder,g['folder'], mask)).convert("L")
        new_img.paste(artwork,(g[view]['xx'],g[view]['yy']),artwork)
        new_img = Image.composite(base,new_img,mask_img)
        mask_img.close()

    jpg_img = new_img.convert('RGB')
    file_name = image_name(name,garm,color,view)
    new_PTH = os.path.join(project_folder,file_name)
    jpg_img.save(new_PTH)
    artwork.close()
    base.close()
    new_img.close()
    jpg_img.close()
    return file_name


def create_product_data(product_data):
    with open(os.path.join(root_path,'templates','csv_templates','shopify_template.csv'), 'r') as f:
        reader = csv.reader(f)
        shopify_temp = list(reader)
    export = []
    export.append(shopify_temp[0])
    parent_product = shopify_temp[1]
    child_product = shopify_temp[2]
    new_row = []
    y=1
    z=str(y)
    for product in product_data:
        item_name = product_data[z]['itemname']
        product_handle = item_name.replace(" ","-").replace("'","").replace('_','-').lower()
        for product_type in product_data[z]['itemoptions']:
            new_row = parent_product
            new_row[0] = product_handle
            new_row[1] = item_name
            new_row[6] = product_data[z]['tags']
            if len(product_data[z]['itemoptions']) > 1:
                new_row[8] = "Style"
                new_row[9] = product_type
                option_first = 10
            else:
                option_first = 8

            for color in product_data[z]['itemoptions'][product_type]:
                new_row[option_first] = "Color"
                new_row[option_first+1] = color
                new_row[option_first+2] = "Size"
                for size in product_data[z]['itemoptions'][product_type][color]:
                    if size == 'view':
                        continue
                    else:
                        new_row[option_first+3] = size
                        new_row[14] = product_data[z]['itemoptions'][product_type][color][size]["SKU"]
                        new_row[20] = product_data[z]['itemoptions'][product_type][color][size]["Price"]
                        export.append(new_row[:])
                        new_row = child_product[:]
                        new_row[0] = product_handle

        y=y+1
        z=str(y)
    return export



def product_creator(project_num,product_data):
    mockup_file_list = []
    proj_num = str(project_num)
    project_folder = os.path.join(art_folder,proj_num)
    l=1
    for product in product_data:
        m=str(l)
        for product_type in product_data[m]['itemoptions']:
            for color in product_data[m]['itemoptions'][product_type]:
                    mockupfilename = createmock(color,product_type,product_data[m]['filename'],product_data[m]['itemname'],project_folder,product_data[m]['itemoptions'][product_type][color]['view'])
                    mockup_file_list.append(mockupfilename)
        l=l+1
    export = create_product_data(product_data)
    csvfilename = project_num + ".csv"
    csv_path = os.path.join(project_folder,csvfilename)
    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(export)
    file.close()
    return mockup_file_list, csvfilename
