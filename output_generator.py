from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageOps, ImageEnhance, ImageFilter
from io import BytesIO
import discord, requests, requests, random
import datetime, threading, pickle, textwrap, ago, math, time
from resizeimage import resizeimage
font_file = "Data/font2.ttf"
bot_logo = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024"
plays_img = "Data/plays.png"
likes_img = "Data/likes.png"
likes2_img = "Data/likesv2.png"
verif_img = "Data/verification.png"
partn_img = "Data/partner.png"
prem_img = "Data/premium.png"
bot_logo = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024"
star_emote = "⭐ "
gb_emote = "<:GameBot:751968732057698377>"
globe_emote = ":globe_with_meridians:"
game_data_sample = """
`{}`: [{} / {}](https://krunker.io/?game={}) *@ {}*"""

__rarities = {"0": 8185428,
            "1": 1014015,
            "2": 13244869,
            "3": 16761856,
            "4": 13047834,
            "5": 4276545,
            "6": 1}



Main_Color = (227, 126, 255)
month = {1:"JAN",
         2:"FEB",
         3:"MAR",
         4:"APR",
         5:"MAY",
         6:"JUN",
         7:"JUL",
         8:"AUG",
         9:"SEP",
         10:"OCT",
         11:"NOV",
         12:"DEC"}
weapons = ["Knife", "Sniper", "AR",
           "Pistol", "Smg", "Revolver",
           "Shotgun", "Lmg", "Auto",
           "Rl", "Uzi", "Deagle",
           "Alien Blaster", "", "Crossbow", "Famas",
           "Sawed Off", "Auto Pistol"];
skin_types = {
    1:" hat",
    2:" back",
    5:" dye",
    6:" waist",
    7:" face",
    8:" shoe"}

def tint_image(src, color="#FF0000", brightness = 1.45):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    result = ImageOps.colorize(gray, (0, 0, 0, 0), color) 
    result.putalpha(alpha)
    enhancer = ImageEnhance.Brightness(result)
    result = enhancer.enhance(brightness)
    return result

def human_format(num):
    try:
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    except:return "0"
def read_format(num):
    try:return "{:,}".format(num)
    except:return "0"
def dec_format(num):
    try:return "{:,.2f}".format(num)
    except:return "0"
    
def gb_logo(img, client, ngb_logo = None):
    if not ngb_logo:
        ngb_logo = client.gb
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)                
    byte_io = BytesIO()
    byte_io.seek(0)
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io
def change_color(r, g, b, img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if list(pixels[i, j])[-1] == 0:
                pixels[i, j] = (r, g, b, 0)
                
def avg_c(cc, ec, height, c_height):
    ncc = list(cc)
    tbm = c_height/height
    for i in range(3):
        if ncc[i] < ec[i]:ncc[i] = int(ec[i]*tbm)
        else:ncc[i] = ncc[i] - int((int(ncc[i]) - ec[i])*tbm)
    return tuple(ncc)

def gradient(top_c, bottom_c, draw, img):
    for y in range(img.height):
        draw.line((0, y, img.width, y), fill = avg_c(top_c, bottom_c, img.height, y))

def newGrad(xy, top_c = (54, 57, 63), bottom_c = (26, 27, 28)):
    img = Image.new("RGB", (xy[0], xy[1]), (0, 0, 0))
    draw_ = ImageDraw.Draw(img)
    gradient(top_c, bottom_c, draw_, img)
    return img
def fill_tp(r, g, b, img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if list(pixels[i, j])[-1] == 0:
                pixels[i, j] = (r, g, b, 255)

def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue
def draw_non_acsii(x, y, text, font, unic_font, color, mdraw, stroke = 0):
    overall_off = x
    for x, e_letter in enumerate(text):
        if e_letter.isascii():
            mdraw.text((overall_off, y), e_letter, font=font, fill=color)
            overall_off += get_text_size(e_letter, font) + 2
        else:
            mdraw.text((overall_off, y), e_letter, font=unic_font, fill=color)
            overall_off += get_text_size(e_letter, unic_font) + 3
        
    return overall_off-x
def classic_outline(img, x_ = 2, y_ = 9, border = 4, color = (20,22,24), radius= 25, initial_top = 3):
    img = add_corners(img, radius)
    img_b = Image.new('RGB', (img.width + x_, img.height + x_), color)
    img_b = ImageOps.expand(img_b, border=border, fill = color)
    img_b = add_corners(img_b, radius)        
    img_b.paste(img, (initial_top, initial_top), img)
    return img_b

def get_text_size(text, font):
    text_image = Image.new("RGB", (100, 100), (0, 0, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text, font=font, fill=(255, 255, 255))
    pixels = text_image.load()
    x_vals = []
    for x in range(text_image.size[0]):
        for y in range(text_image.size[1]):
            if pixels[x, y] != (0, 0, 0):
                x_vals.append(x)
    try:return max(x_vals) - min(x_vals)
    except:return 1


def make_mods(final_maps, user_name, client, featured_maps_file):
    font_size = 17
    offset = 15
    maps = final_maps
    #maps = [['Caribbean_Escape', 15000, 3], ['Tunnel_Escape', 537, 1], ['Old_Times', 9, 0], ['2d_Jungle',21,-1]] 
    black_color = (255, 255, 255)
    #y = int((len(maps)*(12+(font_size+4)))+(offset))+40
    y = len(maps) * 31
    y += offset + 40 + 5
    #img = newGrad((460,y))
    img = Image.new("RGBA", (460, y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font_size += 10
    with open(featured_maps_file, "rb") as file:
        old_data = pickle.load(file)
    for e_map in maps:
        if e_map[0].lower() in old_data:
            e_map[-1] = 0
        else:e_map[-1] = None
    def filter_votes(votes):
        if not votes:return [13, (100, 100, 100), '', '', votes]
        elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
        elif votes < 0: return [6, (235, 10, 10), '', '', votes]
        elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
    def filter_color(verification):
        if verification == 0:
            return (255, 203, 73)
        return Main_Color
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), user_name+"'s Mods", font2)
    offset = 44
    def e_mod(x, e_map):
        outline_text(draw, 10, 12+((font_size+4)*x)+offset, filter_color(e_map[-1]), (0, 0, 0), e_map[0], font)
        outline_text(draw, 335, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), str(e_map[1]), font)
        x_, color, abbr, abbr2, votes = filter_votes(e_map[2])
        draw.text((410+x_, 12+(((font_size+4))*x)+offset),abbr+str(votes)+abbr2,color,font=font)
    all_threads = []
    for x, e_map in enumerate(maps):
        emthr = threading.Thread(target=e_mod, args = (x, e_map))
        emthr.start()
        all_threads.append(emthr)
    for e_t in all_threads:
        e_t.join()

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((460,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    byte_io = gb_logo(img_b, client)
    return byte_io

def make_online(games_o, user_name, randomize, client, old_data, overall_online):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(games_o) * 31
    y += offset + 40 + 5 + 50
    img = Image.new('RGBA', (590,y), (0, 0, 0, 0))
    #img = newGrad((500, y))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font_size += 10
    def filter_votes(votes):
        if not votes:return [13, (100, 100, 100), '', '', votes]
        elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
        elif votes < 0: return [6, (235, 10, 10), '', '', votes]
        elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
    def filter_color(verification):
        if verification:
            return (255, 203, 73)
        return (227, 126, 255)
    if not randomize:outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), "{}'s Games".format(user_name), font2)
    else:outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), "Top active maps", font2)
    offset = 44
    def e_game(x, mapnm, mapon):
        outline_text(draw, 10, 12+((font_size+4)*x)+offset, filter_color(mapnm.lower() in old_data), (0, 0, 0), mapnm, font)
        outline_text(draw, 240+75, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), str(mapon[1]) + " lobbies", font)
        outline_text(draw, 350+15+83, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), str(mapon[0]) + " online", font)
    all_threads = []
    for x, (mapnm, mapon) in enumerate(games_o.items()):
        emthr = threading.Thread(target=e_game, args = (x, mapnm, mapon))
        emthr.start()
        all_threads.append(emthr)
    for e_t in all_threads:
        e_t.join()


    outline_text(draw, 18, y-45, (220, 220, 220) , (0, 0, 0), "Total", font2)
    outline_text(draw, 310, y-45, (220, 220, 220) , (0, 0, 0), '{:,} online'.format(overall_online), font2)

    ngb_logo = client.gb
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
    
    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=3))
    dark_img.paste(img, (0, 0), img)
    

    gr_img = newGrad((590, y))
    gr_img.paste(dark_img, (0, 0), dark_img)
    gr_img = classic_outline(gr_img)

    byte_io = BytesIO()
    byte_io.seek(0)
    gr_img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im
    
def outline_text(draw, x, y, color_, shadow_color_, text_, font_, thickness = 1):
    draw.text((x, y), text_, font=font_, fill=color_, stroke_fill = shadow_color_, stroke_width = thickness)
    
def get_asset_img(maps, user_name, msg, start = 0, pages_ = 1, pages_main = None, arg_ = "nm", arg_2 = 'siz',arg_2b = True, header = "Assets"):
    maps = sorted(maps, key = lambda x: x[arg_])

    try:
        maps = maps[start:start+30]
    except:
        maps = maps[start:]

    
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = (len(maps) * 31) + offset + 40 + 5
    img = Image.new('RGBA', (460,y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_file, font_size)
    font2 = ImageFont.truetype(font_file, font_size+6)
    fontn = ImageFont.truetype(font_file, font_size-3)
    font_size += 10
    def filter_votes(votes):
        if not votes:return [13, (100, 100, 100), '', '', votes]
        elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
        elif votes < 0: return [6, (235, 10, 10), '', '', votes]
        elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
    def filter_color(verification):
        if verification == 0:return (255, 203, 73)
        return (255, 0, 255)
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), user_name+"'s "+header, font2)
    if pages_main != 1: outline_text(draw, 345, 35, (200, 200, 200), (0, 0, 0), "PG# {} of {}".format(pages_, pages_main), fontn, 2)
    offset = 44
    for x, e_map in enumerate(maps):
        outline_text(draw, 10, 12+((font_size+4)*x)+offset, (227, 126, 255), (0, 0, 0), e_map[arg_], font)
        if arg_2b: outline_text(draw, 335, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), str(e_map[arg_2]) + " kb", font)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((460,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    
    img = classic_outline(img)
    gb_logo = Image.open("Data/logo.png","r")
    __x__, __y__ = img.size
    img.paste(gb_logo, (__x__-33, __y__-33), gb_logo)
    byte_io = BytesIO()
    byte_io.seek(0)
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io

def get_search_img(maps, header, message, m_key = "map_verified"):
    font_size = 17
    offset = 15
            
    black_color = (255, 255, 255)
    y = len(maps) * 31
    y += offset + 40 + 5
            
    img = Image.new('RGBA', (500,y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_file, font_size)
    font2 = ImageFont.truetype(font_file, font_size+6)
    font3 = ImageFont.truetype(font_file, font_size-3)
    font_size += 10
    def filter_color(verification):
        if verification == 0:
            return (255, 203, 73)
        elif verification == 1 and m_key == "map_featured":
            return (255, 203, 73)
        return Main_Color
    #draw.text((10, 10), ,,font=font2)
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), header, font2)
    offset = 44
    for x, e_map in enumerate(maps):
                
        #draw.text((10, 12+((font_size+4)*x)+offset),e_map[0],filter_color(e_map[-1]),font=font)
        outline_text(draw, 228, 12+((font_size+4)*x)+offset + 2, (150, 150, 150) , (0, 0, 0), "by "+e_map['creatorname'], font3)
        outline_text(draw, 10, 12+((font_size+4)*x)+offset, filter_color(e_map[m_key]), (0, 0, 0), e_map['map_name'], font)

        outline_text(draw, 380+40, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), str(e_map['map_votes']), font)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    
    img = newGrad((500,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img = classic_outline(img)
    
    gb_logo = Image.open("Data/logo.png","r")
    __x__, __y__ = img.size
    img.paste(gb_logo, (__x__-33, __y__-33), gb_logo)

            
    byte_io = BytesIO()
    byte_io.seek(0)
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io


async def post_emb_page(main_msg, maps, user_name, msg, start = 0, pages_ = 1, pages_main = None, arg1 = "mna", arg2 = "ctn", arg3 = "vte", sort_key = "mna", reverse_sort = False, d_maps= False):
    maps = sorted(maps, key = lambda x:x[sort_key], reverse = reverse_sort)
    try:
        maps = maps[start:start+10]
    except:
        maps = maps[start:]
    if d_maps:
        raw_embed_entry = "[{}](https://krunker.io/?play={}) --- {}{}\n"
        output_entry = "**Map Name   ---  Likes**\n"
        title_em = user_name + "'s Maps"
    else:
        raw_embed_entry = "[{}](https://krunker.io/?play={}) --- by `{}` --- `{}`\n"
        output_entry = "**Map Name   ---   by Creator   ---   Likes**\n"
        title_em = user_name + "'s Favourite Maps"
        
    for e_map in maps:
        if d_maps:e_map[arg2] = ""
        output_entry += raw_embed_entry.format(e_map[arg1],
            requests.compat.quote_plus(e_map[arg1]),
            e_map[arg2],
            e_map[arg3])
    embed = discord.Embed(colour=discord.Colour(14423783), description = output_entry)
    embed.set_author(name= title_em , icon_url=bot_logo)
    embed.set_footer(text="Page # {} of {}".format(pages_, pages_main))
    if main_msg == None:
        tracked_post = await msg.channel.send(embed = embed)
    else:
        await main_msg.edit(embed = embed)
        tracked_post = main_msg
    return tracked_post

async def post_info_page(main_msg, maps, user_name, msg, start = 0, pages_ = 1, pages_main = None, arg1 = "mna", arg2 = "ctn", arg3 = "vte", sort_key = "mna", reverse_sort = False, d_maps= False, sum_of_kr = 0, sum_of_doll = 0):
    maps = sorted(maps, key = lambda x:x[sort_key], reverse = reverse_sort)
    try:
        maps = maps[start:start+10]
    except:
        maps = maps[start:]
    maximum_width = max([len(e_map[arg1]) for e_map in maps]) + 4
    max_width_kr = max([len(e_map["kr"]) for e_map in maps]) + 3
    raw_embed_entry = "[{}](https://krunker.io/?play={}) {} `{} kr` {} `${}`\n"
    output_entry = "**Map Name   ---   Kr   ---   $$$**\n"
    title_em = user_name + "'s Maps"
        
    for e_map in maps:
        output_entry += raw_embed_entry.format(e_map[arg1],
            requests.compat.quote_plus(e_map[arg1]),
                                               e_map[arg1].ljust(maximum_width, "-")[len(e_map[arg1]):],
                                               e_map["kr"],
                                               e_map["kr"].ljust(max_width_kr, "-")[len(e_map["kr"]):],
                                               e_map["doll"])
    output_entry += "Total {} `{} kr` {} `${}`".format("total".ljust(maximum_width, "-")[len("total"):],
                                                        sum_of_kr,
                                                        sum_of_kr.ljust(max_width_kr, "-")[len(sum_of_kr):],
                                                        sum_of_doll)
    
    embed = discord.Embed(colour=discord.Colour(14423783), description = output_entry)
    embed.set_author(name= title_em , icon_url=bot_logo)
    embed.set_footer(text="Page # {} of {}".format(pages_, pages_main))
    if main_msg == None:
        tracked_post = await msg.channel.send(embed = embed)
    else:
        await main_msg.edit(embed = embed)
        tracked_post = main_msg
    return tracked_post

async def sweep_printer(main_msg, data, map_name, msg, start = 0, pages_ = 1, pages_main = None):
    data = list(data.items())
    try:
        data = data[start:start+10]
    except:
        data = data[start:]
    output = ""
    raw_output = "**{}** `+` {}\n"
    for e_user, e_user_data in data:
        output += raw_output.format(e_user.replace("_", r"\_").replace("*", r"\*"), "{:,}".format(e_user_data[-1]-e_user_data[0]))
    today = datetime.datetime.utcnow()
    last_upd = today - datetime.timedelta(hours = int(today.strftime("%H")), minutes = int(today.strftime("%M")))
    embed = discord.Embed(description=output, title = map_name.upper(), timestamp=last_upd)
    embed.set_footer(text="Page # {}/{}\nLast update".format(pages_, pages_main))
    if main_msg == None:
        tracked_post = await msg.channel.send(embed = embed)
    else:
        await main_msg.edit(embed = embed)
        tracked_post = main_msg
    return tracked_post
    
def make_map_info(data, descip, client, map_thumb_url, user_name, host_data):
    online_ppl = 0
    for e_map in host_data:
        if e_map[-1]["i"].lower() == user_name.lower():
            online_ppl += e_map[2]
    font_size = 18
    y_offs = 21*len(descip)
    black_color = (255, 255, 255)
    #img = Image.new('RGB', (500,247+y_offs), (54, 57, 63))
    img = newGrad((500,247+y_offs))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_file, font_size)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)
    font4 = ImageFont.truetype(font_file, font_size-8)

    font5 = ImageFont.truetype(font_file, font_size-7)

    fontsm = ImageFont.truetype(font_file, font_size-4)
    
    
    #draw.text((20, 20), data["map_name"],Main_Color,font=font)
    def filter_color(verification):
        if verification == 0:
            return (255, 203, 73)
        return Main_Color
    #data['map_updatecounter'] = 16
    #draw.text((20, 20), data["map_name"],Main_Color,font=font)
    outline_text(draw, 20, 20, filter_color(data["map_verified"]), (0, 0, 0), data["map_name"], font)
    mnwidth, mnheight = draw.textsize(data["map_name"], font=font)
    
    draw.text((20, 62), "by",(150, 150, 150),font=fontsm)
    outline_text(draw, 50, 62, (191, 176, 190), (50, 50, 50), data["map_creator"], font2)

    
    draw.text((20, 98), "{:,}".format(data["vt"]),(191, 176, 190),font=fontsm)
    twidth, theight = draw.textsize("{:,}".format(data["vt"]), font=fontsm)
    likes_ = Image.open(likes2_img,"r")
    img.paste(likes_, (20+twidth+5, 97), likes_)
    draw.text((20, 131), "{:,}".format(online_ppl),(191, 176, 190),font=fontsm)
    twidth, theight = draw.textsize("{:,}".format(online_ppl), font=fontsm)
    likes_ = Image.open("Data/online.png", "r")
    img.paste(likes_, (20+twidth+5, 131), likes_)

    draw.text((20, 161), "{:,}".format(data["pl"]),(191, 176, 190),font=fontsm)
    twidth, theight = draw.textsize("{:,}".format(data["pl"]), font=fontsm)
    likes_ = Image.open(plays_img,"r")
    img.paste(likes_, (20+twidth+5, 161), likes_)


    date = data["map_initialdate"][:10].split("-")
    draw.text((20, 190), "Publish Date: {}-{}-{}".format(str(date[2]), month[int(date[1])], date[0]),(130, 130, 130),font=font4)

    date = data["map_date"][:10].split("-")
    draw.text((20, 209), "Update Date:  {}-{}-{}".format(str(date[2]), month[int(date[1])], date[0]),(130, 130, 130),font=font4)
    
    #draw.multiline_text((20, 200), ,,font=font3)
    hoffset = 240
    for line in descip:
        draw.text((20, hoffset), line, font=font4, fill=(150, 150, 150))
        hoffset += font.getsize(line)[1]-7
    version = data['map_updatecounter']/10
    draw.text((mnwidth+25, 26), "v"+str(version),(110, 110, 110),font=font4)
    try:
        response = requests.get(map_thumb_url.format(data["map_id"]))
        thumb = Image.open(BytesIO(response.content)).convert("RGBA")
    except:
        thumb = Image.open("Data/unknown.png").convert("RGBA")
    thumb.thumbnail((200, 200), Image.ANTIALIAS)
    thumb = ImageOps.expand(thumb,border=2,fill=(37,41,44))
    img.paste(thumb, (258, 60), thumb)

    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)


def make_owners(maps, client, name_):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(maps) * 31
    y += offset + 40 + 5
    main_bg = (54, 57, 63)
    img = Image.new('RGBA', (500,y), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = ImageFont.truetype(font_file, font_size-3)
    font_size += 10
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), name_ + " Owners", font2)
    offset = 44
    for x, e_map in enumerate(maps):
        offset_pf = 10
        if e_map['su'] > 0:
            prem = Image.open(prem_img, "r")
            img.paste(prem, (offset_pf, 12+((font_size+4)*x)+offset), prem)
            offset_pf += 21
            
        if bool(e_map['ft']):
            verif = Image.open(verif_img,"r")
            img.paste(verif, (offset_pf, 12+((font_size+4)*x)+offset), verif)
            offset_pf += 23
            
        outline_text(draw, offset_pf, 12+((font_size+4)*x)+offset, Main_Color, (0, 0, 0), e_map['nm'], font)

        outline_text(draw, 380+40, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), "x"+str(e_map['ct']), font)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((500,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)


def make_posts(maps, skins, PyJsHoisted_getPreview_, client, is_giveaway):
    y_reoff = 0
    if maps["typ"] in [2, 3, 5]:
        maps["txt"] += " Play it now!" if maps["typ"] == 2 else " Try it now!"
        if maps["typ"] == 5:
            for e_skin_n, e_skin in skins.items():
                try:
                    if e_skin["i"] == int(maps["lnk"]):
                        our_skin = e_skin
                except:pass
            maps["txt"] = "Just unboxed a "+ our_skin["name"]
            thm_url = str(PyJsHoisted_getPreview_(our_skin))[1:-1]
        else:
            thm_url = "https://user-assets.krunker.io/md{}/thumb.png".format(maps["lnk"]) if maps["typ"] == 3 else "https://user-assets.krunker.io/m{}/thumb.png".format(maps["lnk"])
        try:
            response = requests.get(thm_url)
            thumb = Image.open(BytesIO(response.content)).convert("RGBA")
        except:
            thumb = Image.open("Data/unknown.png").convert("RGBA")
        fill_tp(37,41,44, thumb)
        thumb = resizeimage.resize_thumbnail(thumb, [200, 200])
        thumb = add_corners(thumb, 12)
        y_reoff = thumb.height + 30
    text = textwrap.wrap(maps["txt"], width=50)
    y_offs = 30*len(text)
    y_offs_overall = 50*len(text)
    img = newGrad((720, 180+y_offs_overall+y_reoff))
    draw = ImageDraw.Draw(img)

    icon = Image.open("Data/icon.png")
    img.paste(icon, (20, 20), icon)

    dark_c = (226, 226, 226)
    main_c = (227, 126, 255)

    bimg = Image.new('RGB', (686-10,y_offs_overall+6+y_reoff), (149, 158, 158))
    bimg = add_corners(bimg, 10)
    img.paste(bimg, (25, 95), bimg)

    
    bimg = Image.new('RGB', (680-10,y_offs_overall+y_reoff), (98, 104, 104))
    bimg = add_corners(bimg, 10)
    img.paste(bimg, (28, 98), bimg)
    
    font_size = 18

    
    font = ImageFont.truetype(font_file, font_size)
    fontmega = ImageFont.truetype(font_file, font_size+3)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)
    unicode_font = ImageFont.truetype("Data/unifont.ttf", font_size+3)

    twidth, _ = draw.textsize(maps["pln"], font)
    off_ = 0
    if maps["prm"]:
        verif = Image.open("Data/prem.png","r").convert("RGBA")
        verif.thumbnail((20, 20), Image.ANTIALIAS)
        img.paste(verif, (92 + twidth, 24), verif)
        off_ += 26
    if maps["ftr"]:
        verif = Image.open("Data/verif.png","r").convert("RGBA")
        verif.thumbnail((20, 20), Image.ANTIALIAS)
        img.paste(verif, (92 + twidth + off_, 24), verif)
        off_ += 26
    if maps["cln"]:
        if maps["cln"].isascii():
            draw.text((92 + twidth + off_, 24), "["+maps["cln"]+"]", (98, 104, 104), font)
        else:
            draw_non_acsii(92 + twidth + off_, 24, "["+maps["cln"]+"]", font, unicode_font, (98, 104, 104), draw)

    outline_text(draw, 85, 24, main_c, (25, 25, 25), maps["pln"], font)
    outline_text(draw, 85, 55, (98, 104, 104), (25, 25, 25), read_format(maps["flw"]) + " Followers", font2)

    twidth, _ = draw.textsize(str(maps["vot"]), font)
    
    outline_text(draw, 557-twidth, 142+y_offs_overall+y_reoff, main_c, (25, 25, 25), str(maps["vot"]), font)
    overall_likes = 557+8
    twidth2, _ = draw.textsize("Likes", font)
    overall_likes += twidth2 + 7
    draw.text((557+8, 142+y_offs_overall+y_reoff), "Likes", (98, 104, 104), font)
    bimg = Image.open("Data/heart.png")
    img.paste(bimg, (overall_likes, 142+y_offs_overall+y_reoff), bimg)

    ctwidth, _ = draw.textsize(str(maps["cnt"]), font)
    outline_text(draw, 480-twidth, 142+y_offs_overall+y_reoff, main_c, (25, 25, 25), str(maps["cnt"]), font)
    bimg = Image.open("Data/comment.png")
    img.paste(bimg, (480+ctwidth+7-twidth, 142+y_offs_overall+y_reoff), bimg)

    max_t_y = 0

    for x, e_t in enumerate(text, 0):
        outline_text(draw, 50, 115 + (x*45), main_c, (25, 25, 25), e_t, font)
        max_t_y = 115 + (x*45)

    max_t_y += 50

    if y_reoff:
        img.paste(thumb, (int((img.width/2) -  (thumb.width/2)), max_t_y), thumb)
        

    when = ago.human(datetime.timedelta(seconds = int(maps["tim"]/1000)), precision = 3, abbreviate  = True)
    twidth, _ = draw.textsize(when, font)
    outline_text(draw, 705-twidth, 25, (98, 104, 104), (25, 25, 25), when, font)
    if is_giveaway:
        when = ago.human(datetime.timedelta(seconds = int(maps["exp"]/1000)), precision = 3, abbreviate  = True, past_tense = "{} left")
        twidth, _ = draw.textsize(when, font)
        outline_text(draw, 705-twidth, 60, (98, 104, 104), (25, 25, 25), when, font)
        outline_text(draw, 30, 142+y_offs_overall+y_reoff, (98, 104, 104), (25, 25, 25), "{:,} KR".format(maps["fds"]), font)
    
    img_b = classic_outline(img)

    img_b.paste(img, (2, 2), img)
    return gb_logo(img_b, client)

def make_wars(client, all_regions, write_clan_name, regions_x):
    img = Image.open("Data/map.png")
    black_color = (255, 255, 255)
    draw = ImageDraw.Draw(img)
    font_size = 10
    font = client.font3
    
    unicode_font = ImageFont.truetype("Data/unifont.ttf", font_size+3)
    
    def vldr(text, pixel, font_=font):
        twidth, _ = draw.textsize(text, font=font_)
        return pixel -  int(twidth/2)
    
    for x, e_ri in enumerate(all_regions):
        try:
            _name = "["+e_ri[0]["cn"]+"]"
        except:
            _name = "None"
        if _name.isascii():clan_font = font
        else:clan_font = unicode_font
        try:
            clan_rank =  e_ri[0]['cr']
        except:
            clan_rank = e_ri[0]['cr'] = 100
        write_clan_name(draw, (vldr(_name, regions_x[x][0], clan_font), regions_x[x][1]-5), clan_rank, _name, font, unicode_font)
        #draw.text((vldr(_name, regions_x[x][0], clan_font), regions_x[x][1]-5), _name, black_color, font=clan_font)
    return gb_logo(img, client)
def make_lwars(e_ri, client):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(e_ri) * 31
    y += offset + 40 + 5
    img = Image.new("RGBA", (460, y), (0, 0, 0 ,0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = ImageFont.truetype(font_file, font_size-2)
    unicode_font = ImageFont.truetype("Data/unifont.ttf", 18)
    font_size += 10
    def filter_color2(clan_):
        return (130, 130, 130)
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), "Clanwars", font2)
    offset = 44
    for x, (e_clan, e_map)  in enumerate(e_ri.items()):
        if True:
            m_c = Main_Color
            if e_clan.isascii():
                clan_font = font
            else:
                clan_font = unicode_font
            outline_text(draw, 10, 12+((font_size+4)*x)+offset, m_c, (0, 0, 0), "["+e_clan+"]", clan_font)
            if not e_clan.isascii():
                outline_text(draw, 11, 12+((font_size+4)*x)+offset, m_c, (0, 0, 0), "["+e_clan+"]", clan_font)
                outline_text(draw, 9, 12+((font_size+4)*x)+offset, m_c, (0, 0, 0), "["+e_clan+"]", clan_font)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset+1, m_c, (0, 0, 0), "["+e_clan+"]", clan_font)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset-1, m_c, (0, 0, 0), "["+e_clan+"]", clan_font)
            outline_text(draw, 200, 12+((font_size+4)*x)+offset, (255, 255, 255), (0, 0, 0), "{:,}".format(e_map['kl'])+ " Kills" , font3)
            outline_text(draw, 335, 12+((font_size+4)*x)+offset, (255, 255, 255), (0, 0, 0), "{:,}".format(e_map['pl'])+ " Players" , font3)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((460,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)


def make_leadersw(maps, client, main_pages, current_page):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(maps) * (31 + 2)
    y += offset + 40 + 5
    img = Image.new("RGBA", (550, y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = client.main_font3
    font_size += 12

    heading_color = (179, 179, 179)
    outline_text(draw, 18, 15, (255, 255, 255), (0, 0, 0), "Clanwars Players", font2)
    if main_pages > 1: outline_text(draw, 395, 22, heading_color, (0, 0, 0), "Page # {}/{}".format(current_page, main_pages), font)
    offset = 44
    
        
    for x, e_map in enumerate(maps):
        outline_text(draw, 18, 12+((font_size+4)*x)+offset, Main_Color, (0, 0, 0), e_map["p"], font)
        outline_text(draw, 230, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), '{:,}'.format(e_map["k"]) + " kills", font)
        lives_left = 0 if 100-e_map["d"] < 0 else 100-e_map["d"]
        if lives_left == 0:
            l_c = (255, 210, 210)
        else:l_c = black_color
        outline_text(draw, 390, 12+((font_size+4)*x)+offset, l_c, (0, 0, 0), '{:,}'.format(lives_left) + " lives left", font)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((550,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)


def make_leaders(maps, type_, filter_color, client, user_name, write_clan_name):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(maps) * 31
    y += offset + 40 + 5
    img = Image.new("RGBA", (460, y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = ImageFont.truetype(font_file, font_size-2)
    unicode_font = ImageFont.truetype("Data/unifont.ttf", font_size+3+2)
    font_size += 10
    outline_text(draw, 10, 10, (255, 255, 255), (0, 0, 0), user_name.title()+" Leaderboard", font2)
    offset = 44
    for x, e_map in enumerate(maps):
        if not type_ == "player_clan":
            try:
                m_c = filter_color(e_map['player_featured'])
            except:
                m_c = Main_Color
            outline_text(draw, 10, 12+((font_size+4)*x)+offset, m_c, (0, 0, 0), e_map["player_name"], font)
            try:
                if e_map["player_clan"]:
                    twidth, theight = draw.textsize(e_map["player_name"], font=font)
                    write_clan_name(draw,
                                    (10+twidth+5, 12+((font_size+4)*x)+offset),
                                    e_map['clan_rank'],
                                    '['+str(e_map["player_clan"])+']', font, unicode_font)
                    
                    #draw.text((10+twidth+5, 12+((font_size+4)*x)+offset), '['+str(e_map["player_clan"])+']',filter_color2(e_map["player_clan"]),font=font)
            except:pass
            x_offs = 0
            if type_ == 'player_score':
                value_ = "LVL "+str('{:,}'.format(max(1, math.floor(0.03 * math.sqrt(e_map["player_score"])))))
            elif type_ == 'player_timeplayed':
                value_ = str('{:,}'.format(int((str(float(((int(str(e_map["player_timeplayed"]).split(".")[0])/60)/60)/1000)).split(".")[0])))) + " hrs"
            elif type_ == 'player_eventcount':
                value_ = str(e_map['player_eventcount']) + " / 150"
            elif type_ == 'player_followed':
                value_ = str('{:,}'.format(e_map[type_])) + " followers"
                x_offs = -40
            elif type_ == 'player_eventtime':
                value_ = str(datetime.timedelta(seconds = int(e_map[type_]/1000)))
                x_offs = 10
            elif type(e_map[type_]) is int:
                value_ = str('{:,}'.format(e_map[type_]))
            else:
                value_ = str(e_map[type_])
            outline_text(draw, 330+x_offs, 12+((font_size+4)*x)+offset, black_color, (0, 0, 0), value_, font)
        #draw.text((335, 12+((font_size+4)*x)+offset),str(e_map["siz"]) + " kb",black_color,font=font)
        else:
            if not e_map["clan_name"] in ["DEV", "Lore", "nV", "Oxic", "Verb", "Omen", "ロリ幼女", "VOID", "JBP", "PHIL", "TIMP", "g59", "24/7", "GLXY", "MMOK", "KPOP"]:
                m_c = Main_Color
            else:
                m_c = (255, 203, 73)
            write_clan_name(draw,
                            (10, 12+((font_size+4)*x)+offset),
                            e_map['clan_rank'],
                            "["+e_map["clan_name"]+"]", font, unicode_font, outline_c = (0, 0, 0))
            outline_text(draw, 100, 12+((font_size+4)*x)+offset, (150, 150, 150), (0, 0, 0), "("+str(e_map["clan_membercount"])+")", font)
            outline_text(draw, 174, 12+((font_size+4)*x)+offset, (150, 150, 150), (0, 0, 0), "by " + e_map['creatorname'] , font3)
            outline_text(draw, 370, 12+((font_size+4)*x)+offset, (255, 255, 255), (0, 0, 0), "LVL "+str('{:,}'.format(max(1, math.floor(0.03 * math.sqrt(e_map["clan_score"]))))) , font3)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((460,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)


def make_stats(data, info, client, user_name, old_stats):

    with open("Data/timestamps.bt", "rb") as file:
        stamp_data = pickle.load(file)
    try:
        last_timestamp = stamp_data["stats"][user_name.lower()]
    except:
        last_timestamp = None

                
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    new_offset = 30 + 50
    y = len(info) * 31
    y += offset + 40 + 5 + new_offset
    y -= 18*7
    img = Image.new("RGBA", (730, y), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = ImageFont.truetype(font_file, font_size-2)
    unicode_font = ImageFont.truetype("Data/unifont.ttf", font_size+3+2)
    font_size += 10
    heading_color = (165, 69, 255) #(132, 0, 255)
    outline_text(draw, 17, 17, (255, 255, 255), (0, 0, 0), user_name+"'s Stats", font2)
    outline_text(draw, 17, 86, heading_color, (0, 0, 0), "Name", font2)
    outline_text(draw, 220, 86, heading_color, (0, 0, 0), "Old", font2)
    outline_text(draw, 415, 86, heading_color, (0, 0, 0), "New", font2)
    outline_text(draw, 580, 86, heading_color, (0, 0, 0), "Diff.", font2)
    
    draw.line((15, 60, 730-15, 60), (74, 77, 84), 4)
    draw.line((220-20, 60, 220-20, y-20), (74, 77, 84), 4)
    draw.line((415-20, 60, 415-20, y-20), (74, 77, 84), 4)
    draw.line((580-20, 60, 580-20, y-20), (74, 77, 84), 4)
    offset = 44
    if last_timestamp:
        cached_stamp = ago.human(datetime.timedelta(seconds = int(time.time() - last_timestamp)), precision = 2,
                                   future_tense = "{} ago", abbreviate = True)
    else:
        cached_stamp = "unknown"
    stamp_x = int(draw.textsize(cached_stamp, client.font)[0]/2)
    cached_x = int(draw.textsize("Last Cached", client.font)[0]/2)
    draw.text((565, 12-3), "Last Cached", (159, 159, 159), font=client.font)
    draw.text(((565+cached_x)-stamp_x, 12+22-3),cached_stamp,
                  (159, 159, 159), font = client.font)
        
    
    Non_Color = (150, 150, 150)

    def check_status(olds, news, type_ = ""):
        if news - olds > 0:
            return "+", (15, 220, 15) if type_ not in ["player_deaths", "player_losses"] else (235, 10, 10)
        if news - olds < 0:
            return "", (235, 10, 10)
        return "", Non_Color
    def get_value(val):
        if int(val) == float(val):
            return int(val)
        return val
    separator_offset = 0
    for x, (e_map, e_val) in enumerate(info.items()):
        if "sep" in e_map:
            line_c = (81, 64, 124) #(74, 77, 84)
            y_ = 12+((font_size+4)*x)+offset+new_offset+separator_offset
            draw.line((15, y_, 730-15, y_),
                      line_c, 4)
            separator_offset -= 18
            continue
            
        
        try:
            old_stats[e_val[0]]
        except:
            old_stats[e_val[0]] = 0
        old_Stat = e_val[1].format(get_value(old_stats[e_val[0]]))
        new_Stat = e_val[1].format(get_value(data[e_val[0]]))
        dif_Stat = e_val[1].format(get_value(data[e_val[0]] - old_stats[e_val[0]]))
        if "f" in e_val[1]:
            old_Stat = format(float(old_Stat), '.10g')
            new_Stat = format(float(new_Stat), '.10g')
            dif_Stat = format(float(dif_Stat), '.10g')
        if e_val[0] == "player_accuracy":
            old_Stat += " %"
            new_Stat += " %"
            dif_Stat += " %"
        sign_, color_ = check_status(old_stats[e_val[0]], data[e_val[0]], e_val[0])
        if e_val[0] == "player_timeplayed":
            try:old_Stat = ago.human(datetime.timedelta(seconds = int(old_stats['player_timeplayed']/1000)), past_tense = "{}", future_tense = "{}", abbreviate=True, precision= 3 )
            except:old_Stat = "0"
            old_Stat = old_Stat if old_Stat else "0"

            try:new_Stat = ago.human(datetime.timedelta(seconds = int(data['player_timeplayed']/1000)), past_tense = "{}", future_tense = "{}", abbreviate=True, precision= 3 )
            except:new_Stat = "0"
            new_Stat = new_Stat if new_Stat else "0"
            
            try:dif_Stat = ago.human(datetime.timedelta(seconds = int((data[e_val[0]] - old_stats[e_val[0]])/1000)), past_tense = "{}", future_tense = "{}", abbreviate=True, precision= 3 )
            except:dif_Stat = "0"
            dif_Stat = dif_Stat if dif_Stat else "0"
            
        outline_text(draw, 20, 12+((font_size+4)*x)+offset+new_offset+separator_offset, Main_Color, (0, 0, 0), e_map, font)
        outline_text(draw, 220, 12+((font_size+4)*x)+offset+new_offset+separator_offset, (255, 255, 255), (0, 0, 0), old_Stat, font)
        outline_text(draw, 415, 12+((font_size+4)*x)+offset+new_offset+separator_offset, (255, 255, 255), (0, 0, 0), new_Stat, font)
        outline_text(draw, 580, 12+((font_size+4)*x)+offset+new_offset+separator_offset, color_, (0, 0, 0), sign_+ dif_Stat, font)

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((730,y))
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    return gb_logo(img_b, client)

def make_class(x, e_class, client):
    def vldr(text, pixel, font):
        twidth, _ = draw.textsize(text, font=font)
        return pixel -  int(twidth/2)
    img = Image.open("Data/class.png")
    draw = ImageDraw.Draw(img)
    response = requests.get("https://assets.krunker.io/textures/classes/icon_{}.png?".format(x))
    thumb = Image.open(BytesIO(response.content)).convert("RGBA").resize((150, 150), resample=Image.BOX)
    def change_color(r, g, b, img):
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if list(pixels[i, j])[-1] == 0:
                     pixels[i, j] = (r, g, b, 0)
                     
    change_color(98, 104, 104, thumb)
    thumb = add_corners(thumb, 10)
    
    bimg = Image.new('RGB', (154,154), (98, 104, 104))
    bimg = add_corners(bimg, 10)

    img.paste(bimg, (48, 58+30), bimg)
    img.paste(thumb, (50, 60+30), thumb)
    font_size = 18

    
    font = ImageFont.truetype(font_file, font_size)
    fontmega = ImageFont.truetype(font_file, font_size+3)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)
    bimg = Image.new('RGB', (220,242), (98, 104, 104))
    bimg = add_corners(bimg, 14)
    img.paste(bimg, (13, 250), bimg)
    dark_c = (226, 226, 226)
    main_c = (227, 126, 255)

    outline_text(draw, vldr(e_class["name"], img.width/2, fontmega), 15, main_c, (0, 0, 0), e_class["name"], fontmega)
    outline_text(draw, vldr(e_class["wp"], img.width/2, font2), 47, dark_c, (0, 0, 0), e_class["wp"], font2)
    outline_text(draw, 30, 230+30, dark_c, (0, 0, 0), "Health:", font)
    outline_text(draw, 130, 230+30, main_c, (0, 0, 0), str(e_class["health"]), font)

    for x in range(e_class["segs"]):
        bimg = Image.new('RGB', (20, 26), (114, 170, 62))
        bimg = add_corners(bimg, 5)
        img.paste(bimg, (30 + (x * 30), 260+30), bimg)
        
        bimg = Image.new('RGB', (20, 20), (158, 235, 86))
        bimg = add_corners(bimg, 5)
        img.paste(bimg, (30 + (x * 30), 260+30), bimg)

    outline_text(draw, 30, 325, dark_c, (0, 0, 0), "Speed:", font)
    outline_text(draw, 130, 325, main_c, (0, 0, 0), str(e_class["speed"]), font)

    outline_text(draw, 30, 360, dark_c, (0, 0, 0), "Secondary:", font)
    outline_text(draw, 165, 360, main_c, (0, 0, 0), "Yes" if "secondary" in e_class.keys() else "No", font2)

    outline_text(draw, 30, 395, dark_c, (0, 0, 0), "Wall Jump:", font)
    outline_text(draw, 165, 395, main_c, (0, 0, 0), "Yes" if "wallJ" in e_class.keys() else "No", font2)

    outline_text(draw, 30, 390+35+5, dark_c, (0, 0, 0), "Colors:", font)
    def darken(rgb):
        rgb[0] -= 20
        rgb[1] -= 20
        rgb[2] -= 20
        for x, e_v in enumerate(rgb):
            if e_v < 0:rgb[x] = 0
        return rgb
    for x, e_c in enumerate(e_class["colors"]):
        e_c = getRGBfromI(e_c)
        bimg = Image.new('RGB', (20, 26), tuple(darken(list(e_c))))
        bimg = add_corners(bimg, 5)
        img.paste(bimg, (30 + (x * 30), 390+35+35), bimg)
        
        bimg = Image.new('RGB', (20, 20), e_c)
        bimg = add_corners(bimg, 5)
        img.paste(bimg, (30 + (x * 30), 390+35+35), bimg)
        
    img_b = classic_outline(img)

    return gb_logo(img_b, client)

def xp_count(val):
    return str(max(1, math.floor(0.03 * math.sqrt(val))))
def change_color_(r, g, b, img):
    if not sum((r, g, b)):
        return ImageEnhance.Brightness(img).enhance(0)
    else:
        pixels = img.load() # create the pixel map

        for i in range(img.size[0]): # for every pixel:
            for j in range(img.size[1]):
                pixels[i, j] = (r, g, b, list(pixels[i, j])[-1])
                    
def make_cstats(maps, total_maps, get_corr_ind, client, data, stats, get_level_int_c, sclasses_names):
    def vldr(text, pixel, font):
        twidth, _ = draw.textsize(text, font=font)
        return pixel -  int(twidth/2)
    #img = Image.open("Data/cstat.png")
    img = newGrad((709+235-8,(335-40-30-20)*4))
    imgshd = Image.new("RGBA", (709+235-8,(335-40-30-20)*4), (0, 0, 0 ,0))
    imgshd2 = Image.new("RGBA", (709+235-8,(335-40-30-20)*4), (0, 0, 0 ,0))
    imgshd3 = Image.new("RGBA", (709+235-8,(335-40-30-20)*4), (0, 0, 0 ,0))
    draw = ImageDraw.Draw(imgshd)
    font_size = 18


    font = ImageFont.truetype(font_file, font_size)
    fontmega = ImageFont.truetype(font_file, font_size+3)
    fontomega = ImageFont.truetype(font_file, font_size+12)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)
    #maps.insert(0, [total_maps[0]])
    #del ma[
    box_c = (70, 50, 84)#(64, 53, 72) #(70, 75, 75) #(98, 104, 104)
    bg_c = (70, 75, 75)
    bimg = Image.new('RGB', ((230*3)-15,237-20), box_c)
    bimg = add_corners(bimg, 10)
    imgshd2.paste(bimg, (13, 13), bimg)
    try:
        if not (data['player_premium'] > 0):
            raise TimeoutError()
        response = requests.get("https://user-assets.krunker.io/p{}/profile.png".format(data["player_id"]))
        thumb = Image.open(BytesIO(response.content)).convert("RGBA")
        profile_icon = thumb.resize((207-4,207-4)).convert("RGBA")
        new_pficon = Image.new("RGBA", (207-4, 207-4), (0, 0, 0, 0))
        new_pficon.paste(profile_icon, (0, 0), client.icon_mask2)
        profile_icon = new_pficon
            
    except:
        try:
            class_n = stats["c"]
        except:
            class_n = 0
        profile_icon = client.icons[class_n]
        profile_icon = profile_icon.resize((207-4,207-4)).convert("RGBA")
        new_pficon = Image.new("RGBA", (207-4, 207-4), (0, 0, 0, 0))
        new_pficon.paste(profile_icon, (0, 0), client.icon_mask2)
        profile_icon = new_pficon
    imgshd3.paste(profile_icon, (20, 20), profile_icon)
    outline_text(draw, 250, 30, Main_Color, (0, 0, 0), data['player_name'], fontomega)
    outline_text(draw, 250, 80, (226, 226, 226), (0, 0, 0), "[{}]".format(data['player_clan']), fontmega)
    outline_text(draw, 250, 120, (226, 226, 226), (0, 0, 0), "LVL "+xp_count(data['player_score']), fontomega)
    score = data['player_score']
    level = max(1, math.floor(0.03 * math.sqrt(data["player_score"])))
    tmpRank = 0.03 * math.sqrt(score)
    level = math.floor(tmpRank)
    levelPerc = round((tmpRank - level) * 100) # level progress in %
    level = max(1, level) # actual player level

    offset = pow(level / 0.03, 2) if 1 < level else 0
    levelProg = read_format(math.floor(score - offset)) + ' / ' + read_format(math.floor(pow((level + 1) / 0.03, 2) - offset))
    levelProgVal = math.floor(score - offset)/(math.floor(pow((level + 1) / 0.03, 2) - offset))
    loadn = client.defloadn.copy()
    x, y = loadn.size
    loadn = loadn.resize((400, y))
    loadn_mask = loadn.convert("L")
    loadn2 = loadn.crop((0, 0, int(levelProgVal*400), y))
    outline_text(draw, 250, 165, (226, 226, 226), (0, 0, 0), levelProg, font)
    change_color_(50, 10, 50, loadn)
    loadn.putalpha(10)
    imgshd2.paste(loadn, (250, 200), loadn_mask)
    imgshd3.paste(loadn2, (250, 200), loadn2)
        

    for rowx, each_row in enumerate(maps):
        for x, e_class in enumerate(each_row):
            if not sum([rowx,x]):
                x = 3
            num_x = x * 230
            bimg = Image.new('RGB', (220, 275+23+10-40-30-20), box_c)
            bimg = add_corners(bimg, 14)
            
            imgshd2.paste(bimg, (13+num_x, 13+((335-40-30-20)*rowx)), bimg)
            
            #response = requests.get("https://assets.krunker.io/textures/classes/icon_{}.png?".format(get_corr_ind(total_maps.index(e_class))))
            #thumb = Image.open(BytesIO(response.content)).convert("RGBA").resize((150, 150), resample=Image.BOX)
            thumb = client.icons[get_corr_ind(sclasses_names.index(e_class[0].lower()))].copy().resize((80, 80), resample=Image.BOX)
                         
            #change_color(78, 81, 81, thumb)
            #thumb = add_corners(thumb, 10)
        
            bimg = Image.new('RGB', (88,88), bg_c)
            bimg = add_corners(bimg, 10)

            #imgshd3.paste(bimg, (50+21+12+num_x-4, 18+15+60-4+((335-40-30-20)*rowx)), bimg)
            
            imgshd3.paste(thumb, (50+21+12+num_x, 18+15+60+((335-40-30-20)*rowx)), thumb)
            

            dark_c = (226, 226, 226)
            main_c = (227, 126, 255)

            outline_text(draw, vldr(e_class[0], 125 + num_x, fontmega), 22+((335-40-30-20)*rowx), main_c, (0, 0, 0), e_class[0], fontmega)
            outline_text(draw, vldr(e_class[1], 125 + num_x , font2), 59+((335-40-30-20)*rowx), dark_c, (0, 0, 0), e_class[1], font2)

            twidth, _ = draw.textsize("LVL "+ str(e_class[2]), font=fontmega)
            outline_text(draw, (206+num_x)-twidth-3, 260+((335-40-30-20)*rowx)-40-4-30-20, dark_c, (0, 0, 0), "LVL "+ str(e_class[2]), fontmega)
            
            
            #206, 260
            bimg = Image.new('RGB', (200, 25), (51, 52, 56))
            bimg = add_corners(bimg, 10)
            
            imgshd3.paste(bimg, (23+num_x, 278+5+((335-40-30-20)*rowx)-40-30-20), bimg)

            bimg = Image.new('RGB', (190, 20), (82, 88, 88))
            bimg = bimg.crop((0, 0, int(eval(e_class[3])*190), 20))
            bimg = add_corners(bimg, 10)
            
            imgshd3.paste(bimg, (23+num_x+5, 281+5+((335-40-30-20)*rowx)-40-30-20), bimg)
            #draw.text((vldr(e_class[3], 125 + num_x, font3), 281+5+3+((335-40)*rowx)-40),dark_c, e_class[3], font=font3, fill=(255, 255, 255))
            outline_text(draw, vldr(e_class[4], 125 + num_x, font3), 281+5+3+((335-40-30-20)*rowx)-40-30-20, dark_c, (0, 0, 0), e_class[4], font2)
            #outline_text(draw, vldr(e_class[3], 125 + num_x, font3), 281+5, dark_c, (0, 0, 0), e_class[3], font3)


            #outline_text(draw, 30, 360, dark_c, (0, 0, 0), "Secondary:", font)

    
    dark_img = ImageEnhance.Brightness(imgshd2).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(imgshd2, (0, 0), imgshd2)
    img.paste(dark_img, (0, 0), dark_img)

    dark_img = ImageEnhance.Brightness(imgshd3).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(imgshd3, (0, 0), imgshd3)
    img.paste(dark_img, (0, 0), dark_img)
    
    dark_img = ImageEnhance.Brightness(imgshd).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2.5))
    dark_img.paste(imgshd, (0, 0), imgshd)
    img.paste(dark_img, (0, 0), dark_img)
    
    img_b = classic_outline(img)
    

    return gb_logo(img_b, client)


def generate_tag(text, color, tag_img, is_color = 1):
    if is_color:
        tag_img = tint_image(tag_img, color, 2.2)
    else:
        tag_img = tag_img.copy()
    tag_img.paste(text, (0, 0), text)
    return tag_img
    
def make_skin(skin_url, client, skin_data_all, skin_color):
    def vldr(text, pixel, font):
        twidth, _ = draw.textsize(text, font=font)
        return pixel -  int(twidth/2)
    
    img = Image.new("RGBA", (650, 405), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    

    font_size = 18

    
    font = ImageFont.truetype(font_file, font_size)
    fontmega = ImageFont.truetype(font_file, font_size+3)
    fontomega = ImageFont.truetype(font_file, font_size+6)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)

    response = requests.get(skin_url)
    thumb = Image.open(BytesIO(response.content)).convert("RGBA")
    #thumb2 = thumb.filter(ImageFilter.GaussianBlur(radius=3))
    #thumb2.paste(thumb, (0, 0), thumb)
    #thumb = thumb2
    #thumb2 = thumb.filter(ImageFilter.SMOOTH_MORE)
    #thumb = thumb.resize((thumb.width-4, thumb.height-4))
    #thumb2.paste(thumb, (2, 2), thumb)
    #thumb = thumb2

    img.paste(thumb, (int(img.width/2)-int(thumb.width/2), (int(img.height/2)-int(thumb.height/2))+20), thumb)

    twidth, _ = draw.textsize("{:,} KR".format(skin_data_all["avgPrice"]), font=font)
    outline_text(draw, 630-twidth, img.height-65, (233, 228, 0), (0, 0, 0), "{:,} KR".format(skin_data_all["avgPrice"]), font)
    img.paste(client.kr, (630-twidth-30, img.height-65), client.kr)
    try:
        
        twidth, _ = draw.textsize(skin_data_all["limT"], font=font)
        outline_text(draw, 630-twidth, img.height-100, (150, 150, 150), (0, 0, 0), skin_data_all["limT"], font)
    except:pass
    try:
        skin_data_all["creator"]
    except:
        skin_data_all["creator"] = "Krunker.io"
        
    twidth, _ = draw.textsize("By " + skin_data_all["creator"], font=font)
    outline_text(draw, (int(img.width/2)-int(twidth/2)), img.height-40, (150, 150, 150), (0, 0, 0), "By "+skin_data_all["creator"], font)

    #try:
        #twidth, _ = draw.textsize(skin_data_all["limT"], font=font)
        #outline_text(draw, 630-twidth, img.height-80, (150, 150, 150), (0, 0, 0), skin_data_all["limT"], font)
    #except:pass
    total_tags = 0
    tag_image = client.tag_background
    is_color = sum(skin_color) > 2
    if not is_color:
        tag_image = client.tag_rainbow
    
    try:
        this_season = 1
        try:this_season = skin_data_all["seas"]
        except:pass
        this_tag = generate_tag(client.seasons[this_season], skin_color, tag_image, is_color)
        img.paste(this_tag, (30, img.height-60- (40*total_tags)), this_tag)
        total_tags += 1
    except:
        pass
    '''try:
        skin_data_all["glow"]
        this_tag = generate_tag(client.glowing, skin_color, tag_image, is_color)
        img.paste(this_tag, (30, img.height-60 - (40*total_tags)), this_tag)
        total_tags += 1
    except:pass'''
    try:
        skin_data_all["frames"]
        this_tag = generate_tag(client.animated, skin_color, tag_image, is_color)
        img.paste(this_tag, (30, img.height-60 - (40*total_tags)), this_tag)
        total_tags += 1
    except:pass
    try:
        skin_data_all["limited"]
        this_tag = generate_tag(client.limited, skin_color, tag_image, is_color)
        img.paste(this_tag, (30, img.height-60 - (40*total_tags)), this_tag)
        total_tags += 1
    except:pass 
    
    
                  
    #bimg = Image.new('RGB', (220,242), (98, 104, 104))
    #bimg = add_corners(bimg, 14)
    #img.paste(bimg, (13, 250), bimg)
    dark_c = (226, 226, 226)
    main_c = (227, 126, 255)

    try:
        skin_type = skin_data_all["keyW"]
    except:
        try:
            skin_type = weapons[skin_data_all["weapon"]]
        except:
            try:
                skin_type = skin_types[skin_data_all["type"]].strip().title()
            except:
                skin_type = ""
        

    outline_text(draw, vldr(skin_data_all["name"], img.width/2, fontomega), 15, skin_color if is_color else (255, 255, 255), (0, 0, 0), skin_data_all["name"], fontomega)
    if skin_type:
        outline_text(draw, vldr(skin_type, img.width/2, font), 58, (150, 150, 150), (0, 0, 0), skin_type, font)

    

    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=4))
    dark_img.paste(img, (0, 0), img)
    img = newGrad((650, 405))
    img.paste(dark_img, (0, 0), dark_img)
    ngb_logo = client.gb
    if sum(skin_color) > 2:
        ngb_logo = tint_image(ngb_logo, skin_color)
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
    
    img_b = classic_outline(img, color = skin_color, border = 4, x_ = 3, y_ = 12, initial_top = 5)
    if not is_color:
        img_b.paste(client.skin_rainbow, (0, 0), client.skin_mask)
    img_b = classic_outline(img_b, border = 4, x_ = 3, y_ = 12, initial_top = 5)
    byte_io = BytesIO()
    byte_io.seek(0)
    img_b.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io


    #return gb_logo(img_b, client, ngb_logo)

def generate_tag_mini(text, color, tag_img, is_color = 1):
    if is_color:
        tag_img = tint_image(tag_img, color, 2.2)
    else:
        tag_img = tag_img.copy()
    tag_img = tag_img.resize((63, 23))
    text = text.resize((63, 23))
    tag_img.paste(text, (0, 0), text)
    return tag_img
def make_inv(skins_data, client, PyJsHoisted_getPreview_, start):
    def get_skin_name(main_index):
        return {each_skin["i"]:each_name for each_name, each_skin in client.skins.items()}[main_index]
    def get_rarity(x):
        try:return client.skins[get_skin_name(x["i"])]["rarity"]
        except:return 0
    skins_data = sorted(skins_data, key = get_rarity, reverse = True)
    try:
        skins_data = skins_data[start:start+8]
    except:
        skins_data = skins_data[start:]
    output_stats = []
    sub_list = []
    for ind, e_ind in enumerate(skins_data):
        sub_list.append(e_ind)
        if len(sub_list) == 4 or ind == len(skins_data)-1:
            output_stats.append(sub_list)
            sub_list = []
    main_x = 322*4
    main_y = 430*len(output_stats)
    main_img = Image.new("RGBA", (main_x, main_y), (0, 0, 0, 0))

    

    font_size = 18

    
    font = ImageFont.truetype(font_file, font_size)
    fontmega = ImageFont.truetype(font_file, font_size+3)
    fontomega = ImageFont.truetype(font_file, font_size+6)
    font2 = ImageFont.truetype(font_file, font_size-3)
    font3 = ImageFont.truetype(font_file, font_size-5)
    def vldr(text, pixel, font):
        twidth, _ = draw.textsize(text, font=font)
        return pixel -  int(twidth/2)
    all_images = []
    for row_index, each_row in enumerate(output_stats):
        for col_index, each_skin in enumerate(each_row):
            img = Image.new("RGBA", (300, 405), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            user_name = get_skin_name(each_skin["i"])
            skin_data_all = client.skins[user_name.lower()]
            skin_url = str(PyJsHoisted_getPreview_(client.skins[user_name.lower()]))[1:-1]
            try:
                color = __rarities[str(client.skins[user_name.lower()]["rarity"])]
            except:
                color = 1

            skin_color = discord.Colour(color).to_rgb()
            
            
            

            response = requests.get(skin_url)
            thumb = Image.open(BytesIO(response.content)).convert("RGBA")
            thumb = thumb.resize((thumb.width-8, thumb.height-8))
            #thumb2 = thumb.filter(ImageFilter.GaussianBlur(radius=3))
            #thumb2.paste(thumb, (0, 0), thumb)
            #thumb = thumb2
            #thumb2 = thumb.filter(ImageFilter.SMOOTH_MORE)
            #thumb = thumb.resize((thumb.width-4, thumb.height-4))
            #thumb2.paste(thumb, (2, 2), thumb)
            #thumb = thumb2

            img.paste(thumb, (int(img.width/2)-int(thumb.width/2), (int(img.height/2)-int(thumb.height/2))+20), thumb)

            twidth, _ = draw.textsize("{:,} KR".format(skin_data_all["avgPrice"]), font=font3)
            #outline_text(draw, img.width-twidth-5, img.height-65, (150, 150, 150), (0, 0, 0), "{:,} KR".format(skin_data_all["avgPrice"]), font3)

            try:
                skin_data_all["creator"]
            except:
                skin_data_all["creator"] = "Krunker.io"
                
            twidth, _ = draw.textsize("By " + skin_data_all["creator"], font=font)
            outline_text(draw, (int(img.width/2)-int(twidth/2)), img.height-40, (150, 150, 150), (0, 0, 0), "By "+skin_data_all["creator"], font)

            #try:
                #twidth, _ = draw.textsize(skin_data_all["limT"], font=font)
                #outline_text(draw, 630-twidth, img.height-80, (150, 150, 150), (0, 0, 0), skin_data_all["limT"], font)
            #except:pass
            total_tags = 0
            tag_image = client.tag_background
            is_color = sum(skin_color) > 2
            if not is_color:
                tag_image = client.tag_rainbow
            
            try:
                this_season = 1
                try:this_season = skin_data_all["seas"]
                except:pass
                this_tag = generate_tag_mini(client.seasons[this_season], skin_color, tag_image, is_color)
                img.paste(this_tag, (10, img.height-70- (26*total_tags)), this_tag)
                total_tags += 1
            except:
                pass
            '''try:
                skin_data_all["glow"]
                this_tag = generate_tag(client.glowing, skin_color, tag_image, is_color)
                img.paste(this_tag, (30, img.height-60 - (40*total_tags)), this_tag)
                total_tags += 1
            except:pass'''
            try:
                skin_data_all["frames"]
                this_tag = generate_tag_mini(client.animated, skin_color, tag_image, is_color)
                img.paste(this_tag, (10, img.height-70 - (26*total_tags)), this_tag)
                total_tags += 1
            except:pass
            try:
                skin_data_all["limited"]
                this_tag = generate_tag_mini(client.limited, skin_color, tag_image, is_color)
                img.paste(this_tag, (10, img.height-70 - (26*total_tags)), this_tag)
                total_tags += 1
            except:pass 
            
            
                          
            #bimg = Image.new('RGB', (220,242), (98, 104, 104))
            #bimg = add_corners(bimg, 14)
            #img.paste(bimg, (13, 250), bimg)
            dark_c = (226, 226, 226)
            main_c = (227, 126, 255)

            try:
                skin_type = skin_data_all["keyW"]
            except:
                try:
                    skin_type = weapons[skin_data_all["weapon"]]
                except:
                    try:
                        skin_type = skin_types[skin_data_all["type"]].strip().title()
                    except:
                        skin_type = ""
                

            outline_text(draw, vldr(skin_data_all["name"], img.width/2, fontomega), 15, skin_color if is_color else (255, 255, 255), (0, 0, 0), skin_data_all["name"], fontomega)
            if skin_type:
                outline_text(draw, vldr(skin_type, img.width/2, font), 55, (150, 150, 150), (0, 0, 0), skin_type, font)

            dark_img = ImageEnhance.Brightness(img).enhance(0)
            dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=4))
            dark_img.paste(img, (0, 0), img)
            img = newGrad((dark_img.width, dark_img.height))
            img.paste(dark_img, (0, 0), dark_img)
            img = classic_outline(img, color = skin_color, border = 4, x_ = 3, y_ = 12, initial_top = 5)
            if not is_color:
                img.paste(client.inv_rainbow, (0, 0), client.inv_mask)
            all_images.append([col_index, row_index, img])

    for each_image in all_images:
        main_img.paste(each_image[2], (10 + ( 320 * each_image[0]), 10 + ( 425 * each_image[1])), each_image[2].convert("RGBA"))

    dark_img = ImageEnhance.Brightness(main_img).enhance(0)
    dark_img2 = dark_img.filter(ImageFilter.GaussianBlur(radius=2))
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=7))
    dark_img.paste(dark_img2, (0, 0), dark_img2)
    dark_img.paste(main_img, (0, 0), main_img)
    img = newGrad((main_x, main_y))
    img.paste(dark_img, (0, 0), dark_img)
    ngb_logo = client.gb
    if sum(skin_color) > 2:
        ngb_logo = tint_image(ngb_logo, skin_color)
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
    img_b = classic_outline(img, border = 4, x_ = 3, y_ = 12, initial_top = 5)
    byte_io = BytesIO()
    byte_io.seek(0)
    img_b.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io


def get_lobbies_stuff(msg, client, host_data):
    inp = msg.content.lower()
    no_unique = False
    no_ppl_res = False
    max_players = None
    vac_seats = None
    total_online = 0
    max_capacity = 0
    total_lobies = 0
    filter_kr = 0
    pubs = False
    modes = ""
    g_args = inp.split(" -", 1)
    if len(g_args) == 2:
        m_args = g_args[1]
        total_args = m_args.split("-")
        for e_arg in total_args:
            e_arg = e_arg.strip()
            if e_arg == "u":
                no_unique = True
            if e_arg == "p":
                no_ppl_res = True
            if e_arg == "pub":
                pubs = True
            if e_arg == "kr":
                filter_kr = True
            if e_arg.startswith("mp"):
                try:
                    max_players = int(e_arg.replace("mp", "").replace("", ""))
                except:pass
            if e_arg.startswith("vs"):
                try:
                    vac_seats = int(e_arg.replace("vs", "").replace("", ""))
                except:pass
            if e_arg.startswith("m"):
                try:
                    modes = e_arg[1:].split(" ")
                except:pass
    
    randomize = bool(g_args[0] == "g.find")
    o_maps = []
    filters_k = ['zombie', 'wall', 'aim_room',
                 'new krunker map','digger', 'clashroyale',
                 'sniper', 'tower', 'trade', 'infect',
                 '6.4', 'minecraft', 'parkour+', 'bouncyhop',
                 'ikea', "defence", "defense", "parkour",
                 "dust", "run", "biomes", "escape",
                 "zomb", "war", "portal", "prop",
                 "fallguys", "inf", "hangout_night",
                 "says", "yard", "+", "cracked", "walmart",
                 "TRICKSHOT_ONLY", "Hide_And_Seek", "fortnite", "Z☢️mbie_Invasion", "pubg", "race_Mariokart",
                 "CORONAVIRUS"]
    regions = {
        "NY" : "New York",
        "SYD": "Sydney",
        "FRA": "Frankfurt",
        "MIA": "Miami",
        "SV" : "Silicon Valley",
        "DAL": "Dallas",
        "BLR": "India",
        "SIN": "Singapore",
        "TOK": "Tokyo",
        "BHN": "Middle East",
        "BRZ": "Brazil",
        "AFR": "South Africa",
        "SEO": "South Korea",
        }
    
    if randomize:
        for e_map in host_data:
            map_name = e_map[-1]["i"]
            if not pubs:
                if map_name.lower() in client.official_maps:continue
            co_ = 0
            try:prom = star_emote if e_map[-1]["pr"] else ""
            except:prom = ""
            total_online += e_map[2]
            max_capacity += e_map[3]
            total_lobies += 1
            if not no_unique:
                for e_filt_k in filters_k:
                    if e_filt_k.lower() in map_name.lower():
                        co_ = 1
                        break
                if co_: continue
            if filter_kr:
                try:
                    e_map[-1]["kr"]
                except:continue
            max_vac = True if e_map[3] > 11 else e_map[3] - e_map[2] < 8
            mdata = [e_map[0], e_map[-1]["i"], e_map[2], e_map[3], e_map[-1]["i"], e_map[0].split(":", 1)[0], prom]
            if not max_players:
                if vac_seats == None:
                    if e_map[2] >= 5 and (e_map[3] - e_map[2] >= 1) or no_ppl_res:
                        o_maps.append(mdata)
                elif (e_map[3] - e_map[2] >= vac_seats) and (e_map[2] >= 1):
                    o_maps.append(mdata)
            else:
                if vac_seats == None:vac_seats = 1
                if e_map[3] == max_players and (e_map[3] - e_map[2] >= vac_seats):
                    o_maps.append(mdata)
                
    else:
        map_name = g_args[0][7:]
        for e_map in host_data:
            if not pubs:
                if e_map[-1]["i"].lower() in client.official_maps:
                    continue
            total_online += e_map[2]
            max_capacity += e_map[3]
            total_lobies += 1
            try:prom = star_emote if e_map[-1]["pr"] else ""
            except:prom = ""
            if filter_kr:
                try:
                    e_map[-1]["kr"]
                except:continue
            if map_name.lower() in e_map[-1]["i"].lower():
                o_maps.append([e_map[0], e_map[-1]["i"], e_map[2], e_map[3], prom+e_map[-1]["i"], e_map[0].split(":", 1)[0]])
    if not len(o_maps):
        return None, None
    random.shuffle(o_maps)
    try:
        total_found = len(o_maps)
        o_maps = o_maps[:10]
    except:pass
    longest_name = max(o_maps, key=lambda x: len(x[4]))[4]
    o_maps = sorted(o_maps, key = lambda x: x[2])
    emb_desc = ""
    for e_map in o_maps:
        emb_desc += game_data_sample.format(e_map[4].ljust(len(longest_name)+1),
                                            e_map[2], e_map[3], e_map[0], regions[e_map[5]])
    prom_desc = ""
    for e_game in client.promoted:
        found = 0
        for e_map in host_data:
            if ("https://krunker.io/?game="+e_map[0]).lower() == e_game.lower():
                found = 1
                try:prom = star_emote if e_map[-1]["pr"] else ""
                except:prom = ""
                o_map = [e_map[0], e_map[-1]["i"], e_map[2], e_map[3], e_map[-1]["i"], e_map[0].split(":", 1)[0], prom]
                prom_desc += game_data_sample.format(o_map[4],
                                            o_map[2], o_map[3], o_map[0], regions[o_map[5]])
        if not found:
            try:client.promoted.remove(e_game)
            except:pass
    if prom_desc:
        prom_desc = gb_emote+" **Sponsored Games:**" + prom_desc + "\n\n"

    emb_desc = globe_emote+" **Games found [{}+]:**".format(len(o_maps)) + "\n" + emb_desc
    embed=discord.Embed(colour=discord.Colour(14423783 if not prom_desc else 4562172),
                        description = emb_desc)
    foot = "Total Online: {}\nMax Capacity: {}\nTotal Lobbies: {}\nLobbies Recommended: {}".format(total_online, max_capacity, total_lobies, total_found)
    embed.set_footer(text = foot)
    return embed, prom_desc

def gonline_p1(maps, host_data):
    games_o = {}
    overall_online = 0
    for e_map in host_data:
        if e_map[-1]["i"] in maps:
            try:
                games_o[e_map[-1]["i"]]
            except:
                games_o[e_map[-1]["i"]] = [0, 0]
            games_o[e_map[-1]["i"]][0] += e_map[2]
            games_o[e_map[-1]["i"]][1] += 1
            overall_online += e_map[2]
    return dict(sorted(games_o.items(), key=lambda x: x[1][0], reverse=True)), overall_online


def gonline_p2(host_data, client):
    games_o = {}
    overall_online = 0
    for e_map in host_data:
        overall_online += e_map[2]
        if e_map[-1]["i"].lower() in client.official_maps:
            continue
        try:
            games_o[e_map[-1]["i"]][0] += e_map[2]
            games_o[e_map[-1]["i"]][1] += 1
        except:
            games_o[e_map[-1]["i"]] = [e_map[2], 1]
    return dict(sorted(games_o.items(), key=lambda x: x[1][0], reverse=True)[:30]), overall_online

