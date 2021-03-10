import discord, emoji, math, textwrap
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont, ImageOps, ImageFilter, ImageColor, ImageSequence, ImageEnhance
from PIL.ImageColor import getcolor, getrgb
from PIL.ImageOps import grayscale
from io import BytesIO
import asyncio, pickle, aiofiles
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures, getpass
shard_count = 1 if getpass.getuser() == "MN" else 6
import websockets, msgpack, time, requests
import datetime, difflib
import random, math, string
import matplotlib.pyplot as plt
import matplotlib.text as txt
import datetime, js2py
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pylab as pylab
import matplotlib, ago
matplotlib.use('Agg')
from iteration_utilities import duplicates
import numpy as np, functools
from PIL import ImageChops
import json, threading, aiohttp, subprocess
from output_generator import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib
from urllib.parse import unquote
from resizeimage import resizeimage
import Levenshtein as lvl
#from scipy.interpolate import interpolate

client = discord.AutoShardedClient(shard_count = shard_count)
client.connected_ = False
client.cptpause = False
client.cptnotice = "Krunker Social is currently not giving expected response (captchas). Please try again later."


#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
print("Initialized")
#loading = emoji.emojize(":arrows_counterclockwise:", use_aliases=True)
loading = emoji.emojize(":jigsaw:", use_aliases=True)
#warning = emoji.emojize(":warning:", use_aliases=True)
warning = emoji.emojize(":x:", use_aliases=True)
taskdone = emoji.emojize(":white_check_mark:", use_aliases=True)
recipt = emoji.emojize(":receipt:", use_aliases=True)
#question = emoji.emojize(":question:", use_aliases=True)
question = emoji.emojize(":question:", use_aliases=True)
prev_page = emoji.emojize(":arrow_backward:", use_aliases=True)
stop = emoji.emojize(":octagonal_sign:", use_aliases=True)
next_page = emoji.emojize(":arrow_forward:", use_aliases=True)
map_em = emoji.emojize(":map:", use_aliases=True)
check_mark = emoji.emojize(":white_check_mark:", use_aliases=True)
error = emoji.emojize(":x:", use_aliases=True)

emote_one = emoji.emojize(":one:", use_aliases=True)
emote_two = emoji.emojize(":two:", use_aliases=True)
emote_three = emoji.emojize(":three:", use_aliases=True)
emote_four = emoji.emojize(":four:", use_aliases=True)

y_cube = emoji.emojize(":yellow_square:", use_aliases=True)
b_cube = emoji.emojize(":blue_square:", use_aliases=True)
p_cube = emoji.emojize(":purple_square:", use_aliases=True)
w_cube = emoji.emojize(":white_large_square:", use_aliases=True)
mail = emoji.emojize(":e_mail:", use_aliases=True)
weapons = ["Knife", "Sniper Rifle", "Assault Rifle",
           "Pistol", "Submachine Gun", "Revolver",
           "Shotgun", "Machine Gun", "Semi Auto",
           "Rocket Launcher", "Akimbo Uzi", "Desert Eagle",
           "Alien Blaster", "", "Crossbow", "Famas",
           "Sawed Off", "Auto Pistol"];
weapons = ["Knife", "Sniper", "AR",
           "Pistol", "Smg", "Revolver",
           "Shotgun", "Lmg", "Auto",
           "Rl", "Uzi", "Deagle",
           "Alien Blaster", "", "Crossbow", "Famas",
           "Sawed Off", "Auto Pistol"];

exec('from js2py.pyjs import *\n# setting scope\nvar = Scope( JS_BUILTINS )\nset_global_object(var)\n\n# Code follows:\nvar.registers([\'getPreview\', \'types\'])\n@Js\ndef PyJsHoisted_getPreview_(a, this, arguments, var=var):\n    var = Scope({\'a\':a, \'this\':this, \'arguments\':arguments}, var)\n    var.registers([\'a\'])\n    def PyJs_LONG_1_(var=var):\n        def PyJs_LONG_0_(var=var):\n            return (((var.get(\'a\').get(\'weapon\') or Js(0.0))+Js(\'_\'))+(((var.get(\'a\').get(\'tex\') if var.get(\'a\').get(\'tex\') else var.get(\'a\').get(\'id\')) if (var.get(u"null")==var.get(\'a\').get(\'pat\')) else (Js(\'c\')+var.get(\'a\').get(\'pat\'))) if (var.get(u"null")==var.get(\'a\').get(\'mid\')) else ((Js(\'m\')+var.get(\'a\').get(\'mid\'))+(Js(\'\') if (var.get(u"null")==var.get(\'a\').get(\'midT\')) else (Js(\'_\')+var.get(\'a\').get(\'midT\'))))))\n        return (((((Js(\'cosmetics/\')+var.get(\'a\').get(\'type\'))+Js(\'_\'))+var.get(\'a\').get(\'id\'))+((Js(\'_\')+var.get(\'a\').get(\'tex\')) if var.get(\'a\').get(\'tex\') else Js(\'\'))) if (var.get(\'a\').get(\'type\') and ((Js(3.0)>var.get(\'a\').get(\'type\')) or (Js(4.0)<var.get(\'a\').get(\'type\')))) else (var.get(\'types\').get((var.get(\'a\').get(\'type\') or Js(0.0)))+((var.get(\'a\').get(\'id\')+((Js(\'\') if (var.get(u"null")==var.get(\'a\').get(\'tex\')) else (Js(\'_\')+var.get(\'a\').get(\'tex\'))) if (var.get(u"null")==var.get(\'a\').get(\'pat\')) else (Js(\'_c\')+var.get(\'a\').get(\'pat\')))) if (var.get(\'a\').get(\'type\') and (Js(3.0)==var.get(\'a\').get(\'type\'))) else PyJs_LONG_0_())))\n    return ((Js(\'https://assets.krunker.io/textures/\')+((Js(\'sprays/\')+var.get(\'a\').get(\'id\')) if (var.get(\'a\').get(\'type\') and (Js(4.0)==var.get(\'a\').get(\'type\'))) else (Js(\'previews/\')+PyJs_LONG_1_())))+Js(\'.png\'))\nPyJsHoisted_getPreview_.func_name = \'getPreview\'\nvar.put(\'getPreview\', PyJsHoisted_getPreview_)\nJs(\'use strict\')\nvar.put(\'types\', Js([Js(\'weapons/weapon_\'), Js(\'hats/hat_\'), Js(\'body/body_\'), Js(\'melee/melee_\'), Js(\'sprays/\'), Js(\'dyes/\')]))\npass\npass\n')
exec('from js2py.pyjs import *\n# setting scope\nvar = Scope( JS_BUILTINS )\nset_global_object(var)\n\n# Code follows:\nvar.registers([\'classForWeapon\', \'h\', \'cosmetics\', \'types\', \'getViewer\', \'second\', \'v\', \'rarityColor\', \'rarities\', \'weapons\'])\n@Js\ndef PyJsHoisted_getViewer_(a, this, arguments, var=var):\n    var = Scope({\'a\':a, \'this\':this, \'arguments\':arguments}, var)\n    var.registers([\'a\'])\n    if var.get(\'a\'):\n        if (Js(1.0)==var.get(\'a\').get(\'type\')):\n            return (Js(\'https://krunker.io/viewer.html?class=9&hat=\')+var.get(\'a\').get(\'i\'))\n        else:\n            if (Js(2.0)==var.get(\'a\').get(\'type\')):\n                return (Js(\'https://krunker.io/viewer.html?class=9&back=\')+var.get(\'a\').get(\'i\'))\n            else:\n                if (Js(3.0)==var.get(\'a\').get(\'type\')):\n                    return (Js(\'https://krunker.io/viewer.html?class=9&hidePlayer&melee=\')+var.get(\'a\').get(\'i\'))\n                else:\n                    if (Js(5.0)==var.get(\'a\').get(\'type\')):\n                        return (Js(\'https://krunker.io/viewer.html?class=9&dye=\')+var.get(\'a\').get(\'i\'))\n                    else:\n                        if (Js(6.0)==var.get(\'a\').get(\'type\')):\n                            return (Js(\'https://krunker.io/viewer.html?class=9&waist=\')+var.get(\'a\').get(\'i\'))\n                        else:\n                            if (Js(7.0)==var.get(\'a\').get(\'type\')):\n                                return (Js(\'https://krunker.io/viewer.html?class=9&face=\')+var.get(\'a\').get(\'i\'))\n                            else:\n                                if ((var.get(\'a\').get(\'weapon\').typeof()==Js(\'integer\')) and var.get(\'second\').callprop(\'indexOf\', (var.get(\'a\').get(\'weapon\')-Js(1.0)))):\n                                    return (((Js(\'https://krunker.io/viewer.html?hidePlayer&swap=-1&nosup&skinIdS=\')+var.get(\'a\').get(\'i\'))+Js(\'&secIndex=\'))+(var.get(\'a\').get(\'weapon\')-Js(1.0)))\n                                else:\n                                    return (((Js(\'https://krunker.io/viewer.html?class=\')+var.get(\'classForWeapon\').get((var.get(\'a\').get(\'weapon\')-Js(1.0))))+Js(\'&hidePlayer&nosup&skinIdP=\'))+var.get(\'a\').get(\'i\'))\nPyJsHoisted_getViewer_.func_name = \'getViewer\'\nvar.put(\'getViewer\', PyJsHoisted_getViewer_)\nvar.put(\'types\', Js([Js(\'weapons/weapon_\'), Js(\'hats/hat_\'), Js(\'body/body_\'), Js(\'melee/melee_\'), Js(\'sprays/\'), Js(\'dyes/\')]))\nvar.put(\'rarityColor\', Js([Js(\'#b2f252\'), Js(\'#2196F3\'), Js(\'#E040FB\'), Js(\'#FBC02D\'), Js(\'#ed4242\'), Js(\'#171717\'), Js(\'#fff53d\')]))\nvar.put(\'rarities\', Js([Js(\'Uncommon\'), Js(\'Rare\'), Js(\'Epic\'), Js(\'Legendary\'), Js(\'Relic\'), Js(\'Contraband\'), Js(\'Unobtainable\')]))\nvar.put(\'weapons\', Js([Js(\'Knife\'), Js(\'Sniper Rifle\'), Js(\'Assault Rifle\'), Js(\'Pistol\'), Js(\'Submachine Gun\'), Js(\'Revolver\'), Js(\'Shotgun\'), Js(\'Machine Gun\'), Js(\'Semi Auto\'), Js(\'Rocket Launcher\'), Js(\'Akimbo Uzi\'), Js(\'Desert Eagle\'), Js(\'Alien Blaster\'), Js(\'\'), Js(\'Crossbow\'), Js(\'Famas\'), Js(\'Sawed Off\'), Js(\'Auto Pistol\')]))\nvar.put(\'cosmetics\', Js([Js(\'\'), Js(\'Hat\'), Js(\'Back\'), Js(\'\'), Js(\'Spray\'), Js(\'Dye\'), Js(\'Waist\')]))\nvar.put(\'second\', Js([Js(2.0), Js(10.0), Js(11.0), Js(15.0), Js(16.0)]))\nvar.put(\'classForWeapon\', Js([Js(1.0), Js(0.0), Js(0.0), Js(2.0), Js(5.0), Js(4.0), Js(3.0), Js(6.0), Js(7.0), Js(8.0), Js(10.0), Js(0.0), Js(11.0), Js(12.0), Js(0.0), Js(13.0)]))\nvar.put(\'h\', Js([Js({\'name\':Js(\'Sniper Rifle\'),\'src\':Js(\'weapon_1\'),\'icon\':Js(\'icon_1\'),\'sound\':Js(\'weapon_1\'),\'animWhileAim\':Js(True),\'trail\':Js(True),\'flap\':Js({\'src\':Js(\'flap_0\'),\'rot\':Js(2.1),\'scl\':Js(1.0),\'zOff\':Js(0.43),\'xOff\':Js(0.17),\'yOff\':Js(0.53)}),\'noAo\':Js(True),\'nAuto\':Js(True),\'type\':Js(0.0),\'scope\':Js(True),\'swapTime\':Js(300.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(0.95),\'ammo\':Js(3.0),\'dmg\':Js(100.0),\'pierce\':Js(0.2),\'reload\':Js(1500.0),\'range\':Js(1000.0),\'dropStart\':Js(230.0),\'dmgDrop\':Js(30.0),\'scale\':Js(0.00115608717587935),\'leftHoldY\':(-Js(0.65)),\'rightHoldY\':(-Js(0.68)),\'leftHoldZ\':Js(2.1),\'rightHoldZ\':Js(0.75),\'holdW\':Js(1.0),\'xOff\':Js(0.8),\'yOff\':(-Js(0.65)),\'zOff\':(-Js(1.8)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.55)),\'zOrg\':(-Js(0.8)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'inspectR\':Js(0.2),\'inspectM\':Js(0.1),\'muzOff\':Js(8.0),\'muzMlt\':Js(1.6),\'rate\':Js(900.0),\'spread\':Js(260.0),\'zoom\':Js(2.7),\'leanMlt\':Js(1.5),\'recoil\':Js(0.009),\'recoilR\':Js(0.02),\'recover\':Js(0.993),\'recoverY\':Js(0.997),\'recoverF\':Js(0.975),\'recoilYM\':Js(0.35),\'recoilZ\':Js(1.4),\'recoilAnim\':Js({\'time\':Js(280.0),\'aimTime\':Js(500.0),\'recoilTweenY\':Js(0.3)}),\'jumpYM\':Js(0.15),\'rumble\':Js(0.9),\'rumbleDur\':Js(500.0),\'icnPad\':Js(9.0)}), Js({\'name\':Js(\'Assault Rifle\'),\'src\':Js(\'weapon_2\'),\'icon\':Js(\'icon_2\'),\'sound\':Js(\'weapon_2\'),\'noAo\':Js(True),\'swapWiggle\':Js(0.3),\'attach\':Js(0.0),\'attachYOff\':(-Js(0.06)),\'attachZOff\':(-Js(0.8)),\'zRot\':Js(1.0),\'type\':Js(0.0),\'swapTime\':Js(300.0),\'aimSpeed\':Js(130.0),\'spdMlt\':Js(0.95),\'ammo\':Js(30.0),\'rate\':Js(110.0),\'reload\':Js(1200.0),\'dmg\':Js(23.0),\'pierce\':Js(1.0),\'range\':Js(700.0),\'dmgDrop\':Js(5.0),\'scale\':Js(0.00095745145728643),\'leftHoldY\':(-Js(0.41)),\'rightHoldY\':(-Js(0.6)),\'leftHoldZ\':Js(0.5),\'rightHoldZ\':(-Js(1.2)),\'holdW\':Js(0.8),\'xOff\':Js(1.0),\'yOff\':(-Js(0.9)),\'rotOff\':(-Js(0.03)),\'aimOffY\':Js(0.042),\'yRot\':Js(0.0018),\'zOff\':(-Js(3.6)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.59)),\'zOrg\':(-Js(2.3)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'inspectR\':Js(0.1),\'inspectM\':Js(1.5),\'caseZOff\':(-Js(1.7)),\'caseYOff\':(-Js(0.2)),\'muzOff\':Js(5.1),\'muzOffY\':(-Js(0.05)),\'muzMlt\':Js(1.4),\'spread\':Js(100.0),\'minSpread\':Js(5.0),\'zoom\':Js(1.6),\'leanMlt\':Js(1.5),\'recoil\':Js(0.003),\'recoilR\':Js(0.021),\'recover\':Js(0.978),\'recoverY\':Js(0.995),\'recoverF\':Js(0.975),\'jYMlt\':Js(0.9),\'recoilYM\':Js(0.35),\'recoilZ\':Js(5.7),\'recoilZM\':(-Js(0.05)),\'aimRecMlt\':Js(0.7),\'recoilAnim\':Js({\'time\':Js(300.0),\'recoilTweenY\':Js(0.05)}),\'jumpYM\':Js(0.6),\'rumble\':Js(0.5),\'icnPad\':Js(5.0)}), Js({\'name\':Js(\'Pistol\'),\'src\':Js(\'weapon_3\'),\'icon\':Js(\'icon_3\'),\'sound\':Js(\'weapon_3\'),\'secondary\':Js(True),\'noAo\':Js(True),\'transp\':Js(True),\'nAuto\':Js(True),\'kill\':Js([Js(\'\'), Js(75.0)]),\'swapWiggle\':Js(0.3),\'type\':Js(1.0),\'shine\':Js(10.0),\'swapTime\':Js(350.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.05),\'ammo\':Js(10.0),\'reload\':Js(700.0),\'dmg\':Js(20.0),\'range\':Js(700.0),\'dmgDrop\':Js(10.0),\'scale\':Js(0.0003158947055276376),\'leftHoldY\':(-Js(1.1)),\'rightHoldY\':(-Js(0.62)),\'leftHoldZ\':(-Js(0.3)),\'rightHoldZ\':(-Js(0.32)),\'rightHoldX\':Js(0.13),\'holdW\':Js(1.3),\'xOff\':Js(1.2),\'yOff\':(-Js(0.6)),\'zOff\':(-Js(3.7)),\'xOrg\':Js(0.0),\'yRot\':(-Js(0.005)),\'yOrg\':(-Js(0.23)),\'zOrg\':(-Js(3.9)),\'jYMlt\':Js(0.1),\'cLean\':Js(0.3),\'cRot\':Js(0.3),\'caseZOff\':Js(0.2),\'caseYOff\':Js(0.0),\'inspectR\':Js(0.3),\'inspectM\':Js(0.8),\'muzOff\':Js(1.5),\'muzOffY\':Js(0.0),\'muzMlt\':Js(0.95),\'rate\':Js(150.0),\'spread\':Js(60.0),\'zoom\':Js(1.4),\'leanMlt\':Js(1.0),\'recoil\':Js(0.006),\'recoilR\':Js(0.01),\'recover\':Js(0.98),\'recoverY\':Js(0.99),\'recoverF\':Js(0.98),\'recoilYM\':Js(0.2),\'aimRecMlt\':Js(0.4),\'recoilZ\':Js(3.8),\'recoilZM\':(-Js(0.4)),\'recoilAnim\':Js({\'time\':Js(200.0),\'recoilTweenY\':Js(0.28)}),\'rumble\':Js(0.4),\'icnPad\':(-Js(15.0)),\'expScale\':Js(0.8)}), Js({\'name\':Js(\'Submachine Gun\'),\'src\':Js(\'weapon_4\'),\'icon\':Js(\'icon_4\'),\'sound\':Js(\'weapon_4\'),\'swapWiggle\':Js(0.5),\'attach\':Js(0.0),\'attachYOff\':(-Js(0.09)),\'attachZOff\':(-Js(1.1)),\'zRot\':Js(0.75),\'noAo\':Js(True),\'type\':Js(0.0),\'shine\':Js(50.0),\'swapTime\':Js(300.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.04),\'ammo\':Js(28.0),\'reload\':Js(1000.0),\'dmg\':Js(18.0),\'pierce\':Js(1.0),\'range\':Js(700.0),\'dmgDrop\':Js(12.0),\'scale\':Js(0.000574897587939697),\'leftHoldY\':(-Js(0.4)),\'leftHoldX\':(-Js(0.1)),\'leftHoldZ\':Js(1.1),\'rightHoldZ\':(-Js(0.95)),\'rightHoldY\':(-Js(0.5)),\'holdW\':Js(0.85),\'xOff\':Js(0.85),\'yOff\':(-Js(0.86)),\'zOff\':(-Js(3.0)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.59)),\'zOrg\':(-Js(2.5)),\'cRot\':Js(0.18),\'cLean\':Js(0.16),\'inspectR\':Js(0.2),\'inspectM\':Js(1.2),\'caseYOff\':(-Js(0.15)),\'caseZOff\':(-Js(0.4)),\'muzOff\':Js(2.15),\'muzOffY\':Js(0.1),\'rate\':Js(90.0),\'spread\':Js(70.0),\'minSpread\':Js(5.0),\'zoom\':Js(1.65),\'jYMlt\':Js(0.8),\'leanMlt\':Js(1.0),\'recoil\':Js(0.0034),\'recoilY\':Js(0.77),\'recoilR\':Js(0.02),\'recover\':Js(0.975),\'recoverY\':Js(0.996),\'recoverF\':Js(0.975),\'recoilZ\':Js(3.2),\'recoilZM\':(-Js(0.1)),\'aimRecMlt\':Js(0.6),\'recoilAnim\':Js({\'time\':Js(200.0),\'recoilTweenYM\':Js(0.05),\'recoilTweenY\':Js(0.06)}),\'expScale\':Js(0.8),\'rumble\':Js(0.4),\'icnPad\':Js(0.0)}), Js({\'name\':Js(\'Revolver\'),\'src\':Js(\'weapon_5\'),\'icon\':Js(\'icon_5\'),\'sound\':Js(\'weapon_5\'),\'nAuto\':Js(True),\'noAo\':Js(True),\'nCase\':Js(True),\'transp\':Js(True),\'kill\':Js([Js(\'\'), Js(50.0)]),\'type\':Js(0.0),\'swapTime\':Js(200.0),\'swapWiggle\':Js(0.4),\'aimSpeed\':Js(110.0),\'spdMlt\':Js(1.04),\'ammo\':Js(6.0),\'reload\':Js(900.0),\'dmg\':Js(66.0),\'pierce\':Js(0.85),\'dmgDrop\':Js(10.0),\'scale\':Js(0.000515531266331653),\'hDstOff\':Js(1.6),\'leftHoldY\':(-Js(1.3)),\'rightHoldY\':(-Js(0.8)),\'leftHoldZ\':(-Js(0.6)),\'rightHoldZ\':(-Js(0.72)),\'rightHoldX\':Js(0.1),\'holdW\':Js(1.1),\'rotOff\':(-Js(0.05)),\'xOff\':Js(0.7),\'yOff\':(-Js(0.5)),\'zOff\':(-Js(3.5)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.31)),\'zOrg\':(-Js(3.5)),\'jYMlt\':Js(0.8),\'cLean\':Js(0.2),\'cRot\':Js(0.1),\'cDrop\':Js(0.1),\'inspectR\':Js(0.1),\'inspectM\':Js(0.3),\'muzOff\':Js(2.75),\'muzOffY\':Js(0.2),\'muzMlt\':Js(0.95),\'range\':Js(700.0),\'rate\':Js(390.0),\'spread\':Js(100.0),\'zoom\':Js(1.45),\'leanMlt\':Js(1.6),\'recoil\':Js(0.013),\'recoilR\':Js(0.06),\'recover\':Js(0.982),\'recoverY\':Js(0.992),\'recoverF\':Js(0.98),\'recoilYM\':Js(0.5),\'aimRecMlt\':Js(0.1),\'recoilZM\':Js(0.01),\'recoilZ\':Js(3.4),\'recoilAnim\':Js({\'time\':Js(300.0),\'recoilTweenY\':Js(0.36),\'recoilTweenYM\':Js(0.25)}),\'expScale\':Js(0.9),\'rumble\':Js(0.7),\'icnPad\':(-Js(10.0))}), Js({\'name\':Js(\'Shotgun\'),\'src\':Js(\'weapon_6\'),\'icon\':Js(\'icon_6\'),\'sound\':Js(\'weapon_6\'),\'altSkin\':Js({\'name\':Js(\'Nova Pump\'),\'mid\':Js(0.0),\'blocked\':Js(True),\'noSale\':Js(True),\'midT\':Js(38.0),\'scl\':Js(0.9),\'mScl\':Js(1.0),\'zOff\':Js(0.28),\'yOff\':(-Js(0.5)),\'seas\':Js(2.0),\'weapon\':Js(6.0),\'rarity\':Js(0.0)}),\'noAo\':Js(True),\'nAuto\':Js(True),\'nCase\':Js(True),\'nRing\':Js(True),\'swapWiggle\':Js(0.4),\'shine\':Js(35.0),\'type\':Js(0.0),\'physRang\':Js(35.0),\'physPow\':Js(0.085),\'swapTime\':Js(300.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.0),\'ammo\':Js(2.0),\'reload\':Js(1100.0),\'dmg\':Js(50.0),\'dmgDrop\':Js(50.0),\'scale\':Js(0.00082934281407035),\'rightHoldX\':Js(0.1),\'leftHoldY\':(-Js(0.6)),\'rightHoldY\':(-Js(0.6)),\'leftHoldZ\':Js(0.4),\'rightHoldZ\':(-Js(1.3)),\'holdW\':Js(1.0),\'xOff\':Js(0.95),\'yOff\':(-Js(0.6)),\'zOff\':(-Js(3.8)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.3)),\'zOrg\':(-Js(2.8)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'jYMlt\':Js(0.2),\'inspectR\':Js(0.1),\'muzOff\':Js(6.0),\'muzMlt\':Js(1.8),\'inspectM\':Js(1.9),\'range\':Js(180.0),\'rate\':Js(400.0),\'innac\':Js(110.0),\'spread\':Js(180.0),\'shots\':Js(5.0),\'cSpread\':Js([Js(0.03), Js(0.02), (-Js(0.27)), Js(0.02), Js(0.03), (-Js(0.31)), Js(0.3), (-Js(0.01)), Js(0.01), Js(0.28), Js(0.01), Js(0.02), (-Js(0.17)), (-Js(0.22)), (-Js(0.3)), Js(0.31), Js(0.32), Js(0.28), Js(0.3), (-Js(0.2))]),\'minSpread\':Js(20.0),\'zoom\':Js(1.25),\'leanMlt\':Js(1.6),\'recoil\':Js(0.02),\'recoilR\':Js(0.015),\'recover\':Js(0.99),\'recoverF\':Js(0.97),\'recoilZ\':Js(2.1),\'recoilZM\':Js(0.2),\'aimRecMlt\':Js(0.67),\'recoilYM\':Js(0.65),\'recoilAnim\':Js({\'time\':Js(340.0),\'recoilTweenY\':Js(0.22)}),\'jumpYM\':Js(0.5),\'rumble\':Js(0.8),\'icnPad\':Js(10.0),\'expScale\':Js(0.85)}), Js({\'name\':Js(\'Machine Gun\'),\'src\':Js(\'weapon_7\'),\'icon\':Js(\'icon_7\'),\'sound\':Js(\'weapon_7\'),\'type\':Js(0.0),\'attach\':Js(0.0),\'swapWiggle\':Js(0.3),\'attachYOff\':(-Js(0.085)),\'attachZOff\':(-Js(0.7)),\'zRot\':Js(0.75),\'noAo\':Js(True),\'swapTime\':Js(700.0),\'aimSpeed\':Js(200.0),\'spdMlt\':Js(0.79),\'jumMlt\':Js(0.85),\'ammo\':Js(60.0),\'reload\':Js(3500.0),\'dmg\':Js(20.0),\'pierce\':Js(1.0),\'range\':Js(700.0),\'dmgDrop\':Js(10.0),\'jYMlt\':Js(0.8),\'scale\':Js(0.0008856008924623108),\'leftHoldY\':(-Js(0.85)),\'leftHoldX\':Js(0.4),\'rightHoldY\':(-Js(0.75)),\'leftHoldZ\':Js(1.1),\'rightHoldZ\':(-Js(0.2)),\'holdW\':Js(1.1),\'yRot\':(-Js(0.01)),\'xOff\':Js(0.95),\'yOff\':(-Js(0.75)),\'zOff\':(-Js(2.8)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.6)),\'zOrg\':(-Js(1.8)),\'cLean\':Js(0.1),\'cRot\':Js(0.1),\'cDrop\':Js(0.1),\'inspectR\':Js(0.2),\'inspectM\':Js(0.6),\'caseInd\':Js(2.0),\'caseZOff\':(-Js(0.5)),\'caseYOff\':(-Js(0.1)),\'muzOff\':Js(5.5),\'muzOffY\':(-Js(0.14)),\'muzMlt\':Js(1.7),\'rate\':Js(130.0),\'spread\':Js(300.0),\'minSpread\':Js(10.0),\'zoom\':Js(1.3),\'leanMlt\':Js(1.6),\'recoil\':Js(0.0032),\'recoilR\':Js(0.014),\'recover\':Js(0.98),\'recoverY\':Js(0.9975),\'recoverF\':Js(0.975),\'recoilZ\':Js(3.0),\'recoilYM\':Js(0.25),\'recoilZM\':(-Js(0.1)),\'aimRecMlt\':Js(0.5),\'recoilAnim\':Js({\'time\':Js(200.0),\'recoilTweenY\':Js(0.055)}),\'jumpYM\':Js(0.5),\'expScale\':Js(0.85),\'rumble\':Js(0.65),\'icnPad\':Js(10.0),\'forceAttach\':Js(True)}), Js({\'name\':Js(\'Semi Auto\'),\'src\':Js(\'weapon_8\'),\'icon\':Js(\'icon_8\'),\'sound\':Js(\'weapon_8\'),\'altSkin\':Js({\'name\':Js(\'Nova Semi\'),\'blocked\':Js(True),\'noSale\':Js(True),\'mid\':Js(0.0),\'midT\':Js(0.0),\'seas\':Js(3.0),\'weapon\':Js(8.0),\'rarity\':Js(0.0)}),\'attach\':Js(0.0),\'attachYOff\':(-Js(0.08)),\'attachZOff\':(-Js(1.55)),\'nAuto\':Js(True),\'zRot\':Js(0.7),\'type\':Js(0.0),\'noAo\':Js(True),\'swapWiggle\':Js(0.4),\'swapTime\':Js(300.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.0),\'ammo\':Js(8.0),\'reload\':Js(1500.0),\'dmg\':Js(35.0),\'pierce\':Js(0.2),\'range\':Js(1000.0),\'dmgDrop\':Js(0.0),\'scale\':Js(0.00093686221105528),\'leftHoldY\':(-Js(0.5)),\'rightHoldY\':(-Js(0.45)),\'leftHoldZ\':Js(0.4),\'rightHoldZ\':(-Js(1.85)),\'jYMlt\':Js(0.9),\'xOff\':Js(0.8),\'yOff\':(-Js(0.55)),\'zOff\':(-Js(3.5)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.395)),\'yRot\':(-Js(0.005)),\'zOrg\':(-Js(3.4)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'inspectR\':Js(0.2),\'inspectM\':Js(1.4),\'muzOff\':Js(4.0),\'muzOffY\':(-Js(0.05)),\'muzMlt\':Js(1.1),\'rate\':Js(120.0),\'spread\':Js(250.0),\'caseZOff\':(-Js(1.3)),\'zoom\':Js(2.1),\'recoil\':Js(0.01),\'recoilR\':Js(0.012),\'recover\':Js(0.98),\'recoilY\':Js(0.36),\'recoverY\':Js(0.994),\'recoverF\':Js(0.975),\'recoilYM\':Js(0.6),\'recoilZ\':Js(2.0),\'recoilZM\':Js(0.2),\'aimRecMlt\':Js(0.8),\'recoilAnim\':Js({\'time\':Js(250.0),\'recoilTweenY\':Js(0.11)}),\'jumpYM\':Js(0.5),\'rumble\':Js(0.75),\'icnPad\':Js(10.0)}), Js({\'name\':Js(\'Rocket Launcher\'),\'src\':Js(\'weapon_9\'),\'icon\':Js(\'icon_9\'),\'sound\':Js(\'weapon_9\'),\'nInsp\':Js(True),\'nSkill\':Js(True),\'nAuto\':Js(True),\'nCase\':Js(True),\'nRing\':Js(True),\'noAo\':Js(True),\'projectile\':Js(0.0),\'type\':Js(0.0),\'swapTime\':Js(400.0),\'swapWiggle\':Js(0.4),\'aimSpeed\':Js(200.0),\'spdMlt\':Js(0.9),\'physRang\':Js(40.0),\'physPow\':Js(0.095),\'ammo\':Js(2.0),\'shots\':Js(0.0),\'reload\':Js(1800.0),\'scale\':Js(0.00076263407035176),\'leftHoldX\':(-Js(0.1)),\'leftHoldY\':(-Js(0.36)),\'rightHoldY\':(-Js(0.3)),\'leftHoldZ\':Js(1.2),\'rightHoldX\':(-Js(0.15)),\'rightHoldZ\':(-Js(0.45)),\'holdW\':Js(0.9),\'jYMlt\':Js(0.4),\'xOff\':Js(0.95),\'yOff\':(-Js(0.56)),\'zOff\':(-Js(2.6)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.945)),\'zOrg\':(-Js(3.0)),\'zRot\':Js(0.9),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'muzOff\':Js(5.0),\'muzOffY\':Js(0.0),\'muzMlt\':Js(1.5),\'rate\':Js(350.0),\'spread\':Js(120.0),\'minSpread\':Js(15.0),\'zoom\':Js(1.5),\'leanMlt\':Js(1.4),\'landBob\':Js(0.8),\'recoil\':Js(0.008),\'recoilR\':Js(0.012),\'recover\':Js(0.99),\'recoverY\':Js(0.998),\'recoverF\':Js(0.975),\'recoilZ\':Js(4.0),\'recoilZM\':(-Js(0.5)),\'aimRecMlt\':Js(0.9),\'recoilAnim\':Js({\'time\':Js(400.0),\'recoilTweenY\':Js(0.25)}),\'jumpYM\':Js(0.3),\'expScale\':Js(0.7),\'rumble\':Js(1.0),\'rumbleDur\':Js(750.0),\'icnPad\':Js(10.0)}), Js({\'name\':Js(\'Akimbo Uzi\'),\'src\':Js(\'weapon_10\'),\'icon\':Js(\'icon_10\'),\'sound\':Js(\'weapon_10\'),\'altSkin\':Js({\'name\':Js(\'Nova Uzi\'),\'mid\':Js(0.0),\'midT\':Js(0.0),\'blocked\':Js(True),\'noSale\':Js(True),\'weapon\':Js(10.0),\'rarity\':Js(0.0),\'seas\':Js(3.0)}),\'nInsp\':Js(True),\'noAim\':Js(True),\'akimbo\':Js(True),\'type\':Js(0.0),\'swapTime\':Js(300.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.04),\'ammo\':Js(18.0),\'reload\':Js(1300.0),\'dmg\':Js(14.0),\'pierce\':Js(1.0),\'range\':Js(700.0),\'dmgDrop\':Js(13.0),\'scale\':Js(0.9),\'rightHoldY\':(-Js(0.55)),\'leftHoldZ\':Js(0.2),\'leftHoldX\':(-Js(0.1)),\'leftHoldY\':(-Js(0.55)),\'rightHoldZ\':Js(0.2),\'rightHoldX\':(-Js(0.1)),\'holdW\':Js(1.3),\'xOff\':Js(1.5),\'yOff\':(-Js(0.95)),\'zOff\':(-Js(3.3)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.62)),\'zOrg\':(-Js(2.5)),\'zLnM\':Js(0.4),\'cLean\':Js(0.1),\'cRot\':Js(0.1),\'cDrop\':Js(0.2),\'caseYOff\':(-Js(0.15)),\'caseZOff\':(-Js(0.4)),\'muzOff\':Js(3.6),\'rate\':Js(70.0),\'spread\':Js(40.0),\'noSpread\':Js(True),\'minSpread\':Js(50.0),\'zoom\':Js(1.5),\'recoil\':Js(0.0034),\'recoilR\':Js(0.015),\'leanMlt\':Js(0.6),\'recover\':Js(0.978),\'recoverY\':Js(0.996),\'recoverF\':Js(0.975),\'recoilZ\':Js(5.0),\'recoilYM\':Js(0.6),\'recoilAnim\':Js({\'recoilTweenY\':Js(0.01)}),\'expScale\':Js(0.7),\'rumble\':Js(0.4),\'icnPad\':(-Js(4.0))}), Js({\'name\':Js(\'Desert Eagle\'),\'src\':Js(\'weapon_11\'),\'icon\':Js(\'icon_11\'),\'sound\':Js(\'weapon_11\'),\'secondary\':Js(True),\'minRec\':Js(15.0),\'nAuto\':Js(True),\'noAo\':Js(True),\'transp\':Js(True),\'kill\':Js([Js(\'\'), Js(50.0)]),\'type\':Js(1.0),\'swapTime\':Js(200.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.0),\'ammo\':Js(6.0),\'reload\':Js(1000.0),\'dmg\':Js(50.0),\'pierce\':Js(0.85),\'dmgDrop\':Js(10.0),\'scale\':Js(0.94),\'leftHoldY\':(-Js(0.9)),\'rightHoldY\':(-Js(0.7)),\'leftHoldZ\':(-Js(0.5)),\'rightHoldZ\':(-Js(0.5)),\'holdW\':Js(1.1),\'xOff\':Js(1.0),\'yOff\':(-Js(0.55)),\'zOff\':(-Js(4.1)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.195)),\'zOrg\':(-Js(3.8)),\'cLean\':Js(0.3),\'cRot\':Js(0.3),\'inspectR\':Js(0.35),\'inspectM\':Js(0.9),\'muzOff\':Js(2.0),\'muzMlt\':Js(1.1),\'range\':Js(700.0),\'rate\':Js(400.0),\'spread\':Js(150.0),\'jYMlt\':Js(0.5),\'zoom\':Js(1.4),\'leanMlt\':Js(1.6),\'recoil\':Js(0.01),\'recoilR\':Js(0.01),\'recover\':Js(0.985),\'recoverY\':Js(0.996),\'recoverF\':Js(0.98),\'recoilYM\':Js(0.4),\'aimRecMlt\':Js(0.43),\'recoilZ\':Js(2.5),\'recoilZM\':Js(0.2),\'recoilAnim\':Js({\'time\':Js(270.0),\'recoilTweenY\':Js(0.42)}),\'rumble\':Js(0.8),\'icnPad\':(-Js(10.0)),\'expScale\':Js(1.55)}), Js({\'name\':Js(\'Alien Blaster\'),\'src\':Js(\'weapon_12\'),\'icon\':Js(\'icon_12\'),\'sound\':Js(\'weapon_12\'),\'secondary\':Js(True),\'nRing\':Js(True),\'nAuto\':Js(True),\'transp\':Js(True),\'nCase\':Js(True),\'minRec\':Js(50.0),\'kill\':Js([Js(\'\'), Js(50.0)]),\'type\':Js(1.0),\'swapTime\':Js(200.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.0),\'ammo\':Js(4.0),\'reload\':Js(1500.0),\'dmg\':Js(50.0),\'pierce\':Js(0.85),\'dmgDrop\':Js(10.0),\'scale\':Js(1.1),\'leftHoldY\':(-Js(1.0)),\'rightHoldY\':(-Js(0.65)),\'leftHoldZ\':(-Js(0.2)),\'rightHoldZ\':(-Js(0.2)),\'holdW\':Js(1.0),\'xOff\':Js(1.3),\'yOff\':(-Js(0.83)),\'zOff\':(-Js(4.1)),\'xOrg\':Js(0.0),\'yRot\':(-Js(0.01)),\'yOrg\':(-Js(0.53)),\'zOrg\':(-Js(3.8)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.0),\'inspectR\':Js(0.1),\'inspectM\':Js(0.8),\'muzOff\':Js(2.2),\'muzOffY\':Js(0.1),\'muzID\':Js(3.0),\'muzMlt\':Js(1.1),\'jYMlt\':Js(0.8),\'range\':Js(700.0),\'rate\':Js(170.0),\'spread\':Js(150.0),\'zoom\':Js(1.4),\'leanMlt\':Js(1.6),\'recoil\':Js(0.006),\'recoilR\':Js(0.01),\'recover\':Js(0.98),\'recoverY\':Js(0.99),\'recoverF\':Js(0.98),\'recoilYM\':Js(0.2),\'recoilZ\':Js(2.2),\'aimRecMlt\':Js(0.3),\'recoilAnim\':Js({\'time\':Js(200.0),\'recoilTweenY\':Js(0.32)}),\'rumble\':Js(0.4),\'icnPad\':(-Js(8.0)),\'expScale\':Js(1.85)}), Js({\'name\':Js(\'Combat Knife\'),\'icon\':Js(\'icon_0\'),\'melee\':Js(True),\'nInsp\':Js(True),\'noSkins\':Js(True),\'holdW\':Js(0.9),\'swapWiggle\':Js(0.3),\'sounds\':Js([Js(\'swish_0\'), Js(\'swish_1\')]),\'noAim\':Js(True),\'type\':Js(1.0),\'swapTime\':Js(280.0),\'aimSpeed\':Js(120.0),\'rate\':Js(250.0),\'dmg\':Js(50.0),\'dmgDrop\':Js(0.0),\'range\':Js(15.0),\'spdMlt\':Js(1.1),\'spread\':Js(100.0),\'leftHoldY\':(-Js(0.82)),\'leftHoldX\':Js(1.5),\'rightHoldX\':(-Js(1.5)),\'rightHoldY\':(-Js(0.82)),\'leftHoldZ\':(-Js(0.5)),\'rightHoldZ\':(-Js(0.5)),\'xOff\':Js(0.0),\'yOff\':(-Js(0.6)),\'zOff\':(-Js(3.6)),\'xOrg\':Js(0.5),\'yOrg\':Js(0.0),\'zOrg\':(-Js(3.6)),\'zRM\':Js(0.35),\'zoom\':Js(1.0),\'leanMlt\':Js(0.8),\'recoil\':Js(0.006),\'recoilR\':Js(0.01),\'recover\':Js(0.98),\'recoverF\':Js(0.98),\'rumble\':Js(0.4),\'rumbleDur\':Js(150.0),\'icnPad\':(-Js(10.0))}), Js({\'name\':Js(\'Crossbow\'),\'src\':Js(\'weapon_14\'),\'icon\':Js(\'icon_14\'),\'sound\':Js(\'weapon_14\'),\'nInsp\':Js(True),\'nRing\':Js(True),\'nAuto\':Js(True),\'noAo\':Js(True),\'nCase\':Js(True),\'nMuz\':Js(True),\'attach\':Js(0.0),\'attachYOff\':(-Js(0.1)),\'attachZOff\':Js(0.65),\'kill\':Js([Js(\'\'), Js(100.0)]),\'type\':Js(0.0),\'projectile\':Js(1.0),\'swapTime\':Js(200.0),\'aimSpeed\':Js(120.0),\'spdMlt\':Js(1.0),\'ammo\':Js(1.0),\'reload\':Js(900.0),\'dmg\':Js(100.0),\'pierce\':Js(0.0),\'dmgDrop\':Js(0.0),\'scale\':Js(0.0007303348040201011),\'leftHoldY\':(-Js(0.33)),\'rightHoldY\':(-Js(0.28)),\'leftHoldZ\':Js(2.2),\'leftHoldX\':Js(0.0),\'rightHoldZ\':Js(0.9),\'xOff\':Js(1.3),\'yOff\':(-Js(0.95)),\'zOff\':(-Js(1.9)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.72)),\'zOrg\':(-Js(1.0)),\'cLean\':Js(0.1),\'cRot\':Js(0.1),\'zRot\':Js(0.9),\'cDrop\':Js(0.2),\'holdW\':Js(0.5),\'muzOff\':Js(2.2),\'muzOffY\':Js(0.1),\'muzID\':Js(3.0),\'muzMlt\':Js(1.1),\'jYMlt\':Js(0.95),\'range\':Js(700.0),\'rate\':Js(150.0),\'spread\':Js(300.0),\'zoom\':Js(1.4),\'leanMlt\':Js(0.3),\'recoil\':Js(0.007),\'recoilR\':Js(0.01),\'recover\':Js(0.985),\'recoverY\':Js(0.996),\'recoverF\':Js(0.98),\'recoilZ\':Js(4.0),\'recoilAnim\':Js({\'time\':Js(300.0),\'recoilTweenY\':Js(0.1)}),\'rumble\':Js(0.5),\'icnPad\':Js(9.0)}), Js({\'name\':Js(\'Famas\'),\'src\':Js(\'weapon_15\'),\'icon\':Js(\'icon_15\'),\'sound\':Js(\'weapon_15\'),\'noAo\':Js(True),\'nAuto\':Js(True),\'burst\':Js({\'c\':Js(3.0),\'r\':Js(90.0)}),\'swapWiggle\':Js(0.6),\'attach\':Js(0.0),\'attachYOff\':(-Js(0.1)),\'attachZOff\':(-Js(0.5)),\'zRot\':Js(1.0),\'type\':Js(0.0),\'swapTime\':Js(300.0),\'aimSpeed\':Js(130.0),\'spdMlt\':Js(0.95),\'ammo\':Js(30.0),\'rate\':Js(280.0),\'reload\':Js(1200.0),\'dmg\':Js(28.0),\'pierce\':Js(1.0),\'range\':Js(900.0),\'dmgDrop\':Js(5.0),\'scale\':Js(0.0008858419597989991),\'leftHoldY\':(-Js(0.45)),\'rightHoldY\':(-Js(0.5)),\'leftHoldZ\':Js(0.72),\'rightHoldZ\':(-Js(0.75)),\'holdW\':Js(1.0),\'xOff\':Js(1.0),\'yOff\':(-Js(0.86)),\'yRot\':Js(0.0018),\'zOff\':(-Js(3.0)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(1.14)),\'zOrg\':(-Js(2.0)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'inspectR\':Js(0.1),\'inspectM\':Js(1.5),\'caseZOff\':(-Js(1.7)),\'caseYOff\':(-Js(0.2)),\'muzOff\':Js(4.9),\'muzOffY\':(-Js(0.05)),\'muzMlt\':Js(1.4),\'spread\':Js(90.0),\'minSpread\':Js(5.0),\'zoom\':Js(1.5),\'leanMlt\':Js(1.5),\'recoil\':Js(0.003),\'recoilR\':Js(0.02),\'recover\':Js(0.978),\'recoverY\':Js(0.995),\'recoverF\':Js(0.975),\'jYMlt\':Js(0.9),\'recoilYM\':Js(0.32),\'recoilZ\':Js(5.5),\'recoilZM\':Js(0.05),\'aimRecMlt\':Js(0.65),\'recoilAnim\':Js({\'time\':Js(300.0),\'recoilTweenY\':Js(0.06)}),\'jumpYM\':Js(0.6),\'rumble\':Js(0.5),\'expScale\':Js(0.9),\'icnPad\':Js(9.0)}), Js({\'name\':Js(\'Sawed Off\'),\'src\':Js(\'weapon_16\'),\'icon\':Js(\'icon_16\'),\'sound\':Js(\'weapon_6\'),\'noAo\':Js(True),\'nAuto\':Js(True),\'nCase\':Js(True),\'nRing\':Js(True),\'secondary\':Js(True),\'minRec\':Js(20.0),\'swapWiggle\':Js(0.4),\'shine\':Js(35.0),\'type\':Js(1.0),\'physRang\':Js(36.0),\'physPow\':Js(0.1),\'swapTime\':Js(200.0),\'aimSpeed\':Js(100.0),\'spdMlt\':Js(1.0),\'ammo\':Js(1.0),\'reload\':Js(1100.0),\'dmg\':Js(12.0),\'dmgDrop\':Js(12.0),\'scale\':Js(1.0),\'rightHoldX\':Js(0.1),\'leftHoldY\':(-Js(0.5)),\'rightHoldY\':(-Js(0.6)),\'leftHoldZ\':Js(0.4),\'rightHoldZ\':(-Js(1.5)),\'holdW\':Js(1.0),\'xOff\':Js(0.95),\'yOff\':(-Js(0.65)),\'zOff\':(-Js(3.8)),\'xOrg\':Js(0.0),\'yOrg\':(-Js(0.3)),\'zOrg\':(-Js(2.8)),\'cLean\':Js(0.2),\'cRot\':Js(0.2),\'cDrop\':Js(0.1),\'jYMlt\':Js(0.2),\'inspectR\':Js(0.1),\'inspectM\':Js(1.9),\'muzOff\':Js(6.0),\'muzMlt\':Js(1.8),\'range\':Js(210.0),\'rate\':Js(400.0),\'innac\':Js(110.0),\'spread\':Js(120.0),\'shots\':Js(5.0),\'cSpread\':Js([Js(0.01), Js(0.05), (-Js(0.17)), (-Js(0.22)), (-Js(0.3)), Js(0.31), Js(0.32), Js(0.28), Js(0.3), (-Js(0.2))]),\'minSpread\':Js(20.0),\'zoom\':Js(1.25),\'leanMlt\':Js(1.6),\'recoil\':Js(0.02),\'recoilR\':Js(0.015),\'recover\':Js(0.99),\'recoverF\':Js(0.97),\'recoilZ\':Js(2.1),\'recoilZM\':Js(0.32),\'aimRecMlt\':Js(0.3),\'recoilYM\':Js(1.0),\'recoilAnim\':Js({\'time\':Js(340.0),\'recoilTweenY\':Js(0.35)}),\'jumpYM\':Js(0.5),\'rumble\':Js(0.8),\'icnPad\':Js(10.0),\'expScale\':Js(1.4)}), Js({\'name\':Js(\'Auto Pistol\'),\'src\':Js(\'weapon_17\'),\'icon\':Js(\'icon_17\'),\'sound\':Js(\'weapon_17\'),\'secondary\':Js(True),\'minRec\':Js(30.0),\'noAo\':Js(True),\'noHeadShot\':Js(True),\'kill\':Js([Js(\'\'), Js(50.0)]),\'type\':Js(1.0),\'swapTime\':Js(200.0),\'aimSpeed\':Js(100.0),\'spdMlt\':Js(1.0),\'ammo\':Js(12.0),\'reload\':Js(1000.0),\'dmg\':Js(15.0),\'pierce\':Js(0.95),\'dmgDrop\':Js(2.0),\'scale\':Js(0.0003158947055276376),\'leftHoldY\':(-Js(1.1)),\'rightHoldY\':(-Js(0.62)),\'leftHoldZ\':(-Js(0.3)),\'rightHoldZ\':(-Js(0.32)),\'rightHoldX\':Js(0.13),\'holdW\':Js(1.35),\'xOff\':Js(1.2),\'yOff\':(-Js(0.6)),\'zOff\':(-Js(3.7)),\'xOrg\':Js(0.0),\'yRot\':(-Js(0.005)),\'yOrg\':(-Js(0.23)),\'zOrg\':(-Js(3.9)),\'cLean\':Js(0.3),\'cRot\':Js(0.3),\'inspectR\':Js(0.35),\'inspectM\':Js(0.9),\'muzOff\':Js(2.0),\'muzMlt\':Js(1.1),\'range\':Js(700.0),\'rate\':Js(100.0),\'spread\':Js(150.0),\'jYMlt\':Js(0.5),\'zoom\':Js(1.3),\'leanMlt\':Js(1.6),\'recoil\':Js(0.005),\'recoilR\':Js(0.01),\'recover\':Js(0.98),\'recoverY\':Js(0.99),\'recoverF\':Js(0.98),\'recoilYM\':Js(0.2),\'aimRecMlt\':Js(0.4),\'recoilZ\':Js(3.8),\'recoilZM\':(-Js(0.4)),\'recoilAnim\':Js({\'time\':Js(200.0),\'recoilTweenY\':Js(0.28)}),\'rumble\':Js(0.8),\'icnPad\':(-Js(10.0)),\'expScale\':Js(1.55)})]))\nvar.put(\'v\', Js([Js({\'name\':Js(\'Triggerman\'),\'loadout\':Js([Js(1.0)]),\'secondary\':Js(True),\'colors\':Js([Js(10975328.0), Js(4013373.0), Js(2302755.0), Js(2631720.0), Js(7098434.0), Js(12566463.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.05)}), Js({\'name\':Js(\'Hunter\'),\'loadout\':Js([Js(0.0)]),\'secondary\':Js(True),\'colors\':Js([Js(10975328.0), Js(8083261.0), Js(6506290.0), Js(2631720.0), Js(6506290.0), Js(4008733.0)]),\'health\':Js(60.0),\'segs\':Js(5.0),\'speed\':Js(1.05)}), Js({\'name\':Js(\'Run N Gun\'),\'loadout\':Js([Js(3.0)]),\'colors\':Js([Js(10975328.0), Js(4088706.0), Js(3099491.0), Js(2631720.0), Js(6506290.0), Js(1715002.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.18)}), Js({\'name\':Js(\'Spray N Pray\'),\'loadout\':Js([Js(6.0)]),\'txts\':Js([Js(\'Calling in the Big Guns?\'), Js(\'Remember - No Russian.\'), Js(\'Pesky Snipers...\')]),\'colors\':Js([Js(10975328.0), Js(5793865.0), Js(4806204.0), Js(2631720.0), Js(2631720.0), Js(3160103.0)]),\'health\':Js(170.0),\'segs\':Js(7.0),\'regen\':Js(0.05),\'speed\':Js(0.95)}), Js({\'name\':Js(\'Vince\'),\'loadout\':Js([Js(5.0)]),\'txts\':Js([Js(\'...\')]),\'secondary\':Js(True),\'colors\':Js([Js(8412234.0), Js(5526119.0), Js(4144461.0), Js(2631720.0), Js(2631720.0), Js(2697267.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Detective\'),\'loadout\':Js([Js(4.0)]),\'txts\':Js([Js("I\'m onto something")]),\'colors\':Js([Js(10975328.0), Js(7360054.0), Js(4410462.0), Js(2631720.0), Js(6506290.0), Js(4140062.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Marksman\'),\'loadout\':Js([Js(7.0)]),\'secondary\':Js(True),\'colors\':Js([Js(10975328.0), Js(5793865.0), Js(4806204.0), Js(2631720.0), Js(2631720.0), Js(2699298.0)]),\'health\':Js(90.0),\'segs\':Js(6.0),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Rocketeer\'),\'loadout\':Js([Js(8.0)]),\'secondary\':Js(True),\'txts\':Js([Js(\'...\')]),\'colors\':Js([Js(10975328.0), Js(5793865.0), Js(4806204.0), Js(2631720.0), Js(7098434.0), Js(2831140.0)]),\'health\':Js(130.0),\'segs\':Js(7.0),\'speed\':Js(0.86)}), Js({\'name\':Js(\'Agent\'),\'loadout\':Js([Js(9.0)]),\'colors\':Js([Js(10975328.0), Js(4013373.0), Js(2302755.0), Js(2631720.0), Js(2631720.0), Js(12566463.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.2)}), Js({\'name\':Js(\'Runner\'),\'txts\':Js([Js(\'You sure about this?\'), Js(\'...\'), Js(\'Oh boy\'), Js("I don\'t know about this..."), Js(\'Not me again...\')]),\'loadout\':Js([Js(12.0)]),\'wallJ\':Js(True),\'colors\':Js([Js(10975328.0), Js(4013373.0), Js(2302755.0), Js(2631720.0), Js(2631720.0), Js(2302755.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'regen\':Js(0.2),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Deagler\'),\'hide\':Js(True),\'loadout\':Js([Js(10.0)]),\'colors\':Js([Js(10975328.0), Js(4013373.0), Js(2302755.0), Js(2631720.0), Js(2631720.0), Js(2302755.0)]),\'health\':Js(60.0),\'segs\':Js(5.0),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Bowman\'),\'loadout\':Js([Js(13.0)]),\'secondary\':Js(True),\'colors\':Js([Js(10975328.0), Js(9530450.0), Js(6308654.0), Js(2631720.0), Js(2631720.0), Js(4666663.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.0)}), Js({\'name\':Js(\'Commando\'),\'loadout\':Js([Js(14.0)]),\'secondary\':Js(True),\'colors\':Js([Js(10975328.0), Js(4013373.0), Js(2302755.0), Js(2631720.0), Js(10050604.0), Js(1513239.0)]),\'health\':Js(100.0),\'segs\':Js(6.0),\'speed\':Js(1.0)})]))\npass\npass\n')
exec("from js2py.pyjs import *\n# setting scope\nvar = Scope( JS_BUILTINS )\nset_global_object(var)\n\n# Code follows:\nvar.registers(['getListings', 'getPrice'])\n@Js\ndef PyJsHoisted_getPrice_(a, this, arguments, var=var):\n    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)\n    var.registers(['a'])\n    return (Js('https://krunker.io/social.html?p=itemsales&i=')+var.get('a').get('i'))\nPyJsHoisted_getPrice_.func_name = 'getPrice'\nvar.put('getPrice', PyJsHoisted_getPrice_)\n@Js\ndef PyJsHoisted_getListings_(a, this, arguments, var=var):\n    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)\n    var.registers(['a'])\n    return (Js('https://krunker.io/social.html?p=market&i=')+var.get('a').get('i'))\nPyJsHoisted_getListings_.func_name = 'getListings'\nvar.put('getListings', PyJsHoisted_getListings_)\nJs('use strict')\npass\npass\npass\n")
def getTexture(i):
    if "weapon" in i.keys():
        if "pat" in i.keys():
            return "weapons/pat/{}".format(i["pat"])
        elif "id" in i.keys():
            return "weapons/skins/weapon_{wp}_{id}".format(wp = i["weapon"], id = i["id"])
        elif "midT" in i.keys() and "mid" not in i.keys():
            return "weapons/skins/weapon_{wp}_{id}".format(wp = i["weapon"], id = i["midT"])
        elif "mid" in i.keys() and "midT" not in i.keys():
            return "weapons/weapon_{wp}_{id}".format(wp = i["weapon"], id = i["mid"])
        else:
            return "weapons/weapon_{wp}_{id}".format(wp = i["weapon"], id = i["midT"])
    if i["type"] == 3:
        if "pat" in i.keys():
            return "melee/melee_c{0}_weapons/pat/{0}".format(i["pat"])
        elif "id" in i.keys() and "tex" in i.keys():
            return "melee/melee_{id}_{tex}".format(id = i["id"], tex = i["tex"])
        elif "id" in i.keys():
            return "melee/melee_{id}".format(id = i["id"])

    if i["type"] == 1:
        return "hats/hat_{}".format(i["id"])
    if i["type"] == 7:
        if "id" in i.keys() and "tex" in i.keys():
            return "faces/face_{id}_{tex}".format(id = i["id"], tex = i["tex"])
        elif "id" in i.keys():
            return "faces/face_{}".format(i["id"])
    if i["type"] == 2:
        if "id" in i.keys() and "tex" in i.keys():
            return "body/body_{id}_{tex}".format(id = i["id"], tex = i["tex"])
        elif "id" in i.keys():
            return "body/body_{}".format(i["id"])


regions_ = ["North America",
            "South America",
            "Western Europe",
            "Africa",
            "Middle East",
            "Asia",
            "Oceania",
            "Eastern Europe"]

regions_x = [
            (150, 86),
            (231, 181),
            (366, 76),
            (366, 149),
            (410, 112),
            (500, 112),
            (564, 203),
            (453, 73)
            ]

region_abbr = {
            "na": "North America",
            "sa": "South America",
            "we": "Western Europe",
            "af": "Africa",
            "me": "Middle East",
            "as": "Asia",
            "oc": "Oceania",
            "eu": "Eastern Europe",
            "gb": "Global"}


asset_categories = ["Clutter","Decoration","Trees & Vegetation","Vehicles","Buildings","Furniture","Stones & Rubble","Technology","Weapons","Random & Strange","Tools","Food & Drink","Characters & Creatures","Fashion & Clothes","Game Map","Walls & Blocks", "Textures", "Triggers"]
map_categories = ["Other", "Parkour", "Puzzle", "Trading", "Training", "Social", "Horror", "Adventure",
                  "Battle Royale", "Realism", "Roleplay", "Rotation", "Racing", "Raid", "Remake", "NCR", "Zombies", "Simulation",
                  "Relaxation", "Action", "Tycoon", "Mini-Games"]
    
scales = {
    1: 6,
    2: 4,
    7: 20,  #vehicle
    8: 6,  #Stack
    15: 10,  #tree
    16: 4,   #cone
    17: 7,
    18: 32,
    19: 7,
    20: 4,
    21: 5,
    22: 6,
    23: 6,
    24: 5,
    25: 6,
    44: 1
}
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context()
ssl_context = ssl._create_unverified_context()
#cookies = pickle.load(open("cookies.pkl", "rb"))

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

def newTR(x = 30, y = 20, radius = 6):
    bimg = Image.new('RGB', (x, y), (140, 140, 140, 140))
    return add_corners(bimg, radius)
def tk(msg,val = 0):
    client.is_operating[msg.author.id] = val;
async def get_tk(msg, message_c = " Bot is already expecting a response from you."):
    try:
        if client.is_operating[msg.author.id]:
            await emb_send(msg.channel, warning + message_c, footer_t = "Please cancel all current operations, or wait for few mins and try again")
            return 1
        return 0
    except:
        return 0
def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue

def getIfromRGB(rgb):
    return (rgb[0]<<16) + (rgb[1]<<8) + rgb[2]


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


def outline_image(img, filter_c = (0, 255, 0)):
    old_ = img.copy()
    img = img.convert("RGB")
    main = Image.new('RGB', (img.width+4,img.height+4), (255, 255, 255))
    main.paste(img, (1, 1))
    img = main
    pixels = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            p_c = list(pixels[x, y])
            if p_c[:3] != [0, 0, 0]:
                pixels[x, y] = (255, 255, 255)
    img = img.filter(ImageFilter.FIND_EDGES)
    img = ImageOps.invert(img)
    width, height = img.size
    img = img.crop((1, 1, width-3, height-3))
    #main = Image.new('RGB', (img.width+2,img.height+2), (255, 255, 255))
    #main.paste(img, (1, 1))
    #img = main
    old_pixels = old_.load()
    pixels = img.load()
    new_img =  img.copy()
    new_pixels = new_img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            p_c = list(new_pixels[x, y])
            if p_c[:3] == [0, 0, 0]:
                if old_pixels[x, y] == filter_c:new_pixels[x, y] = (255, 255, 255)
                
    return new_img

def get_axis_val(val):
    out = math.radians((90-math.degrees(val))*2)
    #out = math.radians(180-math.degrees(val))
    return val + out
    if val > 0:
        return val + out
    else:return val - out

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
a_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "Upgrade",
        "Host": "krunker_social.krunker.io",
        "Origin": "https://internal.krunker.io",
        "Pragma": "no-cache",
        "Upgrade": "websocket",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",

}


map_file = "Data/maps.bt"
mod_file = "Data/mods.bt"
plays_img = "Data/plays.png"
likes_img = "Data/likes.png"
likes2_img = "Data/likesv2.png"
verif_img = "Data/verification.png"
partn_img = "Data/partner.png"
prem_img = "Data/premium.png"
font_file = "Data/font2.ttf"
temp_img = "Data/bgs/tem1.png"
pfp_id_file = "Data/profileIDS.bt"
krunker_matchmaker_path = "https://krunker_matchmaker.krunker.io/game-list?hostname=krunker.io"
map_thumb_url = "https://user-assets.krunker.io/m{}/thumb.png?v=5"
api_maps_url = "https://api.krunker.io/maps?index=5&pos=0&accountId="
graph_data_file = "Data/graph.bt"
featured_maps_file = "Data/featured.bt"
sweep_file = "Data/sweep.bt"
prefix = "g."

__rarities = {"0": 8185428,
            "1": 1014015,
            "2": 13244869,
            "3": 16761856,
            "4": 13047834,
            "5": 4276545,
            "6": 1}
gamemodes = [
    "Free for All",
    "Team Deathmatch",
    "Hardpoint",
    "Capture the Flag",
    "Parkour",
    "Hide & Seek",
    "Infected",
    "Race",
    "Last Man Standing",
    "Simon Says",
    "Gun Game",
    "Prop Hunt",
    "Boss Hunt",
    "Ranked",
    "Ranked",
    "Stalker",
    "King of the Hill",
    "One in the Chamber",
    "Trade",
    "Kill Confirmed",
    "Diffuse",
    "Sharp Shooter",
    "Traitor",
    "Raid",
    "Blitz"
]

bot_logo = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024"
star_emote = "⭐ "
gb_emote = "<:GameBot:751968732057698377>"
globe_emote = ":globe_with_meridians:"
game_data_sample = """
`{}`: [{} / {}](https://krunker.io/?game={}) *@ {}*"""
Main_Color = (227, 126, 255)

Countries = [["af", -96, 0], ["al", -192, 0], ["dz", -320, -96], ["as", -352, 0], ["ad", -32, 0], ["ao", -288, 0], ["ai", -160, 0], None, ["ag", -128, 0], ["ar", -320, 0], ["am", -224, 0], ["aw", -448, 0], ["au", -416, 0], ["at", -384, 0], ["az", 0, -32], ["bs", -480, -32], ["bh", -224, -32], ["bd", -96, -32], ["bb", -64, -32], ["by", -64, -64], ["be", -128, -32], ["bz", -96, -64], ["bj", -288, -32], ["bm", -352, -32], ["bt", 0, -64], ["bo", -416, -32], ["ba", -32, -32], ["bw", -32, -64], ["br", -448, -32], None, ["vg", -192, -448], ["bn", -384, -32], ["bg", -192, -32], ["bf", -160, -32], ["bi", -256, -32], ["kh", 0, -224], ["cm", -384, -64], ["ca", -128, -64], ["cv", -32, -96], ["ky", -224, -224], ["cf", -192, -64], ["td", -480, -384], ["cl", -352, -64], ["cn", -416, -64], None, None, ["co", -448, -64], ["km", -64, -224], ["ck", -320, -64], ["cr", -480, -64], ["hr", -416, -160], ["cu", 0, -96], ["cw", -64, -96], ["cy", -96, -96], ["cz", -128, -96], ["cd", -160, -64], ["dk", -224, -96], ["dj", -192, -96], ["dm", -256, -96], ["do", -288, -96], ["tl", -160, -416], ["ec", -352, -96], ["eg", -416, -96], ["sv", -352, -384], ["gq", -128, -160], ["er", -480, -96], ["ee", -384, -96], ["et", -32, -128], ["fk", -160, -128], ["fo", -224, -128], ["fj", -128, -128], ["fi", -96, -128], ["fr", -256, -128], ["pf", -320, -320], ["ga", -288, -128], ["gm", -32, -160], ["ge", -384, -128], ["de", -160, -96], ["gh", -448, -128], ["gi", -480, -128], ["gr", -160, -160], ["gl", 0, -160], ["gd", -352, -128], ["gu", -256, -160], ["gt", -224, -160], ["gg", -416, -128], ["gn", -64, -160], ["gw", -288, -160], ["gy", -320, -160], ["ht", -448, -160], ["hn", -384, -160], ["hk", -352, -160], ["hu", -480, -160], ["is", -256, -192], ["in", -160, -192], ["id", -32, -192], ["ir", -224, -192], ["iq", -192, -192], ["ie", -64, -192], ["im", -128, -192], ["il", -96, -192], ["it", -288, -192], ["ci", -288, -64], ["jm", -352, -192], ["jp", -416, -192], ["je", -320, -192], ["jo", -384, -192], ["kz", -256, -224], ["ke", -448, -192], ["ki", -32, -224], None, ["kw", -192, -224], ["kg", -480, -192], ["la", -288, -224], ["lv", -64, -256], ["lb", -320, -224], ["ls", -480, -224], ["lr", -448, -224], ["ly", -96, -256], ["li", -384, -224], ["lt", 0, -256], ["lu", -32, -256], ["mo", -480, -256], ["mk", -352, -256], ["mg", -288, -256], ["mw", -224, -288], ["my", -288, -288], ["mv", -192, -288], ["ml", -384, -256], ["mt", -128, -288], ["mh", -320, -256], ["mr", -64, -288], ["mu", -160, -288], ["yt", -416, -448], ["mx", -256, -288], ["fm", -192, -128], ["md", -192, -256], ["mc", -160, -256], ["mn", -448, -256], ["me", -224, -256], ["ms", -96, -288], ["ma", -128, -256], ["mz", -320, -288], ["mm", -416, -256], ["na", -352, -288], ["nr", -128, -320], ["np", -96, -320], ["nl", -32, -320], ["an", -256, 0], ["nc", -384, -288], ["nz", -192, -320], ["ni", 0, -320], ["ne", -416, -288], ["ng", -480, -288], ["nu", -160, -320], ["kp", -128, -224], ["mp", 0, -288], ["no", -64, -320], ["om", -224, -320], ["pk", -416, -320], ["pw", -96, -352], ["ps", -32, -352], ["pa", -256, -320], ["pg", -352, -320], ["py", -128, -352], ["pe", -288, -320], ["ph", -384, -320], ["pn", -480, -320], ["pl", -448, -320], ["pt", -64, -352], ["pr", 0, -352], ["qa", -160, -352], ["cg", -224, -64], ["re", -192, -352], ["ro", -224, -352], ["ru", -288, -352], ["rw", -320, -352], ["bl", -320, -32], ["sh", -32, -384], ["kn", -96, -224], ["lc", -352, -224], ["mf", -256, -256], None, ["vc", -128, -448], ["ws", -352, -448], ["sm", -160, -384], ["st", -320, -384], ["sa", -352, -352], ["sn", -192, -384], ["rs", -256, -352], ["sc", -416, -352], ["sl", -128, -384], ["sg", 0, -384], None, ["sk", -96, -384], ["si", -64, -384], ["sb", -384, -352], ["so", -224, -384], ["za", -448, -448], ["kr", -160, -224], ["ss", -288, -384], ["es", 0, -128], ["lk", -416, -224], ["sd", -448, -352], ["sr", -256, -384], None, ["sz", -416, -384], ["se", -480, -352], ["ch", -256, -64], ["sy", -384, -384], ["tw", -384, -416], ["tj", -96, -416], ["tz", -416, -416], ["th", -64, -416], ["tg", -32, -416], ["tk", -128, -416], ["to", -256, -416], ["tt", -320, -416], ["tn", -224, -416], ["tr", -288, -416], ["tm", -192, -416], ["tc", -448, -384], ["tv", -352, -416], ["vi", -224, -448], ["ug", -480, -416], ["ua", -448, -416], ["ae", -64, 0], ["gb", -320, -128], ["us", 0, -448], ["uy", -32, -448], ["uz", -64, -448], ["vu", -288, -448], ["va", -96, -448], ["ve", -160, -448], ["vn", -256, -448], ["wf", -320, -448], ["eh", -448, -96], ["ye", -384, -448], ["zm", -480, -448], ["zw", 0, -480]]
Countries_names = [['Afghanistan', 'af', 0], ['Albania', 'al', 1], ['Algeria', 'dz', 2], ['American Samoa', 'as', 3], ['Andorra', 'ad', 4], ['Angola', 'ao', 5], ['Anguilla', 'ai', 6], ['Antarctica', 'aq', 7], ['Antigua and Barbuda', 'ag', 8], ['Argentina', 'ar', 9], ['Armenia', 'am', 10], ['Aruba', 'aw', 11], ['Australia', 'au', 12], ['Austria', 'at', 13], ['Azerbaijan', 'az', 14], ['Bahamas', 'bs', 15], ['Bahrain', 'bh', 16], ['Bangladesh', 'bd', 17], ['Barbados', 'bb', 18], ['Belarus', 'by', 19], ['Belgium', 'be', 20], ['Belize', 'bz', 21], ['Benin', 'bj', 22], ['Bermuda', 'bm', 23], ['Bhutan', 'bt', 24], ['Bolivia', 'bo', 25], ['Bosnia and Herzegovina', 'ba', 26], ['Botswana', 'bw', 27], ['Brazil', 'br', 28], ['British Indian Ocean Territory', 'io', 29], ['British Virgin Islands', 'vg', 30], ['Brunei', 'bn', 31], ['Bulgaria', 'bg', 32], ['Burkina Faso', 'bf', 33], ['Burundi', 'bi', 34], ['Cambodia', 'kh', 35], ['Cameroon', 'cm', 36], ['Canada', 'ca', 37], ['Cape Verde', 'cv', 38], ['Cayman Islands', 'ky', 39], ['Central African Republic', 'cf', 40], ['Chad', 'td', 41], ['Chile', 'cl', 42], ['China', 'cn', 43], ['Christmas Island', 'cx', 44], ['Cocos Islands', 'cc', 45], ['Colombia', 'co', 46], ['Comoros', 'km', 47], ['Cook Islands', 'ck', 48], ['Costa Rica', 'cr', 49], ['Croatia', 'hr', 50], ['Cuba', 'cu', 51], ['Curacao', 'cw', 52], ['Cyprus', 'cy', 53], ['Czech Republic', 'cz', 54], ['Democratic Republic of the Congo', 'cd', 55], ['Denmark', 'dk', 56], ['Djibouti', 'dj', 57], ['Dominica', 'dm', 58], ['Dominican Republic', 'do', 59], ['East Timor', 'tl', 60], ['Ecuador', 'ec', 61], ['Egypt', 'eg', 62], ['El Salvador', 'sv', 63], ['Equatorial Guinea', 'gq', 64], ['Eritrea', 'er', 65], ['Estonia', 'ee', 66], ['Ethiopia', 'et', 67], ['Falkland Islands', 'fk', 68], ['Faroe Islands', 'fo', 69], ['Fiji', 'fj', 70], ['Finland', 'fi', 71], ['France', 'fr', 72], ['French Polynesia', 'pf', 73], ['Gabon', 'ga', 74], ['Gambia', 'gm', 75], ['Georgia', 'ge', 76], ['Germany', 'de', 77], ['Ghana', 'gh', 78], ['Gibraltar', 'gi', 79], ['Greece', 'gr', 80], ['Greenland', 'gl', 81], ['Grenada', 'gd', 82], ['Guam', 'gu', 83], ['Guatemala', 'gt', 84], ['Guernsey', 'gg', 85], ['Guinea', 'gn', 86], ['Guinea-Bissau', 'gw', 87], ['Guyana', 'gy', 88], ['Haiti', 'ht', 89], ['Honduras', 'hn', 90], ['Hong Kong', 'hk', 91], ['Hungary', 'hu', 92], ['Iceland', 'is', 93], ['India', 'in', 94], ['Indonesia', 'id', 95], ['Iran', 'ir', 96], ['Iraq', 'iq', 97], ['Ireland', 'ie', 98], ['Isle of Man', 'im', 99], ['Israel', 'il', 100], ['Italy', 'it', 101], ['Ivory Coast', 'ci', 102], ['Jamaica', 'jm', 103], ['Japan', 'jp', 104], ['Jersey', 'je', 105], ['Jordan', 'jo', 106], ['Kazakhstan', 'kz', 107], ['Kenya', 'ke', 108], ['Kiribati', 'ki', 109], ['Kosovo', 'xk', 110], ['Kuwait', 'kw', 111], ['Kyrgyzstan', 'kg', 112], ['Laos', 'la', 113], ['Latvia', 'lv', 114], ['Lebanon', 'lb', 115], ['Lesotho', 'ls', 116], ['Liberia', 'lr', 117], ['Libya', 'ly', 118], ['Liechtenstein', 'li', 119], ['Lithuania', 'lt', 120], ['Luxembourg', 'lu', 121], ['Macau', 'mo', 122], ['Macedonia', 'mk', 123], ['Madagascar', 'mg', 124], ['Malawi', 'mw', 125], ['Malaysia', 'my', 126], ['Maldives', 'mv', 127], ['Mali', 'ml', 128], ['Malta', 'mt', 129], ['Marshall Islands', 'mh', 130], ['Mauritania', 'mr', 131], ['Mauritius', 'mu', 132], ['Mayotte', 'yt', 133], ['Mexico', 'mx', 134], ['Micronesia', 'fm', 135], ['Moldova', 'md', 136], ['Monaco', 'mc', 137], ['Mongolia', 'mn', 138], ['Montenegro', 'me', 139], ['Montserrat', 'ms', 140], ['Morocco', 'ma', 141], ['Mozambique', 'mz', 142], ['Myanmar', 'mm', 143], ['Namibia', 'na', 144], ['Nauru', 'nr', 145], ['Nepal', 'np', 146], ['Netherlands', 'nl', 147], ['Netherlands Antilles', 'an', 148], ['New Caledonia', 'nc', 149], ['New Zealand', 'nz', 150], ['Nicaragua', 'ni', 151], ['Niger', 'ne', 152], ['Nigeria', 'ng', 153], ['Niue', 'nu', 154], ['North Korea', 'kp', 155], ['Northern Mariana Islands', 'mp', 156], ['Norway', 'no', 157], ['Oman', 'om', 158], ['Pakistan', 'pk', 159], ['Palau', 'pw', 160], ['Palestine', 'ps', 161], ['Panama', 'pa', 162], ['Papua New Guinea', 'pg', 163], ['Paraguay', 'py', 164], ['Peru', 'pe', 165], ['Philippines', 'ph', 166], ['Pitcairn', 'pn', 167], ['Poland', 'pl', 168], ['Portugal', 'pt', 169], ['Puerto Rico', 'pr', 170], ['Qatar', 'qa', 171], ['Republic of the Congo', 'cg', 172], ['Reunion', 're', 173], ['Romania', 'ro', 174], ['Russia', 'ru', 175], ['Rwanda', 'rw', 176], ['Saint Barthelemy', 'bl', 177], ['Saint Helena', 'sh', 178], ['Saint Kitts and Nevis', 'kn', 179], ['Saint Lucia', 'lc', 180], ['Saint Martin', 'mf', 181], ['Saint Pierre and Miquelon', 'pm', 182], ['Saint Vincent and the Grenadines', 'vc', 183], ['Samoa', 'ws', 184], ['San Marino', 'sm', 185], ['Sao Tome and Principe', 'st', 186], ['Saudi Arabia', 'sa', 187], ['Senegal', 'sn', 188], ['Serbia', 'rs', 189], ['Seychelles', 'sc', 190], ['Sierra Leone', 'sl', 191], ['Singapore', 'sg', 192], ['Sint Maarten', 'sx', 193], ['Slovakia', 'sk', 194], ['Slovenia', 'si', 195], ['Solomon Islands', 'sb', 196], ['Somalia', 'so', 197], ['South Africa', 'za', 198], ['South Korea', 'kr', 199], ['South Sudan', 'ss', 200], ['Spain', 'es', 201], ['Sri Lanka', 'lk', 202], ['Sudan', 'sd', 203], ['Suriname', 'sr', 204], ['Svalbard and Jan Mayen', 'sj', 205], ['Swaziland', 'sz', 206], ['Sweden', 'se', 207], ['Switzerland', 'ch', 208], ['Syria', 'sy', 209], ['Taiwan', 'tw', 210], ['Tajikistan', 'tj', 211], ['Tanzania', 'tz', 212], ['Thailand', 'th', 213], ['Togo', 'tg', 214], ['Tokelau', 'tk', 215], ['Tonga', 'to', 216], ['Trinidad and Tobago', 'tt', 217], ['Tunisia', 'tn', 218], ['Turkey', 'tr', 219], ['Turkmenistan', 'tm', 220], ['Turks and Caicos Islands', 'tc', 221], ['Tuvalu', 'tv', 222], ['U.S. Virgin Islands', 'vi', 223], ['Uganda', 'ug', 224], ['Ukraine', 'ua', 225], ['United Arab Emirates', 'ae', 226], ['United Kingdom', 'gb', 227], ['United States', 'us', 228], ['Uruguay', 'uy', 229], ['Uzbekistan', 'uz', 230], ['Vanuatu', 'vu', 231], ['Vatican', 'va', 232], ['Venezuela', 've', 233], ['Vietnam', 'vn', 234], ['Wallis and Futuna', 'wf', 235], ['Western Sahara', 'eh', 236], ['Yemen', 'ye', 237], ['Zambia', 'zm', 238], ['Zimbabwe', 'zw', 239]]
classes = [{'name': 'Triggerman', 'loadout': [1], 'secondary': 1, 'colors': [10975328, 4013373, 2302755, 2631720, 7098434, 12566463], 'health': 100, 'segs': 6, 'speed': 1.05, 'wp':'Assult Rifle'}, {'name': 'Hunter', 'loadout': [0], 'secondary': 1, 'colors': [10975328, 8083261, 6506290, 2631720, 6506290, 4008733], 'health': 60, 'segs': 5, 'speed': 1.05, 'wp': 'Sniper Rifle'}, {'name': 'Run N Gun', 'loadout': [3], 'wallJ': 1, 'colors': [10975328, 4088706, 3099491, 2631720, 6506290, 1715002], 'health': 100, 'segs': 6, 'speed': 1.18, 'wp': 'Submachine Gun'}, {'name': 'Spray N Pray', 'loadout': [6], 'txts': ['Calling in the Big Guns?', 'Remember - No Russian.', 'Pesky Snipers...'], 'colors': [10975328, 5793865, 4806204, 2631720, 2631720, 3160103], 'health': 170, 'segs': 7, 'regen': 0.05, 'speed': 0.95, 'wp': 'Machine Gun'}, {'name': 'Vince', 'loadout': [5], 'txts': ['...'], 'secondary': 1, 'colors': [8412234, 5526119, 4144461, 2631720, 2631720, 2697267], 'health': 90, 'segs': 6, 'speed': 1, 'wp': 'Shotgun'}, {'name': 'Detective', 'loadout': [4], 'txts': ["I'm onto something"], 'colors': [10975328, 7360054, 4410462, 2631720, 6506290, 4140062], 'health': 100, 'segs': 6, 'speed': 1, 'wp': 'Revolver'}, {'name': 'Marksman', 'loadout': [7], 'secondary': 1, 'colors': [10975328, 5793865, 4806204, 2631720, 2631720, 2699298], 'health': 90, 'segs': 6, 'speed': 1, 'wp': 'Semi Auto'}, {'name': 'Rocketeer', 'loadout': [8], 'secondary': 1, 'txts': ['...'], 'colors': [10975328, 5793865, 4806204, 2631720, 7098434, 2831140], 'health': 130, 'segs': 7, 'speed': 0.86, 'wp': 'Rocket Launcher'}, {'name': 'Agent', 'loadout': [9], 'wallJ': 1, 'colors': [10975328, 4013373, 2302755, 2631720, 2631720, 12566463], 'health': 100, 'segs': 6, 'speed': 1.2, 'wp': 'Akimbo Uzi'}, {'name': 'Runner', 'txts': ['You sure about this?', '...', 'Oh boy', "I don't know about this...", 'Not me again...'], 'loadout': [12], 'wallJ': 1, 'colors': [10975328, 4013373, 2302755, 2631720, 2631720, 2302755], 'health': 120, 'segs': 6, 'regen': 0.2, 'speed': 1, 'wp': 'Knife'}, {'name': 'Deagler', 'hide': 1, 'loadout': [10], 'colors': [10975328, 4013373, 2302755, 2631720, 2631720, 2302755], 'health': 60, 'segs': 5, 'speed': 1, 'wp': 'Deagle'}, {'name': 'Bowman', 'loadout': [13], 'secondary': 1, 'colors': [10975328, 9530450, 6308654, 2631720, 2631720, 4666663], 'health': 100, 'segs': 6, 'speed': 1, 'wp': 'Crossbow'}, {'name': 'Commando', 'loadout': [14], 'secondary': 1, 'colors': [10975328, 4013373, 2302755, 2631720, 10050604, 1513239], 'health': 100, 'segs': 6, 'speed': 1, 'wp': 'Famas'}, {'name': 'Trooper', 'wallJ': 1, 'loadout': [18], 'colors': [10975328, 12436169, 12436169, 3026478, 2631720, 3026478], 'health': 100, 'segs': 6, 'speed': 1,'wp': 'Blaster'}]
sclasses = [{'name': 'Triggerman', 'wp':'Assult Rifle'}, {'name': 'Hunter', 'wp': 'Sniper Rifle'}, {'name': 'Run N Gun', 'wp': 'Submachine Gun'}, {'name': 'Spray N Pray', 'wp': 'Machine Gun'}, {'name': 'Vince', 'wp': 'Shotgun'}, {'name': 'Detective', 'wp': 'Revolver'}, {'name': 'Marksman', 'wp': 'Semi Auto'}, {'name': 'Rocketeer', 'wp': 'Rocket Launcher'}, {'name': 'Agent', 'wp': 'Akimbo Uzi'}, {'name': 'Runner', 'wp': 'Knife'}, {'name': 'Bowman', 'wp': 'Crossbow'}, {'name': 'Commando', 'wp': 'Famas'}, {'name': 'Trooper', 'wp': 'Blaster'}]
sclasses_names = [e_c["name"].lower() for e_c in sclasses]
skin_types = {
    1:" hat",
    2:" back",
    5:" dye",
    6:" waist",
    7:" face",
    8:" shoe"}
    
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

def generate_colored_text(x, y, text, font, mdraw):
    overall_off = x
    rainbow_colors = [(230, 0, 0), (0, 230, 0), (0, 0, 230), (200, 0, 200), (229, 235, 52), (252, 3, 132)]
    for x, e_letter in enumerate(text):
        mdraw.text((overall_off, y), e_letter, font=font, fill=rainbow_colors[x])
        overall_off += get_text_size(e_letter, font) + 2
    return overall_off-x

def draw_non_acsii(x, y, text, font, unic_font, color, mdraw, stroke = 0, stroke_fill = None, stroke_width = 0):
    overall_off = x
    for x, e_letter in enumerate(text):
        if e_letter.isascii():
            mdraw.text((overall_off, y), e_letter, font=font, fill=color, stroke_fill = stroke_fill, stroke_width = stroke_width)
            overall_off += get_text_size(e_letter, font) + 2
        else:
            mdraw.text((overall_off, y), e_letter, font=unic_font, fill=color, stroke_fill = stroke_fill, stroke_width = stroke_width)
            overall_off += get_text_size(e_letter, unic_font) + 3
        
    return overall_off-x

def cal_non_acsii(text, font, unic_font):
    overall_off = 0
    for x, e_letter in enumerate(text):
        if e_letter.isascii():
            overall_off += get_text_size(e_letter, font) + 2
        else:
            overall_off += get_text_size(e_letter, unic_font) + 3
        
    return overall_off


def command_check(cmd, guild, space__ = True):
    if guild == None:return cmd
    
client.dismiss_ = False
client.efavs_r = {}
client.map_files = {}
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def tint_image(src, color="#FF0000", brightness = 1.45):
    src.load()
    r, g, b, alpha = src.split()
    gray = ImageOps.grayscale(src)
    result = ImageOps.colorize(gray, (0, 0, 0, 0), color) 
    result.putalpha(alpha)
    enhancer = ImageEnhance.Brightness(result)
    result = enhancer.enhance(brightness)
    return result
def make_maps(maps, user_name, last_timestamp, plays, last_plays, main_pages, filter_color, filter_votes, filter_votes_2, get_cord, final_maps, start, get_x_val, total_likes, current_page, indv_plays, is_verified, mid_maps):
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(maps) * (31 + 2)
    y += offset + 40 + 5 + 50 + 60 + 15
    img = Image.new('RGBA', (680,y), (0, 0, 0, 0))
    #img = newGrad((630, y))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = client.main_font3
    font_size += 12
    heading_color = (179, 179, 179)
    def title_Stuff():
        profile_offset = 0
        if is_verified:
            img.paste(client.verif2, (18, 15), client.verif2)
            profile_offset = client.verif2.width+7
        outline_text(draw, 18+profile_offset, 15, (255, 255, 255), (0, 0, 0), user_name+"'s Maps", font2)
        draw.text((130+15, y-45-3), "Last Cached", (74, 77, 84), font=client.font)
        if last_timestamp:
            cached_stamp = ago.human(datetime.timedelta(seconds = int(time.time() - last_timestamp)), precision = 2,
                                       future_tense = "{} ago", abbreviate = True)
        else:
            cached_stamp = "unknown"
        stamp_x = int(draw.textsize(cached_stamp, client.font)[0]/2)
        cached_x = int(draw.textsize("Last Cached", client.font)[0]/2)
        
        draw.text(((130+cached_x)-stamp_x+15, y-45+22-3),cached_stamp,
                  (74, 77, 84), font = client.font)
        #last_timestamp
        if main_pages > 1: outline_text(draw, 450, 22, heading_color, (0, 0, 0), "Page # {}/{}".format(current_page, main_pages), font)
        outline_text(draw, 18, 60, heading_color, (0, 0, 0), "Map Name", font3)
        outline_text(draw, 313, 60, heading_color, (0, 0, 0), "Plays", font3)
        outline_text(draw, 523, 60, heading_color, (0, 0, 0), "Likes", font3)
        draw.line((15, 100, 600+20+30, 100), (74, 77, 84), 4)
    offset = 44
    tsthr = threading.Thread(target = title_Stuff, args = ())
    tsthr.start()
    draw.line((52, 101, 52, y-75), (74, 77, 84), 3)

    def each_map_stuff(x, e_map):
        def name_pla():
            outline_text(draw, 53+10, 12+((font_size+4)*x)+offset+ 60, filter_color(e_map['map_featured']), (0, 0, 0), e_map["map_name"], font)
            outline_text(draw, 280+30, 12+((font_size+4)*x)+offset+ 60, black_color, (0, 0, 0), '{:,}'.format(e_map["map_pl"]), font)
        def likes():
            try:
                new_plays = e_map["map_pl"] - indv_plays[e_map["map_name"].lower()]
                if new_plays < 0:new_plays = 0
                x_, color, abbr, abbr2, votes = filter_votes(new_plays)
            except:
                x_, color, abbr, abbr2, votes = filter_votes(0)
            draw.text((383+x_+30, 12+((font_size+4)*x)+offset+ 60), abbr+'{:,}'.format(votes), color, font=client.font15)
            outline_text(draw, 490+30, 12+((font_size+4)*x)+offset+ 60, black_color, (0, 0, 0), '{:,}'.format(e_map["map_votes"]), font)
            x_, color, abbr, abbr2, votes = filter_votes_2(final_maps[x+start][2])
            draw.text((575+x_+30, 12+(((font_size+4))*x)+offset+60),abbr+str(votes)+abbr2,color,font=client.font15)
        npthr = threading.Thread(target = name_pla, args = ())
        npthr.start()
        lthr = threading.Thread(target = likes, args = ())
        lthr.start()
        lthr.join()
        npthr.join()
    def download_thumbs(x, e_map):
        try:
            response = requests.get("https://user-assets.krunker.io/m{}/thumb.png?v=80".format(mid_maps[e_map['map_name']]))
            thumb = Image.open(BytesIO(response.content)).convert("RGBA")
            profile_icon = thumb.resize((31,21)).convert("RGBA")
        except:
            profile_icon = client.unknown
        img.paste(profile_icon, (10, 12+((font_size+4)*x)+offset+60), profile_icon)
            
        
    em_thr = []
    emt_thr = []
    for x, e_map in enumerate(maps):
        ems = threading.Thread(target = each_map_stuff, args = (x, e_map))
        ems.start()
        em_thr.append(ems)
        ems = threading.Thread(target = download_thumbs, args = (x, e_map))
        ems.start()
        emt_thr.append(ems)
    def bottom_stuff():
        draw.line((15, y-57-6, 600+20+30, y-57-6), (43, 44, 47), 4)
        outline_text(draw, 18, y-45, (220, 220, 220) , (0, 0, 0), "Total", font2)

        outline_text(draw, 278+30, y-45, (220, 220, 220) , (0, 0, 0), '{:,}'.format(plays), font)
        twidth, _ = draw.textsize('{:,}'.format(plays), font)
        x_, color, abbr, abbr2, votes = filter_votes(plays - last_plays[0])
        twidth2, _ = draw.textsize(abbr +'{:,}'.format(votes), client.font15)
        total_new_likes = sum([e_map[2] for e_map in final_maps])
        
        w_t_s_x = get_cord(plays - last_plays[0])
        if not votes:
            x_pre = 429
        else:
            x_pre = twidth+278+(((487-(twidth+278))/2)-(twidth2/2))+30
        draw.text((x_pre, y-45), abbr +'{:,}'.format(votes), color, font=client.font15)
        outline_text(draw, 487+30, y-45, (220, 220, 220) , (0, 0, 0), '{:,}'.format(total_likes), font)
        x_, color, abbr, abbr2, votes = filter_votes(total_new_likes)
        w_t_s_x = 615 if (total_new_likes) != 0 else 600
        draw.text((w_t_s_x-get_x_val(draw, abbr +'{:,}'.format(votes), font)+30, y-45), abbr +'{:,}'.format(votes), color, font=client.font15)
    btthr = threading.Thread(target = bottom_stuff, args = ())
    btthr.start()
    
    ngb_logo = client.gb
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
    for e_t in em_thr:
        e_t.join()
    for e_t in emt_thr:
        e_t.join()
        
    tsthr.join()
    btthr.join()
    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2))
    dark_img.paste(img, (0, 0), img)
    
    gr_img = newGrad((680, y))#, (60, 60, 60), (30, 30, 30))
    gr_img.paste(dark_img, (0, 0), dark_img)
    gr_img = classic_outline(gr_img)

    byte_io = BytesIO()
    byte_io.seek(0)
    gr_img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io

def get_level_int_c(chl, Level_ = None, def_c = (255, 255, 255)):
    if Level_ == None:
        Level_ = int(str(chl if chl >= 1 else 0).replace("None", "0"))
    if Level_ >= 10 and Level_ <= 14:return Level_, (251, 148, 45)
    elif Level_ >= 15 and Level_ <= 19:return Level_, (193, 45, 251)
    elif Level_ >= 20:return Level_, (251, 45, 45)
    else:return Level_, def_c
    

def generate_pf(data, stats, user_name, is_applying, mdata, application, muser, bg_confs = 0):
    def change_color_(r, g, b, img):
        if not sum((r, g, b)):
            return ImageEnhance.Brightness(img).enhance(0)
        else:
            pixels = img.load() # create the pixel map

            for i in range(img.size[0]): # for every pixel:
                for j in range(img.size[1]):
                    pixels[i, j] = (r, g, b, list(pixels[i, j])[-1])
    value_c = (255, 255, 255)
    main_c = (191, 176, 190)
    foot_c = (170, 170, 170)
    #main_c = (204, 176, 255)
    main_c = (227, 126, 255)
    User_Text = (227, 126, 255)
    has_bg = 0
    put_overlay = -1
    motto = ""
    is_default = False
    if not bg_confs:
        if data['player_name'].lower() == "transparent":
            pbimg = Image.new('RGBA', (719, 464), (0, 0, 0, 0))
            bar_color = User_Text
            has_bg = 1
            is_default = True
            t_shadows = 1
            logo_color = 0; borders = {}
        for e_p in client.bgs["p"]:
            if e_p["cm"].lower() == data['player_name'].lower():
                pbimg = e_p["file"]
                main_c = e_p["hd"]
                User_Text = e_p["ut"]
                bar_color = e_p["xp"]
                try:put_overlay = e_p["bglay"]
                except:put_overlay = 0
                try:motto = e_p["txt"]
                except:motto = ""
                try:logo_color = e_p["lgc"]
                except:logo_color = 0
                try:borders = e_p["brd"]
                except:borders = {}
                has_bg = 1
        if not has_bg:
            for e_p in client.bgs["c"]:
                if e_p["cm"].lower() == data['player_clan'].lower():
                    pbimg = e_p["file"]
                    main_c = e_p["hd"]
                    User_Text = e_p["ut"]
                    bar_color = e_p["xp"]
                    try:put_overlay = e_p["bglay"]
                    except:put_overlay = 0
                    try:motto = e_p["txt"]
                    except:motto = ""
                    try:logo_color = e_p["lgc"]
                    except:logo_color = 0
                    try:borders = e_p["brd"]
                    except:borders = {}
                    has_bg = 1
        
        if not has_bg:
            pbimg = random.choice(client.default_bg)
            bar_color = User_Text
            is_default = True
            t_shadows = 1
            logo_color = 0
            borders = {}
    else:
        pbimg = bg_confs["bg"]
        main_c = bg_confs["hd"]
        User_Text = bg_confs["ut"]
        bar_color = bg_confs["xp"]
        try:put_overlay = bg_confs["bglay"]
        except:put_overlay = 0
        try:motto = bg_confs["txt"]
        except:motto = ""
        try:logo_color = bg_confs["lgc"]
        except:logo_color = 0
        try:borders = bg_confs["brd"]
        except:borders = {}
        has_bg = 1
    t_shadows = 1
    if not borders:
        borders = {"shd":0, "outl":0, "clr": 0, "xpb":0}
    img = Image.new('RGBA', (719, 464), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = client.font
    font2 = client.font2
    font3 = client.font3
    font4 = client.font4
    font5 = client.font5
    font6 = client.font6
    unicode_font = client.unicode_font
    def vldr(text, pixel, font=font):
        twidth, _ = draw.textsize(text, font=font)
        return pixel -  int(twidth/2)

    def custom_out(xy, text_, main_c, font, outline = (0, 0, 0)):
        outline_text(draw, xy[0], xy[1], main_c, outline, text_, font)    
    def drawtext(draw, xy, text, value_c, font, outline_c = (0, 0, 0)):
        outline_text(draw, xy[0], xy[1], value_c, outline_c, text, font)

    def put_username(img, stats, user_name, User_Text, data):        
        outline_text(draw, 135, 15, User_Text, (0, 0, 0), data['player_name'], font2)
    username_th = threading.Thread(target = put_username, args = (img, stats, user_name, User_Text, data))
    username_th.start()
    twidth, _ = draw.textsize(data['player_name'], font=font2)
    
    is_staff_member = user_name.lower() in [e_pat.lower() for e_pat in staff_names]
    staff_offset = -100
    staff_offset = 225 + sum([bool(data['partner_approved']),
                             bool(data['player_featured']),
                             bool(data['player_premium'] > 0),
                             bool(data['player_infected']) ])*38
    try:
        if stats["flg"] == -1:
            raise TypeError()
        country = Countries[stats["flg"]]
        staff_offset += 40
    except:pass
    def put_top_stats(img, stats, user_name, is_staff_member, staff_offset):
        offset_pf = 0
        try:
            if stats["flg"] == -1:
                raise TypeError()
            country = Countries[stats["flg"]]
            sheet = client.country_sheet
            flg = sheet.crop((abs(country[1]), abs(country[2]), abs(country[1])+32, abs(country[2])+32))
            img.paste(flg, (225+offset_pf, 50), flg)
            offset_pf += 40
        except:pass
        if bool(data['partner_approved']):
            if data['partner_approved'] == 1:
                partn = client.partn
            else:
                partn = client.partn2
            img.paste(partn, (225+offset_pf, 50), partn)
            offset_pf += 38
        if bool(data['player_featured']):
            #x12, y39
            verif = client.verif
            img.paste(verif, (225+offset_pf, 50), verif)
            offset_pf += 38
        if data['player_premium'] > 0:
            #x12, y39
            prem = client.prem
            img.paste(prem, (225+offset_pf, 50), prem)
            offset_pf += 35
        if bool(data['player_infected']):
            inf = client.inf
            img.paste(inf, (225+offset_pf, 50), inf)
            offset_pf += 38
        if is_staff_member:
            partn = client.staff_.copy()
            img.paste(partn, (staff_offset, 50), partn)
            offset_pf += 38
            
        if user_name.lower() in [e_pat.lower() for e_pat in patreons_names]:
            partn = client.patron
            img.paste(partn, (225+offset_pf, 50), partn)
            offset_pf += 38
        if user_name.lower() in [e_pat.lower() for e_pat in double_boosters]:
            partn = client.boost
            img.paste(partn, (225+offset_pf, 50), partn)
            offset_pf += 38
        if user_name.lower() in [e_pat.lower() for e_pat in boosters]:
            partn = client.sboost
            img.paste(partn, (225+offset_pf, 50), partn)
            offset_pf += 38
            
        if data['player_type'] == 1:
            partn = client.kdev
            img.paste(partn, (225+offset_pf, 50), partn)
    top_stats_thr = threading.Thread(target = put_top_stats, args = (img, stats, user_name, is_staff_member, staff_offset))
    top_stats_thr.start()
    
    green_c = (83, 228, 12)
    yell_c = (220, 228, 12)
    red_c = (228, 12, 57)
    blue_c = (12, 159, 228)
    def get_color(val, mval):
        if mval == 0:return green_c
        elif (o_val := val / mval * 100.0) < 50:return red_c
        elif o_val > 50 and o_val < 100:return yell_c
        elif o_val >= 100 and o_val < 200:return green_c
        elif o_val >= 200:return blue_c
    unqualified = False
    if is_applying:
        lvl_c = get_color(max(1, math.floor(0.03 * math.sqrt(data["player_score"]))), application["lvl"])
        try:_name = "%.2f" % float(data['player_kills']/data['player_deaths'])
        except:
            if str(data['player_deaths']) != '0': _name = '0'
            else:_name = str(data['player_kills'])
        kdr_c = get_color(float(_name), application["kdr"])
        try:_name = int(data['player_score']/data['player_kills'])
        except:_name = 0
        spk_c = get_color(_name, application["spk"])
        try:_name = '{:.2f}'.format(data['player_kills']/data['player_games_played'])
        except:_name = '0'
        kpg_c = get_color(float(_name), application["kpg"])
        try:_name = stats['n']
        except:_name = 0
        nukes_c = get_color(_name, application["n"])
        try:_name = '{:.2f}'.format((stats['h'] or 0) / stats['s'] * 100 if stats['s'] else 0)
        except:_name = '0'
        try:acc_c = get_color(float(_name), application["acc"])
        except:acc_c = green_c
        if yell_c in [lvl_c, kdr_c, spk_c, kpg_c, nukes_c]:unqualified = True
        if red_c in [lvl_c, kdr_c, spk_c, kpg_c, nukes_c]:unqualified = True
    else:lvl_c = kdr_c = spk_c = kpg_c = nukes_c = acc_c = value_c
    y_offset_overall = 69
    Level_, lvl_color = get_level_int_c(data['player_chal'])
    drawtext(draw, (139, 57), "LVL", lvl_c, font=font4)
    t_width, _ = draw.textsize("LVL ", font=font4)
    drawtext(draw, (139+t_width+4, 57), str(max(1, math.floor(0.03 * math.sqrt(data["player_score"])))), lvl_color, font = font4)
    colored_text = False
    if bool(data['player_clan']):
        clan_stroke_clr = (0, 0, 0)
        clan_c = (150, 150, 150)
        clan_text = "[{}]".format(data['player_clan'])
        if clan_text.isascii():clan_font = font2;offset__ = 0
        else:clan_font = unicode_font;offset__ = 5
        if data['clan_rank'] == 1:
            draw.text((135+twidth+15, 15), clan_text, (0, 0, 0), font = font2, stroke_fill = clan_stroke_clr, stroke_width = 1)
            colored_text = ((135+twidth+15, 15), clan_text, clan_font)
        else:
            try:
                clan_color = clan_colors[data['clan_rank']]
                if clan_color == clan_stroke_clr:
                    clan_stroke_clr = (25, 25, 25)
            except:clan_color = (200, 200, 200)
            if data['player_clan'].lower() == "dev":clan_color = (64, 196, 255)
            if clan_text.isascii():draw.text((135+twidth+15, 15), clan_text, clan_color, font = clan_font, stroke_fill = clan_stroke_clr, stroke_width = 1)
            else:draw_non_acsii(135+twidth+15, 15, clan_text, font2, unicode_font, clan_color, draw, stroke_fill = clan_stroke_clr, stroke_width = 1)
    col_1 = -17
    col_2 = -8
    col_3 = -4
    col_4 = 4
    col_5 = 8
    col_6 = 17
    def top_stats_r1(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):
        custom_out((25+4+5, 90+y_offset_overall), 'KILLS',main_c,font=font)
        kills = read_format(data['player_kills'])
        drawtext(draw, (vldr(kills, 57),  90+25+y_offset_overall), kills, value_c, font=font)

        custom_out((25+100+20-1, 90+y_offset_overall), 'DEATHS',main_c,font=font)
        wins = read_format(data['player_deaths'])
        drawtext(draw, (vldr(wins, 176), 90+25+y_offset_overall), wins,value_c,font=font)

        custom_out((25+100+100+40-4, 90+y_offset_overall), 'SCORE',main_c,font=font)
        _name = read_format(data['player_score'])
        drawtext(draw, (vldr(_name, 287), 90+25+y_offset_overall), _name,value_c,font=font)
    tpr1 = threading.Thread(target = top_stats_r1, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr1.start()
    def top_stats_r12(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):

        custom_out((316+60-9, 90+y_offset_overall), 'CHALLENGE',main_c,font=font)
        _name = read_format(data['player_chal']+1).replace("None", "0")
        drawtext(draw, (vldr(_name, 413), 90+25+y_offset_overall), _name,value_c,font=font)

        custom_out((450+80-13, 90+y_offset_overall), 'TIME',main_c,font=font)
        try:_name = ago.human(datetime.timedelta(seconds = int(data['player_timeplayed']/1000)), past_tense = "{}", future_tense = "{}", abbreviate=True)
        except:_name = '0'
        _name = _name if _name else "0"
        drawtext(draw, (vldr(_name, 551-13), 90+25+y_offset_overall), _name,value_c,font=font)

        custom_out((533+100-15, 90+y_offset_overall), 'NUKES',main_c,font=font)
        try:_name = str(stats['n'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 560+100-15), 90+25+y_offset_overall), _name,nukes_c,font=font)
    tpr12 = threading.Thread(target = top_stats_r12, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr12.start()
    def top_stats_r2(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):
        custom_out((23+5-2, 160+y_offset_overall), 'PLAYED',main_c,font=font)
        _name = read_format(data['player_games_played'])
        drawtext(draw, (vldr(_name, 57), 160+25+y_offset_overall), _name,value_c,font=font)
        
        custom_out((6+120-1+20+12-2, 160+y_offset_overall), 'WINS',main_c,font=font)
        _name = read_format(data['player_wins'])
        drawtext(draw, (vldr(_name, 176), 160+25+y_offset_overall), _name,value_c,font=font)

        custom_out((25+100+100+40-4-5-1, 160+y_offset_overall), 'LOSSES',main_c,font=font)
        try:_name = read_format(data['player_games_played'] - data['player_wins'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 286), 160+25+y_offset_overall), _name,value_c,font=font)
    tpr2 = threading.Thread(target = top_stats_r2, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr2.start()
    def top_stats_r22(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):        
        custom_out((316+60-8-2-1, 160+y_offset_overall), 'HEADSHOTS',main_c,font=font)
        try:_name = read_format(stats['hs'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 413), 160+25+y_offset_overall), _name,value_c,font=font)

        custom_out((450+80-20-11-8-3, 160+y_offset_overall), 'WALLBANGS',main_c,font=font)
        try:_name = read_format(stats['wb'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 538), 160+25+y_offset_overall), _name,value_c,font=font)

        custom_out((530+100-15-4-1, 160+y_offset_overall), 'MELEES',main_c,font=font)
        try:_name = read_format(stats['mk'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 644), 160+25+y_offset_overall), _name,value_c,font=font)
    tpr22 = threading.Thread(target = top_stats_r22, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr22.start()
    def top_stats_r3(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):
        custom_out((25+4+5-5+2+1, 230+y_offset_overall), 'MAPS',main_c,font=font)
        _name = str(len(mdata[4]))
        drawtext(draw, (vldr(_name, 57), 230+25+y_offset_overall), _name,value_c,font=font)

        custom_out((6+120+20+5, 230+y_offset_overall), 'MODS',main_c,font=font)
        _name = str(len(mdata[5]))
        drawtext(draw, (vldr(_name, 176), 230+25+y_offset_overall), _name,value_c,font=font)

        custom_out((225+40-4-7, 230+y_offset_overall), 'ASSETS',main_c,font=font)
        _name = str(len(mdata[7]))
        drawtext(draw, (vldr(_name, 286), 230+25+y_offset_overall), _name,value_c,font=font)
    tpr3 = threading.Thread(target = top_stats_r3, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr3.start()
    def top_stats_r32(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):
        custom_out((320+60-5-8+6-3, 230+y_offset_overall), 'ACCURACY',main_c,font=font)
        try:_name = '{:.2f}'.format((stats['h'] or 0) / stats['s'] * 100 if stats['s'] else 0)
        except:_name = '0'
        _name += " %"
        drawtext(draw, (vldr(_name, 413), 230+25+y_offset_overall), _name,acc_c,font=font)

        custom_out((450+80-28-10-11+9, 230+y_offset_overall), 'BULLSEYES',main_c,font=font)
        try:_name = str(stats["tmk"])
        except:_name = "0"
        drawtext(draw, (vldr(_name, 537), 230+25+y_offset_overall), _name,value_c,font=font)

        custom_out((530+100-15-15-3, 230+y_offset_overall), 'BEATDOWNS',main_c,font=font)
        try:_name = str(stats["fk"])
        except:_name = "0"
        drawtext(draw, (vldr(_name, 647), 230+25+y_offset_overall), _name,value_c,font=font)
    tpr32 = threading.Thread(target = top_stats_r32, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr32.start()
    def top_stats_r4(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):
        custom_out((25+4+8+4, 300+y_offset_overall), 'SPK',main_c,font=font)
        try:_name = str(int(data['player_score']/data['player_kills']))
        except:_name = "0"
        drawtext(draw, (vldr(_name, 57), 300+25+y_offset_overall), _name,spk_c,font=font)

        
        custom_out((6+120+20+3+8+2, 300+y_offset_overall), 'W/L',main_c,font=font)
        try:_name = "%.2f" % float(data['player_wins']/(data['player_games_played'] - data['player_wins']))
        except:_name = "1"
        drawtext(draw, (vldr(_name, 176), 300+25+y_offset_overall), _name,value_c,font=font)

        
        custom_out((225+40+5+1, 300+y_offset_overall), 'KDR',main_c,font=font)
        try:_name = "%.2f" % float(data['player_kills']/data['player_deaths'])
        except:
            if str(data['player_deaths']) != '0': _name = '0'
            else:_name = str(data['player_kills'])
        drawtext(draw, (vldr(_name, 287), 300+25+y_offset_overall), _name,kdr_c,font=font)
    tpr4 = threading.Thread(target = top_stats_r4, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr4.start()
    def top_stats_r42(stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6):

        custom_out((320+60-5+26, 300+y_offset_overall), 'KR',main_c,font=font)
        try:_name = read_format(data['player_funds'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 411), 300+25+y_offset_overall), _name,value_c,font=font)

        custom_out((450+80-28-10+29+1, 300+y_offset_overall), 'KPG',main_c,font=font)
        try:_name = '{:.2f}'.format(data['player_kills']/data['player_games_played'])
        except:_name = '0'
        drawtext(draw, (vldr(_name, 538), 300+25+y_offset_overall), _name,kpg_c,font=font)

        custom_out((649-50-1, 300+y_offset_overall), 'MMR 1/2/4',main_c,font=font)
        _name = str(data['player_elo']).replace("None", "0")+"/"+str(data['player_elo2']).replace("None", "0")+"/"+str(data['player_elo4']).replace("None", "0")
        drawtext(draw, (vldr(_name, 647, font3), 300+25+y_offset_overall), _name,value_c,font=font3)

    tpr42 = threading.Thread(target = top_stats_r42, args = (stats, data, main_c, y_offset_overall, font, value_c, col_1, col_2, col_3, col_4, col_5, col_6))
    tpr42.start()
    def paste_profile_icon(stats, data, img):
        try:
            if not (data['player_premium'] > 0):
                raise TimeoutError()
            response = requests.get("https://user-assets.krunker.io/p{}/profile.png".format(data["player_id"]))
            thumb = Image.open(BytesIO(response.content)).convert("RGBA")
            profile_icon = thumb.resize((107,107)).convert("RGBA")
            new_pficon = Image.new("RGBA", (107, 107), (0, 0, 0, 0))
            new_pficon.paste(profile_icon, (0, 0), client.icon_mask)
            profile_icon = new_pficon
                
        except:
            try:
                class_n = stats["c"]
            except:
                class_n = 0
            profile_icon = client.icons[class_n]
        img.paste(profile_icon, (9, 11), profile_icon)
    pficontr = threading.Thread(target = paste_profile_icon, args = (stats, data, img))
    pficontr.start()
    
    paste_border = borders["outl"]
    paste_shd = borders["shd"]
    def outline_stuff(borders):
        try:
            if borders["outl"]:
                if borders["xpb"]:
                    xpbar = Image.open("Data/xpbar.png", "r").convert("RGBA")
                    img.paste(xpbar, (0, 0), xpbar)
        except:pass
    outltr = threading.Thread(target = outline_stuff, args = (borders,))
    outltr.start()
    outltr.join()
    def badges_ranksp1(stats, data, user_name):
        score = data['player_score']
        level = max(1, math.floor(0.03 * math.sqrt(data["player_score"])))
        tmpRank = 0.03 * math.sqrt(score)
        level = math.floor(tmpRank)
        levelPerc = round((tmpRank - level) * 100) # level progress in %
        level = max(1, level) # actual player level

        offset = pow(level / 0.03, 2) if 1 < level else 0
        levelProg = read_format(math.floor(score - offset)) + ' / ' + read_format(math.floor(pow((level + 1) / 0.03, 2) - offset))
        levelProgVal = math.floor(score - offset)/(math.floor(pow((level + 1) / 0.03, 2) - offset))

        inf_offset = 0

        iconId = max(min(maxLevel - 1, roundToNearest(level, 2) - 1), 0)

        try:
            #response = requests.get("https://krunker.io/img/levels/{}.png".format(iconId))
            #thumb = Image.open(BytesIO(response.content)).convert("RGBA")
            img.paste(client.levels[iconId], (485+15+20, 10), client.levels[iconId])
        except:pass
        

        elo = max(min(8, math.floor(data['player_elo'] / 120)), 1) - 1
        img.paste(client.ranks[elo], (530+15+15, 10), client.ranks[elo])

        elo = max(min(8, math.floor(data['player_elo2'] / 120)), 1) - 1
        img.paste(client.ranks[elo], (530+50+15+10, 10), client.ranks[elo])

        elo = max(min(8, math.floor(data['player_elo4'] / 120)), 1) - 1
        img.paste(client.ranks[elo], (530+50+50+15+5, 10), client.ranks[elo])
        ldoffs = 0
        if is_default:
            loadn = client.defloadn
            ldoffs = 0
        else:
            loadn = client.defloadn
        x, y = loadn.size
        loadn = loadn.crop((0, 0, int(levelProgVal*534), y))
        loadn = loadn.copy()
        if not is_default:
            loadn = tint_image(loadn, bar_color, 1.6)
            
        img.paste(loadn, (152, 90-ldoffs), loadn)
        custom_out((152+vldr(levelProg, 272), 92), levelProg, (255, 255, 255),font=font)
    def badges_ranksp2(stats, data, user_name):
        has_premium = 0
        has_twitch = 0
        has_motto = 0
        if data['player_premium'] > 0 and data['player_alias'] != None and data['player_alias'] != data['player_name']:
            has_premium = 1
        if data['player_twitchname']:
            has_twitch = 1
        if motto:
            has_motto = 1
        if has_premium:
            prem = client.prem.copy()
            prem.thumbnail((20, 21), Image.ANTIALIAS)
            img.paste(prem, (160-6-5, 121), prem)

            #draw.text((152, 126), "aka" ,(130, 130, 130),font=font3)
            draw.text((181-6-5, 123), data['player_alias'] ,foot_c,font=font6)
            prem_x_size, _ = draw.textsize(data['player_alias'], font6)
            
        if motto:
            motto_x_pos, _ = draw.textsize(motto, font6)
            
            partn = client.speech
            img.paste(partn, (700-motto_x_pos-26, 119), partn)
            
            custom_out((700-motto_x_pos, 122), motto, foot_c, font=font6, outline = 0)
            motto_x_pos += 26
    def badges_ranksp22(stats, data, user_name):
        has_premium = 0
        has_motto = 0
        motto_x_pos = 0
        prem_x_size = 0
        if motto:
            has_motto = 1
            motto_x_pos, _ = draw.textsize(motto, font6)
            motto_x_pos += 26
        if data['player_premium'] > 0 and data['player_alias'] != None and data['player_alias'] != data['player_name']:
            has_premium = 1
            prem_x_size, _ = draw.textsize(data['player_alias'], font6)
        if data['player_twitchname']:
            twitch_x_size, _ = draw.textsize(data['player_twitchname'], font6)
            if has_premium and motto:
                twitch_x_pos =  int((((700-motto_x_pos) + ((181-6-5) + prem_x_size))/2) - ((twitch_x_size+23)/2))
            elif not has_premium:
                twitch_x_pos = 155
            else:
                twitch_x_pos = 700-20-twitch_x_size
            partn = client.twitch
            img.paste(partn, (twitch_x_pos, 121), partn)
            
            draw.text((twitch_x_pos+23, 123), data['player_twitchname'] ,foot_c, font=font6)
            
        if player_dis := str(muser):
            if player_dis != "-1":
                if len(player_dis) >= 26+5:
                    dname = player_dis.rsplit("#")[0]
                    dtag = player_dis.rsplit("#")[1]
                    dname = dname[:24] + "..."
                    player_dis = dname + dtag
                twidth = cal_non_acsii(player_dis, font6, unicode_font)
                write_non_chars(draw, (700-twidth, 60), player_dis, font6, unicode_font, color = foot_c, outline_c = 0)
                img.paste(client.discord, (700-twidth-32, 56), client.discord)
            else:
                img.paste(client.discord, (700-30, 56), client.discord)
    br = threading.Thread(target = badges_ranksp1, args = (stats, data, user_name))
    br.start()
    br2 = threading.Thread(target = badges_ranksp2, args = (stats, data, user_name))
    br2.start()
    br22 = threading.Thread(target = badges_ranksp22, args = (stats, data, user_name))
    br22.start()
    
    
    def footer_t(stats, data, user_name, is_applying, unqualified):
        member_since = data['player_datenew'][:10].split("-")
        month_since = month[int(member_since[1])].lower().title()
        member_since[1] = month_since
        outline_c = (60, 60, 60)
        custom_out((20, 435), 'Member since '+str("-".join(member_since)), foot_c, font=font, outline = 0)
        custom_out((360, 435), human_format(data['player_followed'])+' Followers', foot_c, font=font, outline = 0)
        custom_out((565, 435), human_format(data['player_following'])+' Following', foot_c, font=font, outline = 0)
        if is_applying:
            if unqualified:
                drawtext(draw, (vldr("UNQUALIFIED", int(img.width/2)),  120), "UNQUALIFIED", red_c, font=font4)
            else:
                drawtext(draw, (vldr("QUALIFIED", int(img.width/2)),  120), "QUALIFIED", green_c, font=font4)

    ft_t = threading.Thread(target = footer_t, args = (stats, data, user_name, is_applying, unqualified))
    ft_t.start()
    total_frames = []
    duration = 0
    if colored_text or is_staff_member:
        if len(list(ImageSequence.Iterator(pbimg))) == 1:
            duration = 40
    def proccess_frame(frame):
        #if put_overlay:
            #frame.paste(client.overlay, (0, 0), client.overlay)
        return frame
    def ready_background(total_frames, pbimg):
        if len(list(ImageSequence.Iterator(pbimg))) == 1:
            total_frames.append(proccess_frame(pbimg.copy().convert("RGBA")))
            if colored_text or is_staff_member:
                for _ in range(29):
                    total_frames.append(proccess_frame(pbimg.copy().convert("RGBA")))
        else:
            for e_fr in ImageSequence.Iterator(pbimg):
                total_frames.append(proccess_frame(e_fr.copy().convert("RGBA")))
    rdbgtr = threading.Thread(target = ready_background, args = (total_frames, pbimg))
    rdbgtr.start()
    
                
    #return gb_logo(img)
    ngb_logo = client.gb
    if logo_color:
        ngb_logo = tint_image(ngb_logo, logo_color)
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33))
    tpr1.join()
    tpr2.join()
    tpr3.join()
    tpr4.join()
    tpr12.join()
    tpr22.join()
    tpr32.join()
    tpr42.join()
    outltr.join()
    if data['player_type'] == 10:
        hacker_y = 157
        if bool(data['player_hack']):locked_y = 240
        else:locked_y = 200
        partn = Image.open("Data/locked.png","r")
        img.paste(partn, (240, locked_y), partn)
    else:hacker_y = 200
    
    if bool(data['player_hack']):
        partn = Image.open("Data/hacker.png","r")
        img.paste(partn, (240, hacker_y), partn)
    br.join()
    username_th.join()
    br2.join()
    br22.join()
    top_stats_thr.join()
    ft_t.join()
    pficontr.join()
    main_colored_img = img.copy()
    if t_shadows:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0)
        img2 = img.copy().filter(ImageFilter.GaussianBlur(radius=6.5))
        img = img.filter(ImageFilter.GaussianBlur(radius=3))
        img.alpha_composite(img2)
        img.paste(main_colored_img, (0, 0), main_colored_img)
    if put_overlay != -1:
        nimg = client.overlay.copy()
        nimg.alpha_composite(img)
        img = nimg
    #frame.paste(client.overlay, (0, 0), client.overlay)
    rdbgtr.join()
    dropshadow = client.dropshadow
    frames = {}

    
    if paste_border:
        outlining = client.outlining.copy()
        if borders["clr"]:
            change_color_(borders["clr"][0], borders["clr"][1], borders["clr"][2], outlining)
        if paste_shd:
            img.paste(client.dropshadowoutline, (0, 0), client.dropshadowoutline)
        img.paste(outlining, (0, 0), outlining)
    tag_colors = [(237, 20, 61), (239, 40, 53), (242, 61, 44), (244, 82, 35), (247, 102, 27), (249, 123, 18), (249, 123, 18), (255, 177, 0), (255, 190, 0), (255, 203, 0), (255, 216, 0), (255, 229, 0), (255, 229, 0), (219, 255, 0), (183, 255, 0), (146, 255, 0), (110, 255, 0), (73, 255, 0), (73, 255, 0), (0, 219, 29), (0, 183, 58), (0, 146, 87), (0, 110, 117), (0, 73, 146), (0, 73, 146), (33, 2, 185), (67, 5, 164), (101, 8, 144), (135, 11, 123), (169, 14, 103)] * 10
    sttag_colors = [(255, 0, 221), (232, 0, 225), (209, 0, 230), (186, 0, 235), (163, 0, 240), (140, 0, 245), (140, 0, 245), (112, 21, 252), (132, 43, 249), (152, 65, 245), (172, 87, 242), (192, 109, 238), (192, 109, 238), (229, 141, 234), (226, 129, 237), (223, 117, 240), (219, 105, 243), (216, 93, 246), (216, 93, 246), (199, 78, 252), (189, 88, 251), (178, 98, 250), (168, 109, 250), (157, 119, 249), (157, 119, 249), (153, 120, 244), (170, 100, 240), (187, 80, 236), (204, 60, 233), (221, 40, 229)] * 10
    def append_make_frames(frame, x, frames, is_default, colored_text, is_staff_member, tag_colors, sttag_colors):
        nframe = frame
        nframe.alpha_composite(img)
        
        if colored_text or is_staff_member:
            if is_staff_member:
                stnew_c  = sttag_colors[x]
                partn = client.staff_.copy()
                change_color(stnew_c[0], stnew_c[1], stnew_c[2], partn)
                img.paste(partn, (staff_offset, 50), partn)
            if colored_text:
                draw = ImageDraw.Draw(nframe)
            
                new_c = tag_colors[x]
                if clan_text.isascii():
                    draw.text(colored_text[0], clan_text, new_c, font = colored_text[2], stroke_fill = (0,0,0), stroke_width = 1)
                else:
                    draw_non_acsii(colored_text[0][0], colored_text[0][1], clan_text, font2, unicode_font, new_c, draw, stroke_fill = (0,0,0), stroke_width = 1)
        frames[x] = nframe
    threads = []
    for x, frame in enumerate(total_frames):
        th = threading.Thread(target = append_make_frames, args = (frame, x, frames, is_default, colored_text, is_staff_member, tag_colors, sttag_colors))
        th.start()
        threads.append(th)
        
    for e_thread in threads:
        e_thread.join()
    frames = list(dict(sorted(frames.items())).values())
    byte_io = BytesIO()
    byte_io.seek(0)
    if len(frames) == 1:
        frames[0].save(byte_io, format="PNG", quality = 100)
        img_format = "png"
    else:
        if duration:
            frames[0].save(byte_io, format="GIF", save_all=True, append_images=frames[1:], quality = 100, transparency=255, loop = 0, duration = duration)
        else:
            frames[0].save(byte_io, format="GIF", save_all=True, append_images=frames[1:], quality = 100, transparency=255, loop = 0)
        img_format = "gif"
    byte_io.seek(0)
    return byte_io, img_format
        

def classic_outline(img, x_ = 2, y_ = 9, border = 4, color = (20,22,24), radius= 25):
    img = add_corners(img, radius)
    img_b = Image.new('RGB', (img.width + x_, img.height + x_), color)
    img_b = ImageOps.expand(img_b, border=border, fill = color)
    img_b = add_corners(img_b, radius)        
    img_b.paste(img, (3, 3), img)
    return img_b
def gb_logo(img):
    ngb_logo = client.gb
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)                
    byte_io = BytesIO()
    byte_io.seek(0)
    img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io
def fill_tp(r, g, b, img):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if list(pixels[i, j])[-1] == 0:
                pixels[i, j] = (r, g, b, 255)
def outline_text(draw, x, y, color_, shadow_color_, text_, font_, thickness = 1):
    draw.text((x, y), text_, font=font_, fill=color_, stroke_fill = shadow_color_, stroke_width = thickness)
    
def xp_count(val):
    return "{:,}".format(int(max(1, math.floor(0.03 * math.sqrt(val)))))
async def manage_impressions(user_name, uid):
    with open("Data/linked.bt", "rb") as file:
        link_data = pickle.load(file)
    accounts = [k for k, v in link_data.items() if v == uid]
    if user_name.lower() in accounts:
        return
    try:
        client.simpressions[user_name] += [int(time.time())]
    except:
        client.simpressions[user_name] = [int(time.time())]
async def save_cache(data, user_name):
    for _ in range(3):
        async with aiofiles.open("Data/cache.bt", "rb") as file:
            try:
                old_data = pickle.loads(await file.read())
                break
            except EOFError:await asyncio.sleep(0.1)
    old_data[user_name.lower()] = data
    async with aiofiles.open("Data/cache.bt", "wb") as file:
        await file.write(pickle.dumps(old_data))
async def get_cache(user_name=None):
    for _ in range(3):
        async with aiofiles.open("Data/cache.bt", "rb") as file:
            try:
                old_data = pickle.loads(await file.read().encode('utf-8'))
                break
            except EOFError:await asyncio.sleep(0.1)
    if user_name:
        try:
            return old_data[user_name.lower()]
        except:
            return ['cpt']
    else:
        return old_data
def convert_int(integer):
    return '{:,}'.format(integer)
client.cpt = False
client.cpt_token = ""
async def get_cpt_token():
    try:
        await client.get_guild(708067789830750449).get_channel(747221866216816800).send("Oh boy! I am not feeling so good")
    except:pass
    if not client.cpt:
        try:
            client.cpt = True
            threading.Thread(target = lambda:os.system("python cpt_opener.py")).start()
            await asyncio.sleep(3.5)
            timeout = aiohttp.ClientTimeout(total=15)
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                async with session.get('http://localhost:3000/token', timeout=timeout) as resp:
                    client.cpt = False
                    client.cpt_token = await resp.text()
                    with open("done.response", "w") as f:pass
                    return client.cpt_token
            print("hmmm?")
        except:client.cpt = False
    else:
        while client.cpt:
            await asyncio.sleep(1)
        return client.cpt_token

async def get_cpt_tokenprev():
    if not client.cpt:
        try:
            client.cpt = True
            cpsl = subprocess.Popen("pause", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            await asyncio.sleep(3)
            if "Token Done" not in cpsl.communicate()[0]:
                await asyncio.sleep(1)
            timeout = aiohttp.ClientTimeout(total=15)
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                async with session.get('http://localhost:3000/token', timeout=timeout) as resp:
                    client.cpt = False
                    client.cpt_token = await resp.text()
                    with open("done.response", "w") as f:pass
                    cpsl.kill()
                    return client.cpt_token
            print("hmmm?")
        except:
            client.cpt = False
    else:
        while client.cpt:
            await asyncio.sleep(1)
        return client.cpt_token


async def get_color_input(msg):
    def check(m):return m.channel == msg.channel and m.author == msg.author
    for _ in range(5):
        try:msg_ = await client.wait_for('message', check=check, timeout=130)
        except asyncio.TimeoutError:await msg.add_reaction(warning);return
        else:
            if msg_.content.lower() == "cancel":await msg.channel.send(warning+" Editing Cancelled!");return
            if msg_.content.lower() == "skip":return "skip"
            elif msg_.content.startswith("#"):
                try:
                    return ImageColor.getcolor(msg_.content, "RGB")
                except:
                    await emb_send(msg.channel, warning+ " Incorrect color. Please enter Hex `#color` or RGB, `255, 255, 255`");continue
            else:
                cnt = msg_.content
                cnt = cnt.replace(" ", "").replace("(", "").replace(")", "")
                data = cnt.split(",")
                try:
                    return (int(data[0]), int(data[1]), int(data[2]))
                except:
                    await emb_send(msg.channel, warning+ " Incorrect color. Please enter Hex `#color` or RGB, `255, 255, 255`");continue
                
async def await_get(url):
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(url, timeout=timeout) as resp:
            return await resp.text()
def request_get_sync(url):
    return requests.get(url)

async def requestsget(url):
    thing = functools.partial(request_get_sync, url)
    with ThreadPoolExecutor(max_workers = 1) as executor:
        return await client.loop.run_in_executor(executor, thing)
async def get_user_data(username, type_ = "profile", pf__ = 0):
    
    output = await get_main_user_data(username, type_)
    if output == ['cpt'] and not pf__:
        with open(pfp_id_file, "rb") as file:
            ppl_ids = pickle.load(file)
        ppl_ids = {k.lower(): v for k, v in ppl_ids.items()}
        try:
            ppl_id = ppl_ids[username.lower()]
            rise = False
        except:
            rise = True
        if rise:
            raise TimeoutError("Websocket issue. The issue will be fixed within few hours or mins.\nIf problem persists, contact bot dev")
        hosts_htm = await await_get(api_maps_url+str(ppl_id))
        maps = json.loads(hosts_htm)['data']
        for e_map in maps:
            e_map['player_name'] = e_map.pop('creatorname')
            
        return [None, None, None, {'player_name':username}, maps, None]
    else:
        return output
    
def save_pid(outdata):
    try:
        with open(pfp_id_file, "rb") as file:
            old_data = pickle.load(file)
        old_data[outdata[3]["player_name"]] = outdata[3]["player_id"]
        with open(pfp_id_file, "wb") as file:
            pickle.dump(old_data, file)
    except:
        pass
async def emb_send(chl, cnt, emb_color = 14423783, footer_t = "", title_ = "", file = None, image_url = ""):
    embed=discord.Embed(colour=discord.Colour(emb_color),
                        description = cnt,
                        title = title_)
    if footer_t:embed.set_footer(text=footer_t)
    if image_url:embed.set_image(url=image_url)
    msg_ = await chl.send(embed=embed, file = file)
    return msg_

async def emb_edit(msg_, content, emb_color = 14423783, footer_t = "", title_ = "", file = None, image_url = ""):
    embed=discord.Embed(colour=discord.Colour(emb_color),
                        description = content,
                        title = title_)
    if footer_t:embed.set_footer(text=footer_t)
    if image_url:embed.set_image(url=image_url)
    await msg_.edit(embed=embed)
def read_data_by_type(data, user_name, type_):
    try:
        if type_ in ["profile", "map", "clan", "clanwars"]:
            return data[2] == user_name
        else:
            return True
    except:pass
async def find_msg(user_name, type_):
    for _ in range(50):
        all_msgs = list(client.ws.messages)
        all_msgs.reverse()
        try:
            if "cpt" in (first_msg:= msgpack.unpackb(all_msgs[0][0:-2], raw=False)) and "True" not in first_msg:
                return ['cpt']
        except Exception as e:
            print(e)
        for e_msg in all_msgs:
            data = msgpack.unpackb(e_msg[0:-2], raw=False)
            if data == ["pi"]:
                continue
            elif data == ["cpt"]:
                return ["cpt"]
            if read_data_by_type(data, user_name, type_):
                return data
        await asyncio.sleep(0.1)
client.responses = {}
'''async def check_and_reconnect():
    async def fetch():
        greeting = await client.ws.recv()
        greeting = msgpack.unpackb(base64.b64decode(greeting[0:-2]), raw=False)
        return greeting
    while True:
        await client.ws.send(msgpack.packb(["pi"], use_bin_type=True) + b"\x00\x00")
        fetch()
    
'''
        
def get_data_msgpack(d):
    ahNum = (0 + client.ahk) & 0xFF
    ahk_b = bytes([ahNum >> 4 & 0xF, ahNum & 0xF])
    #print(d)
    return msgpack.packb(d, use_bin_type=True)+ahk_b
async def get_main_user_data(username, type_ = "profile"):
    async def ws_connect(username, type_):
        async def fetch():
            greeting = await websocket.recv()
            base_decode= greeting[0:-2]
            greeting = msgpack.unpackb(base_decode, raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        data = get_data_msgpack(["r", type_, username, None, None, None, "0", None])
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context, max_size= 1539487) as websocket:
            await websocket.send(data)
        
        
            for _ in range(35):
                outdata = await fetch()
                if str(outdata) == "['cpt']":# or "Socket error" in outdata:
                    client.cptpause = True
                    for _ in range(2):
                        token__ = await get_cpt_token()
                        if token__:break
                    print(token__, "token__")
                    try:
                        await websocket.send(get_data_msgpack(["cptR", token__]))
                        await websocket.send(data)
                    except:pass
                    client.cptpause = False
                elif str(outdata) == "['cptR', True]":
                    print(outdata);continue
                elif outdata != "['pi']":
                    break
                await asyncio.sleep(0.1)
            #client.loop.create_task(save_pid(outdata))
            await websocket.close()
        return outdata

    return await ws_connect(username, type_)


async def get_any_data(list_):
    async def ws_connect(list_):
        async def fetch():
            greeting = await websocket.recv()
            base_decode= greeting[0:-2]
            greeting = msgpack.unpackb(base_decode, raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        data = get_data_msgpack(list_)
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context) as websocket:
            await websocket.send(data)
        
        
            for _ in range(35):
                outdata = await fetch()
                if str(outdata) == "['cpt']":# or "Socket error" in outdata:
                    client.cptpause = True
                    for _ in range(2):
                        token__ = await get_cpt_token()
                        if token__:break
                    print(token__, "token__")
                    try:
                        await websocket.send(get_data_msgpack(["cptR", token__]))
                        await websocket.send(data)
                    except:pass
                    client.cptpause = False
                elif str(outdata) == "['cptR', True]":
                    print(outdata);continue
                elif outdata != "['pi']":
                    break
                await asyncio.sleep(0.1)
            #client.loop.create_task(save_pid(outdata))
            await websocket.close()
        return outdata

    return await ws_connect(list_)


async def get_market(id_):
    async def ws_connect(id_):
        async def fetch():
            greeting = await websocket.recv()
            greeting = msgpack.unpackb(greeting[0:-2], raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context) as websocket:
            data = get_data_msgpack(["r", "itemsales", "market", None, None, None, 0, id_])
            await websocket.send(data)
            for _ in range(35):
                outdata = await fetch()
                if str(outdata) == "['cpt']":
                    print(outdata)
                    token__ = await get_cpt_token()
                    await websocket.send(get_data_msgpack(["cptR", token__]))
                    await websocket.send(data)
                elif str(outdata) == "['cptR', True]":
                    print(outdata)
                    continue
                elif outdata != "['pi']":
                    break
                await asyncio.sleep(0.1)
            await websocket.close()
        return outdata

    return await ws_connect(id_)

async def get_user_data_led(username, type_ = "profile"):
    async def ws_connect(username, type_):
        async def fetch():
            greeting = await websocket.recv()
            greeting = msgpack.unpackb(greeting[0:-2], raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context) as websocket:
            data = get_data_msgpack(["r", "leaders", username, None, None, None, "0", None])
            await websocket.send(data)
            await asyncio.sleep(1)
        
        
            for _ in range(5):
                outdata = await fetch()
                if outdata != "['pi']":
                    break
            await websocket.close()
        return outdata

    return await ws_connect(username, type_)

async def get_user_posts(userid, custom=0):
    async def ws_connect(userid):
        async def fetch():
            greeting = await websocket.recv()
            greeting = msgpack.unpackb(greeting[0:-2], raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context) as websocket:
            if not custom:
                data = get_data_msgpack(["guf", int(userid), None, None, None, None, "0", None])
            else:
                data = get_data_msgpack(custom)
            await websocket.send(data)
            await asyncio.sleep(1)
            for _ in range(10):
                outdata = await fetch()
                if str(outdata) == "['cpt']":# or "Socket error" in outdata:
                    client.cptpause = True
                    for _ in range(2):
                        token__ = await get_cpt_token()
                        if token__:break
                    print(token__, "token__")
                    try:
                        await websocket.send(get_data_msgpack(["cptR", token__]))
                        await websocket.send(data)
                    except:pass
                    client.cptpause = False
                elif str(outdata) == "['cptR', True]":
                    print(outdata);continue
                elif outdata != "['pi']":
                    break
                else:
                    break
            await websocket.close()
        return outdata
    return await ws_connect(userid)

async def sweep_ws(clan_data):
    async def ws_connect(clan_data):
        async def fetch():
            greeting = await websocket.recv()
            greeting = msgpack.unpackb(greeting[0:-2], raw=False)
            return greeting
        ssl_context = ssl._create_unverified_context()
        async with websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context) as websocket:
            output = []
            for username in clan_data:
                data = get_data_msgpack(["r", "clan", username, None, None, None, "0", None])
                await websocket.send(data)
                await asyncio.sleep(0.3)
        
                for _ in range(40):
                    outdata = await fetch()
                    if str(outdata) != "['pi']":
                        break
                    print(outdata)
                    await asyncio.sleep(0.8)
                    
                output.append(outdata)
            await websocket.close()
        return output

    return await ws_connect(clan_data)

missed_cmds = []
async def gb_command_check(msg, cmd, space__ = " ", strict = False, dual = False):
    accepted = functools.partial(gb_command_check_sync, msg, cmd, space__, strict, dual)
    with ThreadPoolExecutor(max_workers = 1) as executor:
        return await client.loop.run_in_executor(executor, accepted)
def gb_command_check_sync(msg, cmd, space__ = " ", strict = False, dual = False):
    if not dual:
        if msg.content.lower().startswith(str(prefix+cmd+space__).lower()) and not strict:
            return True
        elif strict and msg.content.lower() == str(prefix+cmd).lower() and space__ == "":
            return True
        elif strict and msg.content.lower() != str(prefix+cmd).lower():
            return False
        elif msg.content.lower().startswith(str(prefix+cmd).lower()) and space__ != "":
            if msg.id not in missed_cmds:
                missed_cmds.append(msg.id)
            return False
    else:
        if msg.content.lower() == str(prefix+cmd).lower():
            return True
        elif msg.content.lower().startswith(str(prefix+cmd+" ").lower()):
            return True
    return False
def gb_command_fix(msg, cmd, space__ = " "):
    return msg.content[len(prefix)+len(cmd)+len(space__):]
async def post_log(chl, content):
    await chl.send(content)
cool_down_5 = []

ignore_users = [
    # All Users to Ignore
]
patreons = [
    # All patreons
]
patreons_names = [
    # All users to give the patreon badge
]

boosters = [
    # All server booster IGNs
]

double_boosters = [
    # All double server booster IGNs
]
commands_by = {}
muted_users = []
muted_servers = []
commands_in = {}
suggestors = []

dev = 1337 
ghub = 1337
linkers = [
    # All extra linkers
]
devs = [
    # All developer ids
    dev
]
staff = [
    # All staff ids
    dev
]
patreons += staff
admins = [
    # All admins
    dev
]
ignore_users = ignore_users + staff
staff_names = [
    # All staff IGNs
]
blacklisted_servers = ['Krunker comp server']
blacklisted_linking = []
custom_msgs = []

default = (200, 200, 200)
black = (0, 0, 0)
red = (235, 52, 55)
yellow = (251, 192, 45)
purple = (232, 52, 235)
blue = (52, 156, 235)
clan_colors = {}

all_colors = [(237, 20, 61), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 205)] * 12
gb_all_colors = [(255, 0, 221), (93, 0, 255), (232, 153, 231), (209, 68, 252), (136, 140, 247)] * 12
#              Crimson         Orange          Yellow         Lime        Medium Blue
for e_val in range(50):
    if e_val in range(2, 3+1):
        clan_colors[e_val] = black
    if e_val in range(4, 10+1):
        clan_colors[e_val] = red
    if e_val in range(11, 20+1):
        clan_colors[e_val] = yellow
    if e_val in range(21, 30+1):
        clan_colors[e_val] = purple
    if e_val in range(31, 50+1):
        clan_colors[e_val] = blue
color_name_by_code = {
    black: "Black",
    red: "Red",
    yellow: "Yellow",
    purple: "Purple",
    blue: "Blue",
    default: "Gray"}

def roundToNearest(num, near):
    if num > 0:
        return math.ceil(num / near) * near
    elif num < 0:
        return math.floor(num / near) * near
    else: 
        return num
def get_arg(cnt, key):
    for e_cnt in cnt:
        if e_cnt.lower().startswith(key.lower()+":"):
            return e_cnt[len(key)+1:].lower()
maxLevel = 102
def remove_faces(data):
    print(data)
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized') # 
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")

    t = time.time()
    driver = webdriver.Chrome(options=options)
    driver.get("https://face-remover-krunker.blackskull12.repl.co/")
    driver.find_element_by_xpath("//textarea[@id='input']").send_keys(str(data))
    driver.find_element_by_xpath('//button[@onclick="removeFaces()"]').click()
    copy_b = driver.find_element_by_xpath('//button[@onclick="copy()"]')
    while True:
        copy_b.click()
        if (output := driver.find_element_by_xpath("//textarea[@id='output']").get_attribute("value")) != "test":
            old_faces = int(driver.find_element_by_xpath("//textarea[@id='output']").get_attribute("old_face"))
            new_faces = int(driver.find_element_by_xpath("//textarea[@id='output']").get_attribute("new_face"))
            break
        time.sleep(1)
    driver.quit()
    return [output, old_faces, new_faces, time.time()-t]


async def auto_unmute(msg = None, uid = None):
    await asyncio.sleep(60*10)
    if msg != None:
        muted_users.remove(msg.author.id)
    else:
        muted_users.remove(uid)

async def auto_unmute_serv(msg = None, uid = None):
    await asyncio.sleep(60*5)
    if msg != None:
        muted_servers.remove(msg.guild.id)
    else:
        muted_servers.remove(uid)
async def remove_id_from(msg):
    await asyncio.sleep(17)
    try:commands_by[msg.author.id].remove(msg.content.lower())
    except:pass

async def remove_id_from_serv(msg):
    await asyncio.sleep(25)
    try:commands_in[msg.guild.id] -= 1
    except:pass
    
async def remove_id_from_2(msg):
    await asyncio.sleep(60*10)
    try:del suggestors[suggestors.index(msg.author.id)]
    except:pass
async def remove_id_from_3(msg):
    await asyncio.sleep(60*10)
    try:del linkers[linkers.index(msg.author.id)]
    except:pass
async def after_10_secs(msg, tolerance = 0):
    try:
        cmds_by = commands_by[msg.author.id]
    except:return
    cmds_by = {i:cmds_by.count(i) for i in cmds_by}
    if max(cmds_by.values()) > (3 + tolerance) or len(commands_by[msg.author.id]) > (5 + tolerance):
        print("Muted")
        muted_users.append(msg.author.id)
        del commands_by[msg.author.id]
        try:guild__ = msg.guild.name
        except:guild__ = "None"
        await msg.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " WARNING!!", description = "{} has been disregarded for 10 minutes\n**Reason:** Spamming commands".format(msg.author.mention)))
        await client.get_guild(708067789830750449).get_channel(741704072704425984).send("Muted a person - {} - {} - {}".format(msg.author.name,
                                                                                              msg.author.id,
                                                                                              guild__))
        await auto_unmute(msg)
    else:
        client.loop.create_task(remove_id_from(msg))

async def after_10_secs_serv(msg):
    try:
        cmds_in = commands_in[msg.guild.id]
    except:return
    if cmds_in > 10:
        print("Muted Server")
        muted_servers.append(msg.guild.id)
        del commands_in[msg.guild.id]
        try:guild__ = msg.guild.name
        except:guild__ = "None"
        await msg.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " WARNING!!", description = "This server has been disregarded for 5 mins\n**Reason:** Spamming commands - Received more than 15 commands witin 25 seconds"))
        await client.get_guild(708067789830750449).get_channel(741704072704425984).send("Muted a server - {} - {}".format(msg.guild.name,
                                                                                              guild__))
        await auto_unmute_serv(msg)
    else:
        client.loop.create_task(remove_id_from_serv(msg))
def log_data(data):
    try:
        with open("Data/logs.bt", "a") as file:
            file.write(data.encode("utf-8")+"\n")
    except:
        pass
client.banned_words = ['sex', 'gay', 'gae', 'penis', 'porn', 'boobs', 'fuck', 'shit', 'vagina', 'pregnant', 'dick', 'ass', 'suc', 'suck', 'wtf', 'nigger', 'nigga', 'shitter', 'retard', 'cunt', 'hoe', 'pussy', 'bastard']
client.print_cmds = 1
async def do_on_message(msg, tolerance = 0):
    if msg.id in custom_msgs:
        return
    if client.print_cmds:
        try:
            data = "Cmd by {}[{}] in {}   |   '{}'".format(str(msg.author),str(msg.author.id), msg.guild.name, msg.content)
            print(data)
        except:
            data = "Cmd by {}[{}] in {}   |   '{}'".format(str(msg.author),str(msg.author.id), ">dms<", msg.content)
            print(data)
    try:
        commands_by[msg.author.id] += [msg.content.lower()]
    except:
        commands_by[msg.author.id] = [msg.content.lower()]
    try:
        commands_in[msg.guild.id] += 1
    except:
        try:commands_in[msg.guild.id] = 1
        except:pass
    client.loop.create_task(after_10_secs(msg, tolerance))
    client.loop.create_task(after_10_secs_serv(msg))
    


async def cool_down_check(msg):
    if msg.author.id in ignore_users:pass
    elif msg.author.id in cool_down_5 and cool_down_5.count(msg.author.id) >= 2:
        return "Error"
    else:
        cool_down_5.append(msg.author.id)
        client.loop.create_task(update_cool_d(msg.author.id))
async def update_cool_d(__id__):
    await asyncio.sleep(18)
    try:del cool_down_5[cool_down_5.index(__id__)]
    except:pass

async def update_cool_d2(__id__):
    await asyncio.sleep(5.5)
    try:
        del cool_down_5[cool_down_5.index(__id__)]
    except:pass

async def timeout_react(msg):
    try:
        await msg.clear_reactions()
    except:
        await msg.remove_reaction(prev_page, client.user)
        await msg.remove_reaction(stop, client.user)
        await msg.remove_reaction(next_page, client.user)
async def timeout_react_efav(msg, uid):
    try:
        if time.time() - client.efavs_r[uid] > 60:
            try:
                await msg.clear_reactions()
            except:
                await msg.remove_reaction(prev_page, client.user)
                await msg.remove_reaction(stop, client.user)
                await msg.remove_reaction(next_page, client.user)
            del client.efavs_r[uid]
    except:pass
def get_author(msg, user_name):
    try:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        if stat := (old_data[user_name.lower()] == msg.author.id):
            return stat
    except Exception as e:
        print(e)
        return 2

async def get_author_name(msg, user_name, incognito = False, profile = False):
    try:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        if not incognito:
            return await get_u_(old_data[user_name.lower()])
        elif profile and (await get_u_(old_data[user_name.lower()])).id in get_var("incognito") and msg.content.lower() != "g.pf":
            return -1
        elif msg.author.id != old_data[user_name.lower()] and (await get_u_(old_data[user_name.lower()])).id in get_var("incognito"):
            return -1
        else:
            return await get_u_(old_data[user_name.lower()])
    except:
        return ""
async def get_author_obj(msg, uid = None, incognito = True):
    try:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        old_data = {v: k for k, v in old_data.items()}
        if not incognito:
            return old_data[uid if uid != None else msg.author.id]
        elif uid == None:
            return old_data[uid if uid != None else msg.author.id]
        elif uid != None and (await get_u_(uid)).id in get_var("incognito"):
            return ""
        else:
            return old_data[uid if uid != None else msg.author.id]
    except Exception as e:
        print(e)
        return ""

def get_author_list(msg, uid = None, incognito = False):
    try:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        accounts = []
        for k, v in old_data.items():
            if v == (uid if uid != None else msg.author.id):
                accounts.append(k)
        if not incognito:
            return accounts
        elif uid == None:
            return accounts
        elif uid != None and uid in get_var("incognito"):
            return ""
        else:
            return accounts
    except:
        return ""
async def get_author_command(msg, cmd_name, clan_ = False):
    if msg.content.lower() != prefix+cmd_name.lower() and len(msg.mentions) == 0:
        if not clan_:
            output = gb_command_fix(msg, cmd_name)
            if output.isdigit() and len(output) == 18:
                return await get_author_obj(msg, int(output))
            else:return output
        else:
            return {"cn": gb_command_fix(msg, cmd_name),  "is_clan":True}
    elif msg.mentions:
        if not clan_:return await get_author_obj(msg, msg.mentions[0].id)
        else:return {"cn": await get_author_obj(msg, msg.mentions[0].id), "is_clan":False}
    else:
        if not clan_:return await get_author_obj(msg)
        else:return {"cn": await get_author_obj(msg), "is_clan":False}

def get_close_matches(string, all_combs):
    output = {}
    for e_cmd in all_combs:
        output[e_cmd] = lvl.distance(string, e_cmd)
    possible_ = min(output.items(), key=lambda x: x[1])
    return possible_[0] if possible_[1] <= 3 else None
    
async def close_matches(string, all_combs):
    thing = functools.partial(get_close_matches, string, all_combs)
    with ThreadPoolExecutor(max_workers = 1) as executor:
        return await client.loop.run_in_executor(executor, thing)

def append_var(key, obj):
    with open("vars.bt", "rb") as file:
        data = pickle.load(file)
    try:data[key] += obj
    except:data[key] = obj
    with open("vars.bt", "wb") as file:
        pickle.dump(data, file)
def define_var(key, obj):
    with open("vars.bt", "rb") as file:
        data = pickle.load(file)
    data[key] = obj
    with open("vars.bt", "wb") as file:
        pickle.dump(data, file)
def get_var(key):
    with open("vars.bt", "rb") as file:
        data = pickle.load(file)
    return data[key]
def pop_obj_var(key, obj):
    with open("vars.bt", "rb") as file:
        data = pickle.load(file)
    data[key].remove(obj)
    rewrite_data(data)
    

def get_data():
    with open("vars.bt", "rb") as file:
        data = pickle.load(file)
    return data
def rewrite_data(data):
    with open("vars.bt", "wb") as file:
        pickle.dump(data, file)
client.cached_cmds = {}
def compile_channels():
    try:
        return get_var("cmd_chl")
    except:
        return None
def compile_cmds():
    try:
        return get_var("disabled_cmds")
    except:
        return None

async def compile_bgs():
    t = time.time()
    old_data = await async_open("Data/backgrounds.bt")
    client.bgs = old_data
    for e_b in client.bgs["p"]:
        try:
            e_b["file"] = Image.open("Data/backgrounds/"+e_b["file"])
        except Exception as e:print(e)
        await asyncio.sleep(0)
    for e_b in client.bgs["c"]:
        try:
            e_b["file"] = Image.open("Data/backgrounds/"+e_b["file"])
        except Exception as e:print(e)
        await asyncio.sleep(0)
    print("in", time.time()-t, "seconds, backgrounds are loaded")
        
all_commands = ["ping",
                "maps",
                "mods",
                "pf",
                "assets",
                "plays",
                "active",
                "online",
                "map",
                "favs",
                "search",
                "theme",
                "leaders",
                "clan",
                "reg",
                "graph",
                "invite",
                "patreon",
                "help",
                "full_help",
                "find",
                "gameinfo",
                "profile",
                "tc",
                "mod",
                "skin",
                "wars",
                "popular",
                "sweep",
                "link",
                "featured",
                "asset",
                "editor",
                "layout",
                "owners",
                "impressions"
                ]


dev_all_commands = all_commands + ["unlink",
                "sweeper",
                "update_featured",
                "sample",
                "dm",
                "mute",
                "dissmiss",
                "no_dismiss",
                "set_conf",
                "show_conf",
                "statusw",
                "statusp",
                "statusl"]

disableable = [
    "joke",
    "meme",
    "reply",
    "cat",
    "dog",
    "bird",
    "say",
    "warn"

]
each_cmd_help = {
    "maps" : ["Check for user maps", "g.maps <kr-username>", "g.maps Solar13\ng.maps Vince"],
    "map" : ["Check map details", "g.map <map-name>", "g.map Tunnel_Escape\ng.map Caribbean_Escape"],
    "mods" : ["Check for user mods", "g.mods <kr-username>", "g.mods ScamZ\ng.mods Vince"],
    "assets": ["Check for user asets", "g.assets <kr-username>", "g.assets Sidney\ng.assets Vince"],
    "pf": ["Check user profile", "g.pf <kr-username>", "g.pf Sidney\ng.pf Vince"],
    "plays":["Check plays on user maps", "g.plays <kr-username>", "g.plays Solar13\ng.plays Vince"],
    "online":["Check maps with top number of players online\nor Check people online on usermaps", "g.online [kr-username]", "g.online\ng.online Vince"],
    "favs" : ["Check maps added to favourites by a user", "g.favs <kr-username>", "g.favs Arcaner\ng.favs Sidney"],
    "search":["Search for maps using keyword", "g.search <keyword>", "g.search Zombie\ng.search Run"],
    "clan": ["Check a clan", "g.clan <clan-name>", "g.clan Verb"],
    "reg" : ["Register user before using graphs. Data will be updated every 24 hours after registration", "g.reg <kr-username>", "g.reg Eskrr"],
    "graph":["Check graph of plays and likes of a map\nYou must be registered before using graphs", "g.graph <map-name>", "g.graph HowMany"],
    "sweep":["Check new score earned by clan members within 24 hours", "g.sweep <clan-name>\ng.sweeper help", "g.sweep .map"],
    "find":["""Search through active games. You can apply filters such as maximum players, available vacant seats.
```css
g.find [map-name] [-u] [-p] [-mp <val>] [-vs <val>]
-u   ->  Turns off blacklist word filter
-p   ->  Turns off player count filter
-mp  ->  Number of maximum players
-vs  ->  Set minimum vacant seats / available slots for players
```""",
            "g.find [map-name] [-u] [-p] [-mp <val>] [-vs <val>]",
            "g.find\ng.find Zombie\ng.find Zombie -u -p\ng.find -u -p -mp 10\ng.find Arena -p -u -mp 10 -vs 5"],
    "gameinfo":["View live details about a hosted game", "g.gameinfo <url>", "g.gameinfo https://krunker.io/?game=MIA:gvaxz"],
    "leaders":["Check the leaderboard\n*Read help context to see possible keys*", "g.leaders <key>", "g.leaders kills\ng.leaders wins"],
    "patreon":["View the official patreon page. Support us on patreon and get plenty of benefits", "g.patreon", "g.patreon"],
    "help":["View the help context","g.help","g.help\ng.help_here\ng.help maps"],
    "skin" : ["Check a skin using its name.\nYou can also get texture files by adding `-t` at the end of the command", "g.skin <skin-name>\ng.skin <skin-name> -t", "g.skin Omen\ng.skin Saphire\ng.skin Blue Poly -t"],
    "mod" : ["Check mod details", "g.mod <mod-name>", "g.mod Stremz_Mod\ng.mod csong"],
    "say": ["Dev/Patron only command", "g.say <message>", "g.say Lmao\n.gsay This bot is awesome"],
    "link":["""Get your discord account linked with your krunker username to have plenty of benefits and ease.
 - You can use `g.pf` without your username to check your stats, `g.maps`, and so on...
 - Shows your discord name and tag on your profile
 - You can find other's in-game names quickly""", "g.link <kr-username>", "g.link Sidney\ng.link abc"],
    "alts":["Get list of your linked accounts", "g.alts\ng.alts <id/mention>", "g.alts\ng.alts @abc"],
    "alts set":["Set one of your linked accounts as your main account", "g.alts set", "g.alts set"],
    "layout":["**Image to Layout Converter**  (WIP)\nImplemented in Gamebot. \n#####   **__Use `g.layout`__ in #bot-commands **   #####\n\nConverts an image to layout. *You can define how much to scale the layout. Black pixels in the image define the platform.*\n\n__**NOTE**__: \n- Image must be 100x100 or lower in dimensions*(If its bigger, you wont get good results)*\n - Image must not contain round figures, if it does, the object count will be high *(For a correct image made for layout, the object count is 5-30 depending on number of paths in the layout)*",
              "g.layout", "g.layout"],
    "chl": ["Configure channel for gamebot in your server. You can add multiple channels where bot commands can be used. Once you select first channel, commands will only work in that channel.",
            "\ng.set_chl #channel\ng.list_chl\ng.del_chl #channel", "g.set_chl #channel\ng.list_chl\ng.del_chl #channel"],
    "applications": ["Set minimal stats for your clan server which are required to join your clan. Its an extension of `g.apply` command",
                     "g.applications", "g.applications"],
    "apply": ["Check if you are qualified for the clan or not. You must use this command in the clan server you are applying for. For owner, you have to enable `g.application` first.",
              "g.apply <kr-username>", "g.apply SheriffCarry"],
    "tinyurl": ["Makes a url tiny for easy sharing", "g.tinyurl <url>",
                "g.tinyurl https://krunker.io"],
    "meme": ["View a refreshing meme. Might contain bad words, if you want to disable if for your server, use `g.help cmds`",
             "g.meme", "g.meme"],
    "cmds": ["You can disable fun commands. Those commands wont be accessible in your server unless you re-enable them. Use `g.disable <cmd-name>`. To re-enable it, use `g.enable <cmd-name>`. To get a list of disabled commands, use `g.cmds`.",
             "g.disable <cmd-name>\ng.enable <cmd-name>\ng.cmds", "g.disable <cmd-name>\ng.enable <cmd-name>\ng.cmds"],
    "%": ["Using `%` in command acts as the username of the person you last checked the stats of.",
          "\ng.maps %\ng.pf %", "g.maps %\ng.pf %\ng.clan %"],
    "class": ["View information about a class", "g.class <class-name>", "g.class Hunter"],
    "cstats": ["View your stats of a specific class", "g.cstats <kr-username>", "g.cstats Sidney"],
    "background":["""You can get yourself a background:
```diff
+ Become a supporter on patreon 
- Win it in a giveaway
```
*Useful commands below:*
""", "g.server\ng.pf transparent\ng.patreon", "g.server"],
    "theme": ["Get yourself three refreshing themes for map making in a go", "g.theme", "g.theme"],
    "editor": ["Import your map to start using editor features", "g.editor\ng.editor help", "g.editor"],
    "owners": ["Get list of all owners of an item or a skin","g.owners <skin-name>", "g.owners Blue Poly"],
    "incognito": ["Toggle your account's publicity", "g.incognito", "g.incognito"],
    "hub": ["Get direct social links to the input.", "g.hub <input>", "g.hub Sidney"],
    "profit": ["Calculte profit you get on selling a skin.", "g.profit <buy-price> <sell-price>", "g.profit 500 650"],
    "posts": ["View the posts of a user. You can post stuff at [Krunker Social](https://krunker.io/social)",
              "g.posts <kr-username>", "g.posts Sidney"],
    "impressions": ["Check views you got on your profile.", "g.impressions [username]", "g.impressions Sidney"]
    
    
}
def write_clan_name(draw, xy, rank, text, font, font2, outline_c = (0, 0, 0)):
    
    if rank == 1:
        if outline_c:
            draw.text((xy[0]-1, xy[1]), text, outline_c, font = font)
            draw.text((xy[0]+1, xy[1]), text, outline_c, font = font)
            draw.text((xy[0], xy[1]-1), text, outline_c, font = font)
            draw.text((xy[0], xy[1]+1), text, outline_c, font = font)
            draw.text((xy[0]+1, xy[1]+1), text, outline_c, font = font)
            draw.text((xy[0]-1, xy[1]-1), text, outline_c, font = font)

        twidth = generate_colored_text(xy[0], xy[1], text, font, draw)
        outline_c
    else:
        try:
            clan_color = clan_colors[rank]
        except:
            clan_color = (255, 255, 255)
        if text.lower() == "dev":
            clan_color = (64, 196, 255)
        if text.isascii():
            twidth, _ = draw.textsize(text, font=font)
            draw.text((xy[0], xy[1]), text, clan_color, font = font, stroke_width = 1, stroke_fill = outline_c)
        else:
            twidth = draw_non_acsii(xy[0], xy[1], text, font, font2, clan_color, draw, stroke_width = 1, stroke_fill = outline_c)
    return twidth


def write_non_chars(draw, xy, text, font, font2, color = (150, 150, 150), outline_c = (70, 70, 70), outline_stroke = 0):
    twidth = draw_non_acsii(xy[0], xy[1], text, font, font2, color, draw, stroke_width = outline_stroke, stroke_fill = outline_c)
    return twidth
            
def rec_ramps(img):
    objects = []
    pixels = img.load()
    while True:
        obj_x = []
        obj_y = []
        current_obj_y = []
        break_ = 0
        found_range = False
        for y in range(img.size[1]):
            current_obj_x = []
            if not found_range:
                for x in range(img.size[0]):
                    p_c = list(pixels[x, y])
                    if p_c == [255, 0, 0] and not current_obj_x:
                        found_range = True
                        current_obj_x.append(x-1)
                        current_obj_y.append(y)
                    if p_c != [255, 0, 0] and found_range:
                        current_obj_x.append(x-1)
                        break
            if obj_x == []:
                obj_x = current_obj_x
            else:
                if len(obj_x) == 1:
                    obj_x.append(img.size[1]-1)
                for e_x in range(obj_x[0]+1, obj_x[1]+1):
                    if list(pixels[e_x, y]) != [255, 0, 0]:
                        current_obj_y.append(y)
                        break
                    elif y == img.size[0]-1 and len(current_obj_y) <= 1:
                        current_obj_y.append(y+1)
                    

            if len(current_obj_y) >= 2:
                obj_y = current_obj_y
                green = [0, 255, 0]
                if list(pixels[obj_x[0], obj_y[0]]) == green:
                    axis = "-x"
                elif list(pixels[obj_x[1], obj_y[0]-1]) == green:
                    axis = "-y"
                    obj_y[0] -= 1
                elif list(pixels[obj_x[1]+1, obj_y[0]]) == green:
                    axis = "x"
                    obj_x[1] += 1
                    obj_x[0] -= 1
                else:
                    axis = "y"
                    obj_y[1] += 1
                objects.append([obj_x, obj_y, axis])
                for e_y in range(current_obj_y[0]+1, current_obj_y[1]+1):
                    for e_x in range(obj_x[0]+2, obj_x[1]+2):
                        pixels[e_x-1, e_y-1] = (255, 255, 255)
                break
        if (255, 0, 0) not in [v for k,v  in list(dict(img.getcolors(img.size[0]*img.size[1])).items())]:break
    return objects
    


def unwrap_image(img, scale, lay_y = 10, accuracy = True, y_pos_in = 0, invert = False, if_ramps = True):
    objects = []
    pixels = img.load() # create the pixel map
    bumps = 0
    for y in range(img.size[1]):
        found_b = False
        for x in range(img.size[0]):
            try:
                p_c = list(pixels[x, y])
            except Exception as e:
                raise e
            if p_c != [0, 0, 0] and not found_b:
                found_b = True
                bumps += 1
                
            elif p_c  == [0, 0, 0] and found_b:
                found_b = False
    if bumps > 1000:return bumps
    while True:
        obj_x = []
        obj_y = []
        current_obj_y = []
        break_ = 0
        found_range = False
        for y in range(img.size[1]):
            current_obj_x = []
            if not found_range:
                for x in range(img.size[0]):
                    p_c = list(pixels[x, y])
                    if p_c == [0, 0, 0] and not current_obj_x:
                        found_range = True
                        current_obj_x.append(x-1)
                        current_obj_y.append(y)
                    if p_c != [0, 0, 0] and found_range:
                        current_obj_x.append(x-1)
                        break
            if obj_x == []:
                obj_x = current_obj_x
            else:
                if len(obj_x) == 1:
                    obj_x.append(img.size[1]-1)
                for e_x in range(obj_x[0]+1, obj_x[1]+1):
                    if list(pixels[e_x, y]) != [0, 0, 0]:
                        current_obj_y.append(y)
                        break
                    elif y == img.size[0]-1 and len(current_obj_y) <= 1:
                        current_obj_y.append(y+1)
                    

            if len(current_obj_y) >= 2:
                obj_y = current_obj_y
                objects.append([obj_x, obj_y])
                for e_y in range(current_obj_y[0]+1, current_obj_y[1]+1):
                    for e_x in range(obj_x[0]+2, obj_x[1]+2):
                        pixels[e_x-1, e_y-1] = (255, 255, 255)
                break
        if (0, 0, 0) not in [v for k,v  in list(dict(img.getcolors(img.size[0]*img.size[1])).items())]:break
    if if_ramps:
        ramps = rec_ramps(img)
        objects += ramps
    map_objects = []
    def get_int_or_f(val, choice):
        if not choice:return int(val)
        else:return val
    axes = {
        "y": 1,
        "x": 0,
        "-y": 3,
        "-x": 2
    }
    for map_obj in objects:
        
        p_x_pos = ((map_obj[0][0]+(map_obj[0][1]-map_obj[0][0])/2)*scale)/2

        p_y_pos = ((map_obj[1][0]+(map_obj[1][1]-map_obj[1][0])/2)*scale)/2
        future_obj = {
                "p": [get_int_or_f(p_x_pos, accuracy),
                      y_pos_in,
                      get_int_or_f(p_y_pos, accuracy)],
                
                "s": [get_int_or_f(((map_obj[0][1]-map_obj[0][0])/2)*scale, accuracy),
                      lay_y,
                      get_int_or_f(((map_obj[1][1]-map_obj[1][0])/2)*scale, accuracy)]
            }
        try:
            map_obj[2]
            
            future_obj["i"] = 9
            future_obj["d"] = axes[map_obj[2]]
            if not invert:
                future_obj["s"][1] = (0 - y_pos_in)
                future_obj["p"][1] = y_pos_in + lay_y
            else:
                future_obj["s"][1] = y_pos_in 
                future_obj["p"][1] = 0 + lay_y
                future_obj["d"] += 2
                if future_obj["d"] > 3:
                    future_obj["d"] -= 3
        except:pass
        map_objects.append(future_obj)
    return map_objects

async def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = await await_get(apiurl + url)
    return tinyurl
async def start_loading(msg):
    await msg.add_reaction(loading)
client.dev_mode = 1
@client.event
async def on_message(message):
    if str(message.content).startswith("<@!717416553099952219>"):
        if (new_out := message.content.replace("<@!717416553099952219> ", "g.", 1)) == message.content:
            new_out = message.content.replace("<@!717416553099952219>", "g.", 1)
        message.content = new_out
        del message.mentions[0]
    if message.content.startswith("https://krunker.io/?game="):
        message.content = "g.lgameinfo " +message.content
    if not message.content.lower().startswith("g."):return
    
    msg = message
    chl = msg.channel
    if msg.author.id not in devs and client.dev_mode == 1:
        return
    try:
        guild_id = msg.guild.id
        guild_name = msg.guild.name
    except:
        guild_id = 0
        guild_name = ">dms<"
    try:
        client.compiled_chls[msg.guild.id]
        if msg.channel.id not in client.compiled_chls[msg.guild.id]:
            return
    except:pass
    
    try:
        client.compiled_cmds[msg.guild.id]
        if msg.content.lower().split(" ")[0][2:] in client.compiled_cmds[msg.guild.id]:
            return
        elif msg.content.lower().split(" ")[0][2:][:-1] in client.compiled_cmds[msg.guild.id]:
            return

    except:pass
    
    if message.author == client.user or message.author.id in muted_users or guild_id in muted_servers or message.author.bot:
        return

    elif message.guild == None and msg.author.id not in patreons:
        return

    elif message.content.lower() == "g.":
        client.loop.create_task( do_on_message(msg, 1))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        await message.channel.send("Do you need my help?\nGet started using `g.help`")
    

    elif (await gb_command_check(msg, "maps", "", dual = True)) or (await gb_command_check(msg, "games", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        try:
            if msg.content.lower().startswith("g.maps"):
                if not (user_name := (await get_author_command(msg, "maps"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            elif msg.content.lower().startswith("g.games"):
                if not (user_name := (await get_author_command(msg, "games"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if len(user_name) > 22:
                await emb_send(chl, warning+ " Account not found!");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
                
            #fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Counting..."))
            client.loop.create_task(start_loading(msg))
            async with aiofiles.open(pfp_id_file, "rb") as file:
                ppl_ids = pickle.loads(await file.read())
            ppl_ids = {k.lower(): v for k, v in ppl_ids.items()}
            try:ppl_id = ppl_ids[user_name.lower()]
            except:
                data = await get_user_data(user_name)
                try:
                    is_verified = data[3]['player_featured']
                    ppl_id = data[3]['player_id']
                except:
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found!", description = "Make sure you are using the correct user name."))
                    await msg.remove_reaction(loading, client.user);return
            all_maps = []
            for c_ind in range(5):
                custom_api_maps_url = "https://api.krunker.io/maps?index=5&pos={}&accountId={}"
                hosts_htm = await await_get(custom_api_maps_url.format(c_ind, ppl_id))
                maps = json.loads(hosts_htm)['data']
                all_maps += maps
                if len(maps) < 30 or not maps:break
            try:
                is_verified
            except:
                try:
                    cached_data_ver = client.scache[user_name.lower()]
                    is_verified = cached_data_ver["player_featured"]
                except Exception as e:
                    is_verified = 0
            maps = all_maps
            plays = 0
            total_likes = 0
            for e_map in maps:
                try:plays += e_map["map_pl"]
                except:pass
                try:total_likes += e_map["map_votes"]
                except:pass

            mid_maps = {}
            for e_map in maps:
                mid_maps[e_map["map_name"]] = e_map["map_id"]

            async with aiofiles.open(featured_maps_file, "rb") as file:
                old_data = pickle.loads(await file.read())
            sorted_maps = []
            for e_map in maps:
                if e_map['map_name'].lower() in old_data:
                    e_map['map_featured'] = 0
                else:e_map['map_featured'] = None
                
            async with aiofiles.open(map_file, "rb") as file:
                old_data = pickle.loads(await file.read())
            user_exists = user_name.lower() in [e_user[0] for e_user in old_data]
            if not user_exists:
                new_str = [user_name.lower()]
                new_dict = {}
                for e_map in maps:
                    new_dict[e_map['map_name'].replace("'","")] =  e_map['map_votes']
                new_str.append(new_dict)
                old_data.append(new_str)
                async with aiofiles.open(map_file, "wb") as file:
                    await file.write(pickle.dumps(old_data))
                    
            for e_user in old_data:
                user_exists = 0
                if e_user[0].replace("'","") == user_name.lower().replace("'",""):
                    user_exists = 1
                    for e_map in maps:
                        map_data = e_user[1]
                        try:sorted_maps.append([e_map['map_name'].replace("'",""), map_data[e_map['map_name']], e_map['map_votes'], e_map['map_verified']])
                        except Exception as e:sorted_maps.append([e_map['map_name'].replace("'",""), e_map['map_votes'], e_map['map_votes'], e_map['map_verified']])
            with open("Data/timestamps.bt", "rb") as file:
                stamp_data = pickle.load(file)
            
            try:
                last_timestamp = stamp_data["maps"][user_name.lower()]
            except:
                last_timestamp = None
                
            if get_author(msg, user_name):
                with open(map_file, "wb") as file:
                    indexes = [i for i,x in enumerate(old_data) if x[0] == user_name.lower()][0]
                    del old_data[indexes]
                    new_str = [user_name.lower()]
                    new_dict = {}
                    for e_map in maps:
                        new_dict[e_map['map_name'].replace("'","")] =  e_map['map_votes']
                    new_str.append(new_dict)
                    old_data.append(new_str)
                    pickle.dump(old_data, file)
                stamp_data["maps"][user_name.lower()] = int(time.time())
                with open("Data/timestamps.bt", "wb") as file:
                    pickle.dump(stamp_data, file)
            final_maps = []
            for e_map in sorted_maps:
                final_maps.append([e_map[0], e_map[2], e_map[2]-e_map[1], e_map[-1]])
            final_maps = sorted(final_maps, key = lambda x: x[1], reverse = True)
            


            
            maps = sorted(maps, key = lambda x: x["map_votes"], reverse = True)

            try:
                user_name = maps[0]['creatorname']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "No usermaps found!"))
                await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            with open("Data/plays.bt", "rb") as file:
                old_data = pickle.load(file)
            try:
                last_plays = old_data[user_name.lower()]
                indv_plays = last_plays[-1]
            except Exception as e:
                last_plays = old_data[user_name.lower()] = [plays, {e_map["map_name"].lower(): e_map["map_pl"] for e_map in maps}]
                indv_plays = last_plays[-1]
            
            if get_author(msg, user_name):
                with open("Data/plays.bt", "wb") as file:
                    old_data[user_name.lower()] = [plays, {e_map["map_name"].lower(): e_map["map_pl"] for e_map in maps}]
                    pickle.dump(old_data, file)
            def get_x_val(draw, text, font):
                twidth, _ = draw.textsize(text, font=font)
                return twidth
            def filter_color(verification):
                if verification == 0:return (255, 203, 73)
                return Main_Color
                #return (255, 0, 255)
            def filter_votes(votes):
                if not votes:return [13, (100, 100, 100), '', '', votes]
                elif votes > 0 and votes <= 100:return [0, (15, 220, 15), '+', '', votes]
                elif votes < 0: return [6, (235, 10, 10), '', '', votes]
                elif votes > 100:return [0, (15, 220, 15), '+', '', votes]
            def filter_votes_2(votes):
                if not votes:return [13, (100, 100, 100), '', '', votes]
                elif votes > 0 and votes <= 100:return [0, (15, 220, 15), '+', '', votes]
                elif votes < 0: return [6, (235, 10, 10), '', '', votes]
                elif votes > 100:return [0, (15, 220, 15), '+', '', votes]
            def get_cord(new_plays):
                if len(str(new_plays)) <= 1:return 408
                if len(str(new_plays)) <= 2:return 420
                elif len(str(new_plays)) <= 3:return 432
                elif len(str(new_plays)) <= 5:return 460
                else:return 499
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
            
            total_maps = maps
            try:maps = total_maps[:20];has_pages = True
            except:has_pages = False
            main_pages = math.ceil(len(total_maps)/20)
            current_page = 1
            start = 0
            started = False
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == main_pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page -= 1
                    thing = functools.partial(make_maps, maps, user_name, last_timestamp, plays, last_plays, main_pages, filter_color, filter_votes, filter_votes_2, get_cord, final_maps, start, get_x_val, total_likes, current_page, indv_plays, is_verified, mid_maps)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
        
                    ask = await message.channel.send(file=discord.File(byte_io, "unknown.png"))
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages or main_pages == 1:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "e.maps", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not (user_name := (await get_author_command(msg, "e.maps"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            client.loop.create_task(start_loading(msg))
            data = await get_user_data(user_name)
            try:maps = data[4]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            
            try:user_name = data[3]['player_name']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No account found"))
                await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No user maps found"))
                await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return


            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
            
            pages = math.ceil(len(maps)/10)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            ask = None
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 10
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 10
                            current_page -= 1
                    ask = await post_emb_page(ask, maps, user_name, msg, start = start, pages_ = current_page, pages_main = pages, arg1 = "map_name", arg2 = "creatorname", arg3 = "map_votes", sort_key = "map_votes", reverse_sort = True, d_maps = True)
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                    
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "i.maps", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not (user_name := (await get_author_command(msg, "i.maps"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            client.loop.create_task(start_loading(msg))
            with open(pfp_id_file, "rb") as file:
                ppl_ids = pickle.load(file)
            ppl_ids = {k.lower(): v for k, v in ppl_ids.items()}
            try:ppl_id = ppl_ids[user_name.lower()]
            except:
                data = await get_user_data(user_name)
                try:ppl_id = data[3]['player_id']
                except:
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found!", description = "Make sure you are using the correct user name."))
                    await message.add_reaction(warning);await msg.remove_reaction(loading, client.user);return
            all_maps = []
            for c_ind in range(5):
                custom_api_maps_url = "https://api.krunker.io/maps?index=5&pos={}&accountId={}"
                hosts_htm = await await_get(custom_api_maps_url.format(c_ind, ppl_id))
                maps = json.loads(hosts_htm)['data']
                all_maps += maps
                if len(maps) < 30 or not maps:break
            maps = all_maps
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No user maps found"))
                await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            #maps = [e_map["mna"] for e_map in maps]
            sum_of_kr = 0
            sum_of_doll = 0
            for e_map in maps:
                sum_of_kr += e_map["fund"]
                sum_of_doll += e_map["map_pl"]/1250
                e_map["kr"] = "{:,.2f}".format(e_map["fund"])
                e_map["doll"] = "{:,.2f}".format(e_map["map_pl"]/1250)
            sum_of_kr = "{:,}".format(sum_of_kr)
            sum_of_doll = "{:,.2f}".format(sum_of_doll)

            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id



            pages = math.ceil(len(maps)/10)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            ask = None
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 10
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 10
                            current_page -= 1
                    ask = await post_info_page(ask, maps, user_name, msg, start = start, pages_ = current_page, pages_main = pages, arg1 = "map_name", arg2 = "creatorname", arg3 = "map_votes", sort_key = "map_votes", reverse_sort = True, d_maps = True, sum_of_kr = sum_of_kr, sum_of_doll =sum_of_doll)
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "mods", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        try:
            if not (user_name := (await get_author_command(msg, "mods"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            data = await get_user_data(user_name)
            try:maps = data[5]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            
            if data == ['cpt']:
                data = [0, 0, 0, client.scache[user_name.lower()], 0]
            
            #maps = [{'map_name': 'Waterfall_Inf', 'map_votes': 1412, 'map_verified': None}, {'map_name': 'Disaster', 'map_votes': 1, 'map_verified': None}]
            try:user_name = data[3]['player_name']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No account found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No user mods found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            sorted_maps = []
            with open(mod_file, "rb") as file:
                old_data = pickle.load(file)
                #[[user,{map:votes}]
            user_exists = user_name.lower() in [e_user[0] for e_user in old_data]
            if not user_exists:
                new_str = [user_name.lower()]
                new_dict = {}
                for e_map in maps:
                    new_dict[e_map['mod_name'].replace("'","")] =  e_map['mod_votes']
                new_str.append(new_dict)
                old_data.append(new_str)
                with open(mod_file, "wb") as file:
                    pickle.dump(old_data, file)
            for e_user in old_data:
                user_exists = 0
                if e_user[0].replace("'","") == user_name.lower().replace("'",""):
                    user_exists = 1
                    for e_map in maps:
                        map_data = e_user[1]
                        try:
                            sorted_maps.append([e_map['mod_name'].replace("'",""), map_data[e_map['mod_name']], e_map['mod_votes'], e_map['mod_featured']])
                        except Exception as e:
                            print(e)
                            sorted_maps.append([e_map['mod_name'].replace("'",""), e_map['mod_votes'], e_map['mod_votes'], e_map['mod_featured']])
            if get_author(msg, user_name):
                with open(mod_file, "wb") as file:
                    indexes = [i for i,x in enumerate(old_data) if x[0] == user_name.lower()][0]
                    del old_data[indexes]
                    new_str = [user_name.lower()]
                    new_dict = {}
                    for e_map in maps:
                        new_dict[e_map['mod_name'].replace("'","")] =  e_map['mod_votes']
                    new_str.append(new_dict)
                    old_data.append(new_str)
                    pickle.dump(old_data, file)
            final_maps = []
            for e_map in sorted_maps:
                final_maps.append([e_map[0], e_map[2], e_map[2]-e_map[1], e_map[-1]])
            final_maps = sorted(final_maps, key = lambda x: x[1], reverse = True)
            
            thing = functools.partial(make_mods, final_maps, user_name, client, featured_maps_file)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
                    
            await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            await fetching.delete()
            client.scache[user_name.lower()] = data
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e






        
    elif (await gb_command_check(msg, "help", "")):
        
        client.loop.create_task( do_on_message(msg))
        embed = discord.Embed(colour=discord.Colour(14423783), description="""
[Support Server](https://discord.gg/coming-soon) | [Invite Url](https://discord.com/api/oauth2/authorize?client_id=coming-soon&permissions=129088&scope=bot) | [Support us on Patreon](https://www.patreon.com/ComingSoonBTW)

**Prefix:**  `g.`

__**Commands:**__

**Profile**
> ```css
> g.pf <kr-username
> g.link <kr-username>
> g.maps <kr-username>
> g.mods <kr-username>
> g.assets <kr-username>
> g.cstats <kr-username>
> g.posts <kr-username>
> g.stats```

**Account Linking & Background**
> ```css
> g.link <kr-username>
> g.unlink <kr-username>
> g.incognito
> g.alts
> g.alts set
> g.pbg <user-name>
> g.cbg <clan-name>```

**Maps**
> ```css
> g.map <map-name>
> g.online [kr-username]
> g.favs <kr-username>
> g.search <keyword>
> g.theme```

**Servers**
> ```css
> g.find [map-name] [-u] [-p] [-mp <val>] [-vs <val>]
> g.online
> g.gameinfo <game-url>
> g.popular
> g.featured```

**Map Editing**
> ```css
> g.editor
> g.layout
> g.editor help```

**Leaderboards & Skins**
> ```css
> g.leaders <key> key: [level][kills][wins][time][kr][clans][1v1][2v2][4v4][challenge][egg][wars]
> g.skin <skin-name> [-t]
> g.owners <skin-name>```

**Clans & Others**
> ```css
> g.clan <clan-name>
> g.wars [clan-name] [region:<re>]
> g.leaders wars
> g.applications
> g.apply <kr-username>
> g.mod <mod-name>
> g.asset <asset-name>
> g.hub <name>
> g.class <class-name>
> g.update [version]```

**Graphs & Sweeps**
> ```css
> g.reg <kr-username>
> g.graph <map-name>
> g.sweeper help```

""")
        embed2 = discord.Embed(colour=discord.Colour(14423783), description="""

**Fun Stuff**
> ```css
> g.reply <msg>
> g.cat
> g.dog
> g.bird
> g.joke
> g.meme
> g.tinyurl <url>```

**Server Management:**
> ```css
> g.set_chl <#channel>
> g.list_chl
> g.auto_manage help
> g.levels
> g.auto_updates #<channel>```

**Utility**
> ```css
> g.staff
> g.invite
> g.patreon
> g.ping
> g.help
> g.help <module>
> g.full_help```

[Support Server](https://discord.gg/coming-soon) | [Invite Url](https://discord.com/api/oauth2/authorize?client_id=coming-soon&permissions=129088&scope=bot) | [Support us on Patreon](https://www.patreon.com/ComingSoonBTW)

For more support, visit [Support Server](https://discord.gg/coming-soon) or use `g.staff`
_`<>` are not needed when using commands_\n
_Syntax: <> required, [] optional_""")

        embed.set_author(name="Help", icon_url="https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
        embed2.set_footer(text="Made by 39x. Check the bot out on Github: https://github.com/39x/GameBot.")

        try:
            if msg.content.lower() == "g.help_here":
                raise TimeoutError()
            else:
                raw_desc = """
**Description:** {}

**Usage:**
{}

**Examples:**
{}
"""
                for each_cmd in each_cmd_help.keys():
                    if msg.content.lower().endswith(each_cmd) and msg.content.lower() != "g.help":
                        embed = discord.Embed(colour=discord.Colour(14423783),
                                              description=raw_desc.format(
                                                  each_cmd_help[each_cmd][0],
                                                  each_cmd_help[each_cmd][1],
                                                  each_cmd_help[each_cmd][2]
                                                  ))
                        embed.set_author(name="Command: "+each_cmd.title(), icon_url="https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
                        await message.channel.send(embed= embed)
                        return
                if msg.content.lower() != "g.help":
                    await emb_send(chl, warning+" No help documentation found on module!");return
            await message.author.send(embed = embed)
            await message.author.send(embed = embed2)
            if not message.guild == None: await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783),title = mail+ " You've received mail!"))
        except:

            await message.channel.send(embed= embed)
            await message.channel.send(embed = embed2)
    


    elif (await gb_command_check(msg, "online", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        randomize = bool(msg.content.lower() == "g.online")
        if not randomize:
            user_name = gb_command_fix(msg, "online")
        try:
            counting = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+" Counting..."))
            
            host_data = client.lobbies
            if not randomize:
                with open("Data/usermaps.bt", "rb") as file:
                    old_data = pickle.load(file)
                try:
                    raise TimeoutError()
                    #maps = old_data[user_name.lower()]
                except:
                    if user_name == "%":
                        try:user_name = client.cached_cmds[msg.author.id]
                        except Exception as e:print(e);user_name = "%"
                    elif user_name == "\%":
                        user_name = "%"
                    else:
                        client.cached_cmds[msg.author.id] = user_name.lower()
                    try:
                        maps = client.scache[user_name.lower()]["player_maps"]
                    except:
                        data = await get_user_data(user_name)
                        try:
                            maps = data[4]
                            if maps == None:raise TypeError()
                        except:
                            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No user maps found", description = "Make sure you are using the correct user name"))
                            await counting.delete()
                            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                            return
                    maps = old_data[user_name.lower()] = [e_map['map_name'] for e_map in maps]
                    with open("Data/usermaps.bt", "wb") as file:pickle.dump(old_data, file)
                if not len(maps):
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No user maps found", description = "Note that command has been changed to `g.online <kr-username>`"))
                    await counting.delete()
                    if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                    return
                #for e_map in maps:games_o[e_map] = [0, 0]
                thing = functools.partial(gonline_p1, maps, host_data)
                with ThreadPoolExecutor(max_workers = 1) as executor:
                    games_o, overall_online = await client.loop.run_in_executor(executor, thing)
                    
            else:
                user_name = ""
                thing = functools.partial(gonline_p2, host_data, client)
                with ThreadPoolExecutor(max_workers = 1) as executor:
                    games_o, overall_online = await client.loop.run_in_executor(executor, thing)
                
            if not len(games_o):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No online players found on usermaps"))
                await counting.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            with open(featured_maps_file, "rb") as file:
                old_data = pickle.load(file)
            
            thing = functools.partial(make_online, games_o, user_name, randomize, client, old_data, overall_online)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
            
            await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            #await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "{} players are playing {} right now.".format(counts, map_name)))
            await counting.delete()
            
        except Exception as e:
            await message.channel.send("An error occured. Please try later.")
            await counting.delete()
            raise e    
    
        
    elif (await gb_command_check(msg, "assets", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not (user_name := (await get_author_command(msg, "assets"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            data = await get_user_data(user_name)
            if data == ['cpt']:
                data = client.scache[user_name.lower()]
            #print(data)
            #data = ['0', 'profile', 'GraphiteEater', {'player_name': 'GraphiteEater', 'player_id': 2721181, 'player_kills': 11924, 'player_wins': 494, 'player_games_played': 696, 'player_deaths': 4258, 'player_timeplayed': 253252602, 'player_funds': 274, 'player_score': 1375495, 'player_featured': 1, 'player_clan': 'MMOK', 'player_hack': 0, 'player_following': 0, 'player_followed': 4, 'player_stats': '{"c":9,"s":123970,"h":37098,"r4":120,"c0":768655,"mk":384,"r2":12,"hs":6503,"c1":341960,"c9":4085,"c2":23840,"c5":2345,"c6":18070,"c4":9450,"n":19,"c11":63390,"c12":1790,"wb":91,"c3":51910,"c8":900,"c7":350,"chgP":"15:0,115","flg":235}', 'player_datenew': '2019-04-09T19:39:10.000Z', 'player_elo': 0, 'player_region': 4, 'player_type': 0, 'player_elo2': None, 'player_elo4': None, 'player_chal': 15, 'player_infected': 1, 'player_eventcount': None, 'player_premium': 5443201000.0, 'partner_approved': 0}, [{'map_name': 'zombie_bhop_corn', 'map_votes': 114, 'map_verified': None, 'map_date': '2020-04-18T14:41:59.000Z', 'map_id': 20822, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Titan_Wars', 'map_votes': 21, 'map_verified': 0, 'map_date': '2020-02-22T00:18:35.000Z', 'map_id': 18868, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Oil_Rig_V1', 'map_votes': 8, 'map_verified': None, 'map_date': '2019-04-17T14:20:54.000Z', 'map_id': 8547, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Canal___', 'map_votes': 5, 'map_verified': None, 'map_date': '2019-06-19T12:44:40.000Z', 'map_id': 11400, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Studio', 'map_votes': 2, 'map_verified': None, 'map_date': '2019-05-28T20:19:07.000Z', 'map_id': 10747, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Bill', 'map_votes': 0, 'map_verified': None, 'map_date': '2019-04-21T12:10:03.000Z', 'map_id': 9274, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Tank_Test', 'map_votes': 0, 'map_verified': None, 'map_date': '2020-07-02T17:22:19.000Z', 'map_id': 103535, 'map_info': '{}', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'Mech_Submission', 'map_votes': 0, 'map_verified': None, 'map_date': '2019-04-17T18:06:27.000Z', 'map_id': 9002, 'map_info': '', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}, {'map_name': 'I_wonder_if_dash', 'map_votes': 0, 'map_verified': None, 'map_date': '2020-07-01T22:35:32.000Z', 'map_id': 103475, 'map_info': '{}', 'creatorname': 'GraphiteEater', 'map_updatecounter': 0}], [], None, [{'id': 1060, 'nm': 'FinalFinalFinal', 'cat': 0, 'ini': '2020-07-07T23:29:58.000Z', 'siz': 3636, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 1059, 'nm': 'UndergrowthFinal', 'cat': 0, 'ini': '2020-07-07T22:37:47.000Z', 'siz': 3636, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 1030, 'nm': 'DoNotUse', 'cat': 0, 'ini': '2020-07-06T18:59:49.000Z', 'siz': 320, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 1017, 'nm': 'Tarp2', 'cat': 0, 'ini': '2020-07-05T19:23:35.000Z', 'siz': 15, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 991, 'nm': 'TarpTest', 'cat': 0, 'ini': '2020-07-04T18:40:29.000Z', 'siz': 4, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 987, 'nm': 'WindowTest2', 'cat': 0, 'ini': '2020-07-04T15:50:38.000Z', 'siz': 7, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 986, 'nm': 'WindowTransTest', 'cat': 0, 'ini': '2020-07-04T15:45:22.000Z', 'siz': 18, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 980, 'nm': 'lastugfile', 'cat': 0, 'ini': '2020-07-04T03:51:21.000Z', 'siz': 3635, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 978, 'nm': 'Ihatethissomuch', 'cat': 0, 'ini': '2020-07-04T03:27:09.000Z', 'siz': 3635, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 977, 'nm': 'UF13', 'cat': 0, 'ini': '2020-07-04T02:52:15.000Z', 'siz': 3623, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 976, 'nm': 'UF12', 'cat': 0, 'ini': '2020-07-04T02:39:37.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 975, 'nm': 'UF11', 'cat': 0, 'ini': '2020-07-04T02:37:00.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 974, 'nm': 'UF10', 'cat': 0, 'ini': '2020-07-04T02:34:01.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 973, 'nm': 'UF9', 'cat': 0, 'ini': '2020-07-04T02:32:55.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 972, 'nm': 'UF8', 'cat': 0, 'ini': '2020-07-04T02:31:17.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 971, 'nm': 'UF7', 'cat': 0, 'ini': '2020-07-04T02:01:49.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 970, 'nm': 'UF6', 'cat': 0, 'ini': '2020-07-04T01:59:08.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 959, 'nm': 'UF5', 'cat': 0, 'ini': '2020-07-03T03:09:56.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 958, 'nm': 'UF4', 'cat': 0, 'ini': '2020-07-03T01:44:38.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 957, 'nm': 'UF3', 'cat': 0, 'ini': '2020-07-03T01:39:24.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 956, 'nm': 'UnderFinal2', 'cat': 0, 'ini': '2020-07-03T01:36:31.000Z', 'siz': 3629, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 935, 'nm': 'EdgeNoiseTest2', 'cat': 0, 'ini': '2020-07-02T16:17:13.000Z', 'siz': 16, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 934, 'nm': 'EdgeNoiseTest', 'cat': 0, 'ini': '2020-07-02T16:07:52.000Z', 'siz': 16, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 925, 'nm': 'UnderFinal', 'cat': 0, 'ini': '2020-07-01T21:25:12.000Z', 'siz': 3630, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 920, 'nm': 'lol3', 'cat': 0, 'ini': '2020-07-01T16:38:49.000Z', 'siz': 902, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 913, 'nm': 'lol2', 'cat': 0, 'ini': '2020-07-01T15:09:59.000Z', 'siz': 969, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 872, 'nm': 'MapFinal3', 'cat': 0, 'ini': '2020-06-30T14:07:23.000Z', 'siz': 3578, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 871, 'nm': 'MapFinal2', 'cat': 0, 'ini': '2020-06-30T13:53:02.000Z', 'siz': 3578, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 862, 'nm': 'SandBagTest1', 'cat': 0, 'ini': '2020-06-30T02:41:37.000Z', 'siz': 8, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 858, 'nm': 'MetalSheet2', 'cat': 0, 'ini': '2020-06-30T01:53:17.000Z', 'siz': 9, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 857, 'nm': 'MetalSheet1', 'cat': 0, 'ini': '2020-06-30T01:50:46.000Z', 'siz': 9, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 855, 'nm': 'MapFinal', 'cat': 0, 'ini': '2020-06-29T23:11:44.000Z', 'siz': 3583, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 854, 'nm': 'TestSomething2', 'cat': 0, 'ini': '2020-06-29T23:05:20.000Z', 'siz': 3583, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 853, 'nm': 'TestSomething', 'cat': 0, 'ini': '2020-06-29T23:00:00.000Z', 'siz': 3583, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 852, 'nm': 'asdaffs', 'cat': 0, 'ini': '2020-06-29T22:58:26.000Z', 'siz': 3583, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 851, 'nm': 'Bruh_G', 'cat': 0, 'ini': '2020-06-29T22:57:22.000Z', 'siz': 3583, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 850, 'nm': 'Bruh_f', 'cat': 0, 'ini': '2020-06-29T22:55:49.000Z', 'siz': 3582, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 848, 'nm': 'bruh_E', 'cat': 0, 'ini': '2020-06-29T22:48:18.000Z', 'siz': 3635, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 847, 'nm': 'dW5kZXJncm93dGgK_4', 'cat': 0, 'ini': '2020-06-29T22:43:31.000Z', 'siz': 3635, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 846, 'nm': 'dW5kZXJncm93dGgK_3', 'cat': 0, 'ini': '2020-06-29T22:41:28.000Z', 'siz': 3582, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 845, 'nm': 'dW5kZXJncm93dGgK_2', 'cat': 0, 'ini': '2020-06-29T22:33:30.000Z', 'siz': 3574, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 844, 'nm': 'dW5kZXJncm93dGgK', 'cat': 0, 'ini': '2020-06-29T22:28:02.000Z', 'siz': 3575, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 822, 'nm': 'SeamTest2', 'cat': 0, 'ini': '2020-06-28T21:08:36.000Z', 'siz': 30, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 821, 'nm': 'PowerLineTest1', 'cat': 0, 'ini': '2020-06-28T18:58:25.000Z', 'siz': 26, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 820, 'nm': 'WireTest3', 'cat': 0, 'ini': '2020-06-28T17:00:16.000Z', 'siz': 13, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 819, 'nm': 'WireTest2', 'cat': 0, 'ini': '2020-06-28T16:56:59.000Z', 'siz': 13, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 816, 'nm': 'CrashTestX', 'cat': 0, 'ini': '2020-06-28T16:19:31.000Z', 'siz': 133, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 811, 'nm': 'TreeTest10', 'cat': 0, 'ini': '2020-06-28T01:50:54.000Z', 'siz': 3140, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 810, 'nm': 'TreeTest9', 'cat': 0, 'ini': '2020-06-28T01:37:23.000Z', 'siz': 3138, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 809, 'nm': 'TreeTest8', 'cat': 0, 'ini': '2020-06-28T01:35:55.000Z', 'siz': 3138, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 808, 'nm': 'TreeTest7', 'cat': 0, 'ini': '2020-06-28T01:34:25.000Z', 'siz': 3138, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 807, 'nm': 'TreeTest6', 'cat': 0, 'ini': '2020-06-28T01:32:05.000Z', 'siz': 3138, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 806, 'nm': 'TreeTest5', 'cat': 0, 'ini': '2020-06-28T01:21:08.000Z', 'siz': 3137, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 805, 'nm': 'TreeTest4', 'cat': 0, 'ini': '2020-06-28T01:19:38.000Z', 'siz': 3137, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 804, 'nm': 'TreeTest3', 'cat': 0, 'ini': '2020-06-28T01:17:56.000Z', 'siz': 3137, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 803, 'nm': 'TreeTest2', 'cat': 0, 'ini': '2020-06-28T01:15:53.000Z', 'siz': 3137, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 802, 'nm': 'TreeTest1', 'cat': 0, 'ini': '2020-06-28T00:14:55.000Z', 'siz': 3127, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 790, 'nm': 'Dump2', 'cat': 0, 'ini': '2020-06-27T01:40:12.000Z', 'siz': 25, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 789, 'nm': 'Palm5', 'cat': 0, 'ini': '2020-06-27T01:30:43.000Z', 'siz': 56, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 787, 'nm': 'Palm4', 'cat': 0, 'ini': '2020-06-27T01:25:27.000Z', 'siz': 56, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 784, 'nm': 'CrashTest5', 'cat': 0, 'ini': '2020-06-26T18:37:50.000Z', 'siz': 117, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 783, 'nm': 'CrashTest4', 'cat': 0, 'ini': '2020-06-26T18:36:22.000Z', 'siz': 116, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 782, 'nm': 'CrashTest3', 'cat': 0, 'ini': '2020-06-26T18:15:28.000Z', 'siz': 108, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 776, 'nm': 'CrashTest2', 'cat': 0, 'ini': '2020-06-26T13:34:30.000Z', 'siz': 162, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 774, 'nm': 'CrashTest1', 'cat': 0, 'ini': '2020-06-26T13:22:48.000Z', 'siz': 105, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 757, 'nm': 'Stack2', 'cat': 0, 'ini': '2020-06-25T15:11:27.000Z', 'siz': 16, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 756, 'nm': 'Stack1', 'cat': 0, 'ini': '2020-06-25T14:55:09.000Z', 'siz': 31, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 755, 'nm': 'LPG_Sphere', 'cat': 0, 'ini': '2020-06-25T14:21:44.000Z', 'siz': 40, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 740, 'nm': 'X', 'cat': 0, 'ini': '2020-06-25T02:00:27.000Z', 'siz': 16, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 724, 'nm': 'Wowzers', 'cat': 0, 'ini': '2020-06-24T16:06:15.000Z', 'siz': 8, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 720, 'nm': 'BruhMomentBruh', 'cat': 0, 'ini': '2020-06-24T15:19:56.000Z', 'siz': 31, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 717, 'nm': 'BruhTest4', 'cat': 0, 'ini': '2020-06-24T14:11:22.000Z', 'siz': 26, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 716, 'nm': 'BruhTest3', 'cat': 0, 'ini': '2020-06-24T14:08:58.000Z', 'siz': 25, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 715, 'nm': 'BruhTest2', 'cat': 0, 'ini': '2020-06-24T13:59:53.000Z', 'siz': 69, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 714, 'nm': 'BruhTest1', 'cat': 0, 'ini': '2020-06-24T13:58:08.000Z', 'siz': 69, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 701, 'nm': 'BeegSej', 'cat': 0, 'ini': '2020-06-23T17:13:17.000Z', 'siz': 15, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 699, 'nm': 'BonkBruh3', 'cat': 0, 'ini': '2020-06-23T16:46:24.000Z', 'siz': 57, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 698, 'nm': 'BonkBruh2', 'cat': 0, 'ini': '2020-06-23T16:44:49.000Z', 'siz': 57, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 697, 'nm': 'BonkBruh', 'cat': 0, 'ini': '2020-06-23T16:42:14.000Z', 'siz': 57, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 696, 'nm': 'GetFreeWifiAnywhere', 'cat': 0, 'ini': '2020-06-23T16:39:08.000Z', 'siz': 57, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 695, 'nm': 'FronkNite2', 'cat': 0, 'ini': '2020-06-23T16:28:40.000Z', 'siz': 17, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 694, 'nm': 'FronkNite', 'cat': 0, 'ini': '2020-06-23T16:23:19.000Z', 'siz': 17, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 691, 'nm': 'Temp_Palm', 'cat': 0, 'ini': '2020-06-23T15:28:06.000Z', 'siz': 56, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 664, 'nm': 'Bruhster', 'cat': 0, 'ini': '2020-06-22T16:13:05.000Z', 'siz': 9, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 662, 'nm': 'BabaBooey', 'cat': 0, 'ini': '2020-06-22T14:50:37.000Z', 'siz': 175, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 659, 'nm': 'GamerGirl2', 'cat': 0, 'ini': '2020-06-22T14:28:22.000Z', 'siz': 7, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 658, 'nm': 'GamerGirl', 'cat': 0, 'ini': '2020-06-22T14:26:07.000Z', 'siz': 7, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 657, 'nm': 'Bruhmomento', 'cat': 0, 'ini': '2020-06-22T14:06:39.000Z', 'siz': 15, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 656, 'nm': 'JoeMom', 'cat': 0, 'ini': '2020-06-22T13:07:52.000Z', 'siz': 10, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 641, 'nm': 'Furries', 'cat': 0, 'ini': '2020-06-21T20:21:51.000Z', 'siz': 21, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 638, 'nm': 'JoeMom4', 'cat': 0, 'ini': '2020-06-21T19:22:10.000Z', 'siz': 1, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 637, 'nm': 'JoeMom3', 'cat': 0, 'ini': '2020-06-21T19:21:48.000Z', 'siz': 2, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 636, 'nm': 'JoeMom2', 'cat': 0, 'ini': '2020-06-21T19:21:26.000Z', 'siz': 2, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 635, 'nm': 'JoeMom1', 'cat': 0, 'ini': '2020-06-21T19:20:53.000Z', 'siz': 3, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 630, 'nm': 'RawrXD', 'cat': 0, 'ini': '2020-06-21T17:39:56.000Z', 'siz': 11, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 547, 'nm': 'KanjiTest_6', 'cat': 0, 'ini': '2020-06-21T01:38:52.000Z', 'siz': 98, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 546, 'nm': 'KanjiTest_5', 'cat': 0, 'ini': '2020-06-21T01:35:15.000Z', 'siz': 364, 'plrn': 'GraphiteEater', 'dat': '{"e":1}'}, {'id': 545, 'nm': 'KanjiTest_4', 'cat': 0, 'ini': '2020-06-21T01:31:47.000Z', 'siz': 290, 'plrn': 'GraphiteEater', 'dat': '{}'}, {'id': 507, 'nm': 'E', 'cat': 0, 'ini': '2020-06-18T14:42:45.000Z', 'siz': 290, 'plrn': 'GraphiteEater', 'dat': '{"t":1}'}, {'id': 544, 'nm': 'EEE', 'cat': 0, 'ini': '2020-06-21T01:16:09.000Z', 'siz': 291, 'plrn': 'GraphiteEater', 'dat': '{"t":1}'}]]

            try:maps = data[7]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            #maps = [{'map_name': 'Waterfall_Inf', 'map_votes': 1412, 'map_verified': None}, {'map_name': 'Disaster', 'map_votes': 1, 'map_verified': None}]
            try:user_name = data[3]['player_name']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No account found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "No user assets found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            
            client.scache[user_name.lower()] = data
            
            await fetching.delete()
            
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

            
            pages = math.ceil(len(maps)/30)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 30
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 30
                            await ask.delete()
                            current_page -= 1
                    thing = functools.partial(get_asset_img, maps, user_name, msg, start = start, pages_ = current_page, pages_main = pages)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    ask = await msg.channel.send(file=discord.File(byte_io, "unknown.png"))
    
                    if not started:
                        started = True
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e


    elif (await gb_command_check(msg, "pf", "", dual = True)) or (await gb_command_check(msg, "profile", "", dual = True)) or (await gb_command_check(msg, "apply")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        is_applying = False
        try:  
            if msg.content.lower().startswith("g.pf"):
                if not (user_name := (await get_author_command(msg, "pf"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            elif msg.content.lower().startswith("g.profile"):
                if not (user_name := (await get_author_command(msg, "profile"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            elif msg.content.lower().startswith("g.apply"):
                is_applying = True
                user_name = gb_command_fix(msg, "apply").split("\n")[0]
                application = get_var("apl")
                try:
                    application = application[msg.guild.id]
                    if application["chl"] != 0 and application["chl"] != msg.channel.id:
                        return
                except:
                    await emb_send(chl, warning+" Please enable application system in your server using `g.applications`")
                    return
            try:
                application
            except:
                application = None
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()

            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            if user_name.lower() not in client.pre_cached:
                mdata = await get_user_data(unquote(unquote(user_name)), pf__ = 1)
                client.pre_cached.append(user_name.lower())
                client.loop.create_task(clear_smart_cache(user_name))
            else:
                try:
                    mdata = client.scache[user_name.lower()]
                    mdata = [0, 0, 0, client.scache[user_name.lower()], mdata["player_maps"], mdata["player_mods"], 0, mdata["player_assets"]]
                except:
                    mdata = [0, 0, 0, 0, 0, 0, 0, 0]
                
            #mdata = ['0', 'profile', 'zombo', {'player_name': 'zombo', 'player_id': 455498, 'player_kills': 804, 'player_wins': 46, 'player_games_played': 169, 'player_deaths': 834, 'player_timeplayed': 43868198, 'player_funds': 430, 'player_score': 79010, 'player_featured': 0, 'player_clan': '', 'player_hack': 0, 'player_following': 0, 'player_followed': 0, 'player_stats': '{"c":1,"s":440,"h":97,"r4":1,"r1":2}', 'player_datenew': '2018-09-27T23:10:47.000Z', 'player_elo': 0, 'player_region': 1, 'player_type': 0, 'player_elo2': None, 'player_elo4': None, 'player_chal': None, 'player_infected': None, 'player_eventcount': None, 'player_premium': 0, 'partner_approved': 0, 'clan_rank': 0, 'player_alias': None, 'player_twitchname': None}, [], [], None, []]
            if mdata == ['cpt']:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Websocket issue. It must be fixed within few hours or mins.", description = "If the problem persists, contact bot dev"))
                await fetching.delete()
                try:client.pre_cached.remove(user_name.lower())
                except:pass
                return
            mdata = mdata.copy()
            try:data = mdata[3]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                try:client.pre_cached.remove(user_name.lower())
                except:pass
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            try:
                data = data.copy()
            except:pass
            if data == None:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found"))
                await fetching.delete()
                return
            
            
            try:
                stats = json.loads(data['player_stats'])
            except:stats = {"c":0,"s":0,"h":0,"mk":0,"c1":0,"c0":0,"r4":0,"c5":0,"c3":0,"c4":0,"c9":0,"c11":0,"c2":0,"n":0,"hs":0,"chgP":"0:0,0,0,0","wb":0,"c6":0,"c8":0, "flg":-1, "tk":0, "fk":0}
            try:data['player_clan']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No account found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            try:
                int(data['player_chal'])
            except:data['player_chal'] = -1
            for e_elo in ["player_elo2", "player_elo4", "player_elo"]:
                try:
                    if not data[e_elo]:
                        data[e_elo] = 0
                except:data[e_elo] = 0
            if client.prank and user_name.lower() == client.pranked:
                #data["player_featured"] = 1
                data["player_hack"] = 1
                data["player_type"] = 10
            
            #img = Image.new('RGB', (450,250), (54, 57, 63))
            muser = await get_author_name(msg, user_name, True, True)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                thing = functools.partial(generate_pf, data, stats, user_name, is_applying, mdata, application, muser)
                byte_io, img_format = await client.loop.run_in_executor(executor, thing)
            
            #with ThreadPoolExecutor(max_workers = 1) as executor:
            #thing = functools.partial(message.channel.send, file=discord.File(byte_io, "gamebot_pf."+img_format))
            #await client.loop.run_in_executor(executor, message.channel.send, file=discord.File(byte_io, "gamebot_pf."+img_format))
                
            await message.channel.send(file=discord.File(byte_io, "gamebot_pf."+img_format))
            
            
            await fetching.delete()
            
            await manage_impressions( data["player_name"], msg.author.id)
            data["player_maps"] = mdata[4]
            data["player_mods"] = mdata[5]
            data["player_assets"] = mdata[7]
            client.scache[user_name.lower()] = data
            
            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "stats", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        is_applying = False
        try:  
            if msg.content.lower().startswith("g.stats"):
                if not (user_name := (await get_author_command(msg, "stats"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return

            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            if ((is_is := get_author(msg, user_name)) == 2 or not is_is) and msg.author.id not in staff:
                await emb_send(chl, warning + " You can only check your own stats using this method. Use `g.pf {}` instead".format(user_name))
                return
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            mdata = await get_user_data(unquote(unquote(user_name)), pf__ = 1)
                
            #mdata = ['0', 'profile', 'zombo', {'player_name': 'zombo', 'player_id': 455498, 'player_kills': 804, 'player_wins': 46, 'player_games_played': 169, 'player_deaths': 834, 'player_timeplayed': 43868198, 'player_funds': 430, 'player_score': 79010, 'player_featured': 0, 'player_clan': '', 'player_hack': 0, 'player_following': 0, 'player_followed': 0, 'player_stats': '{"c":1,"s":440,"h":97,"r4":1,"r1":2}', 'player_datenew': '2018-09-27T23:10:47.000Z', 'player_elo': 0, 'player_region': 1, 'player_type': 0, 'player_elo2': None, 'player_elo4': None, 'player_chal': None, 'player_infected': None, 'player_eventcount': None, 'player_premium': 0, 'partner_approved': 0, 'clan_rank': 0, 'player_alias': None, 'player_twitchname': None}, [], [], None, []]
            if mdata == ['cpt']:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Websocket issue. It must be fixed within few hours or mins.", description = "If the problem persists, contact bot dev"))
                await fetching.delete()
                try:client.pre_cached.remove(user_name.lower())
                except:pass
                return
            try:data = mdata[3]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                try:client.pre_cached.remove(user_name.lower())
                except:pass
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            try:
                data = data.copy()
            except:pass
            if data == None:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found"))
                await fetching.delete()
                return
            
            
            try:
                stats = json.loads(data['player_stats'])
            except:stats = {"c":0,"s":0,"h":0,"mk":0,"c1":0,"c0":0,"r4":0,"c5":0,"c3":0,"c4":0,"c9":0,"c11":0,"c2":0,"n":0,"hs":0,"chgP":"0:0,0,0,0","wb":0,"c6":0,"c8":0, "flg":-1, "tk":0, "fk":0, "tmk":0}
            try:data['player_clan']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No account found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            try:
                int(data['player_chal'])
            except:data['player_chal'] = 0
            for e_elo in ["player_elo2", "player_elo4", "player_elo"]:
                try:
                    if not data[e_elo]:
                        data[e_elo] = 0
                except:data[e_elo] = 0
            muser = await get_author_name(msg, user_name, True, True)
            def define_data(data, k, d2, v):
                try:data[k] = int(d2[v[0]])
                except:data[k] = 0
            data["player_level"] = max(1, math.floor(0.03 * math.sqrt(data["player_score"])))
            data["player_maps"] = len(mdata[4])
            data["player_mods"] = len(mdata[5])
            data["player_assets"] = len(mdata[7])
            define_data(data, "player_headshots", stats, ['hs'])
            define_data(data, "player_wallbangs", stats, ['wb'])
            define_data(data, "player_melees", stats, ['mk'])
            define_data(data, "player_bullseyes", stats, ['tmk'])
            define_data(data, "player_beatdowns", stats, ['fk'])
            define_data(data, "player_nukes", stats, ['n'])
            try:data["player_losses"] = data["player_games_played"] - data["player_wins"]
            except:data["player_losses"] = 0
            try:data["player_accuracy"] = float('{:.2f}'.format((stats['h'] or 0) / stats['s'] * 100 if stats['s'] else 0))
            except:data["player_accuracy"] = 0
            try:data["player_spk"] = int(data['player_score']/data['player_kills'])
            except:data["player_spk"] = 0
            try:data["player_wl"] = float("%.2f" % float(data['player_wins']/(data['player_games_played'] - data['player_wins'])))
            except:data["player_wl"] = 0
            try:data["player_kdr"] = float("%.2f" % float(data['player_kills']/data['player_deaths']))
            except:data["player_kdr"] = 0
            try:data["player_kpg"] = float("%.2f" % float(data['player_kills']/data['player_games_played']))
            except:data["player_kpg"] = 0

            
            info = {
                "Level": ["player_level", "{:,}"],
                "Score":["player_score", "{:,}"],
                "Challenge": ["player_chal", "{:,}"],
                "KR":["player_funds", "{:,}"],
                "sep1":0,

                "SPK":["player_spk", "{:.2f}"],
                "W/L":["player_wl", "{:.2f}"],
                "KDR":["player_kdr", "{:,.2f}"],
                "KPG":["player_kpg", "{:,.2f}"],
                "Accuracy":["player_accuracy", "{:,.3f}"],
                "sep2":0,

                "Kills":["player_kills", "{:,}"],
                "Deaths":["player_deaths", "{:,}"],
                "sep3":0,
                
                "Games":["player_games_played", "{:,}"],
                "Wins":["player_wins", "{:,}"],
                "Losses":["player_losses", "{:,}"],
                "sep4":0,
                
                "Time Played":["player_timeplayed", "{}"],
                "sep5":0,

                "Melees":["player_melees", "{:,}"],
                "Nukes":["player_nukes", "{:,}"],
                "Headshots":["player_headshots", "{:,}"],
                "Wallbangs":["player_wallbangs", "{:,}"],
                "Bullseyes":["player_bullseyes", "{:,}"],
                "Beatdowns":["player_beatdowns", "{:,}"],
                "sep6":0,
                
                "Maps":["player_maps", "{:,}"],
                "Mods":["player_mods", "{:,}"],
                "Assets":["player_assets", "{:,}"],
                "sep7":0,
                
                "Followers":["player_followed", "{:,}"],
                "Following":["player_following", "{:,}"],}
            

            with open("Data/tracker.bt", "rb") as file:
                old_data = pickle.load(file)
            try:old_stats = old_data[user_name.lower()].copy()
            except:old_stats = data.copy()
            old_data[user_name.lower()] = data.copy()
            if get_author(msg, user_name):
                with open("Data/tracker.bt", "wb") as file:
                    pickle.dump(old_data, file)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                thing = functools.partial(make_stats, data, info, client, data["player_name"], old_stats)
                byte_io = await client.loop.run_in_executor(executor, thing)
            if get_author(msg, user_name):
                with open("Data/timestamps.bt", "rb") as file:
                    stamp_data = pickle.load(file)
                try:
                    stamp_data["stats"][user_name.lower()] = int(time.time())
                except:
                    stamp_data["stats"] = {}
                    stamp_data["stats"][user_name.lower()] = int(time.time())
                with open("Data/timestamps.bt", "wb") as file:
                    pickle.dump(stamp_data, file)
            
            #with ThreadPoolExecutor(max_workers = 1) as executor:
            #thing = functools.partial(message.channel.send, file=discord.File(byte_io, "gamebot_pf."+img_format))
            #await client.loop.run_in_executor(executor, message.channel.send, file=discord.File(byte_io, "gamebot_pf."+img_format))
                
            await message.channel.send(file=discord.File(byte_io, "gamebot_stats.png"))
            
            await fetching.delete()
            
            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
        

    elif (await gb_command_check(msg, "map")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        user_name = gb_command_fix(msg, "map")
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Please wait..."))
        data = await get_user_data(user_name, "map")
        #data = ['0', 'map', 'Caribbean_Escape', {'map_id': 101082, 'map_name': 'Caribbean_Escape', 'map_playerid': 1487185, 'map_creator': 'Sidney', 'map_description': 'A fun escape map. Well detailed, well themed. Check it out and press the like button.', 'map_date': '2020-06-13T15:13:49.000Z', 'map_serverid': 1, 'map_initialdate': '2020-05-06T18:14:08.000Z', 'map_verified': None, 'pl': 2269, 'tm': 736842155, 'vt': 365, 'mi': '{"t":1}', 'map_updatecounter': 0}]
        try:
            data = data[3]
            if data == None:raise TypeError()
        except:
            await message.channel.send(embed=discord.Embed(title = warning + " No map found!", description = "Make sure you are using correct map name."))
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            return
        with open(featured_maps_file, "rb") as file:
            old_data = pickle.load(file)
        try:
            if data["map_name"].lower() in old_data:
                data["map_verified"] = 0
            else:data["map_verified"] = None
        except:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No map found"))
            await fetching.delete()
            return
        
        host_data = client.lobbies


        try:descip = data["map_description"]
        except:descip = ""
        descip = textwrap.wrap(descip, width=67)
        with ThreadPoolExecutor(max_workers = 1) as executor:
            thing = functools.partial(make_map_info, data, descip, client, map_thumb_url, user_name, host_data)
            byte_io = await client.loop.run_in_executor(executor, thing)
        
        await emb_send(chl, "", image_url = "attachment://image.png", file=discord.File(byte_io, "image.png"),
                       footer_t = "For more details, use 'g.e.map <map-name>'")
        await fetching.delete()
        

    elif (await gb_command_check(msg, "e.map")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        user_name = gb_command_fix(msg, "e.map")
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Please wait..."))
        data = await get_user_data(user_name, "map")

        try:
            data = data[3]
        except:
            await message.channel.send(embed=discord.Embed(title = warning + " No map found!", description = "Make sure you are using correct map name."))
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            return

        
        with open(featured_maps_file, "rb") as file:
            old_data = pickle.load(file)
        try:
            if data["map_name"].lower() in old_data:
                data["map_verified"] = 0
            else:data["map_verified"] = None
        except:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No map found"))
            await fetching.delete()
            return

        def filter_color(verification):
            if verification == 0:
                return (255, 203, 73)
            return Main_Color

        raw_game = "Game Links: [Hub](https://krunker.io/social.html?p=map&q={}) | [Play](https://krunker.io/?play={})".format(requests.compat.quote_plus(data["map_name"]), requests.compat.quote_plus(data["map_name"]))
        desc = data["map_description"]
        desc += "\n\n"
        desc += raw_game
        if data['vl']:
            desc += "\nVideo showcase: https://youtu.be/{}".format(data['vl'])

        
        
        embed = discord.Embed(colour=discord.Colour(14423783), title=data["map_name"], description=desc)
        embed.set_image(url=map_thumb_url.format(data["map_id"])+"?v="+str(random.randrange(0, 90000)))

        embed.add_field(name="Map Creator", value=data["map_creator"])
        embed.add_field(name="Likes", value = "{:,}".format(data["vt"]))
        embed.add_field(name="Version", value = "v"+str(data['map_updatecounter']/10))
        embed.add_field(name="Category", value = map_categories[data["ca"]])
        
        date = data["map_initialdate"][:10].split("-")
        embed.add_field(name="Publish Date", value="{} {} {}".format(str(date[2]), month[int(date[1])], date[0]).lower().title())
        date = data["map_date"][:10].split("-")
        embed.add_field(name="Update Date", value="{} {} {}".format(str(date[2]), month[int(date[1])], date[0]).lower().title())
        embed.add_field(name="Plays", value = "{:,}".format(data["pl"]))
        embed.add_field(name="~Revenue", value = "${:,}".format(data["pl"]/2000))
        embed.add_field(name="Funds / KR", value = "{:,}".format(data["fund"]))
        await msg.channel.send(embed = embed)
        await fetching.delete()
        
        
    elif (await gb_command_check(msg, "mod")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        map_name = gb_command_fix(msg, "mod")
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Please wait..."))
        hosts_htm = await await_get("https://api.krunker.io/search?type=mod&val=" + requests.compat.quote_plus(map_name))
        maps = json.loads(hosts_htm)['data']
        data = None
        for e_map in maps:
            if e_map["mod_name"].lower() == map_name.lower():
                data = e_map
                break
        if data == None:
            await message.channel.send(embed=discord.Embed(title = warning + " No mod found!", description = "Make sure you are using correct mod name."))
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            return
        desc = ""
        if data["mod_url"] != "ua":
            desc = "Mod Url: [Dropbox]({})".format(data["mod_url"])
        else:
            desc = "Mod Url: [Mod.zip](https://user-assets.krunker.io/md{}/mod.zip)".format(data["mod_id"])
        
        embed = discord.Embed(colour=discord.Colour(14423783), title=data["mod_name"], description=desc)
        embed.set_image(url="https://user-assets.krunker.io/md{}/thumb.png?v=0".format(data["mod_id"]))

        embed.add_field(name="Mod Name", value=data["mod_name"])
        embed.add_field(name="Mod Creator", value=data["creatorname"])
        embed.add_field(name="Likes", value=data["mod_votes"])
        date = data["mod_date"][:10].split("-")
        embed.add_field(name="Publish Date", value="{} {} {}".format(str(date[2]), month[int(date[1])], date[0]).lower().title())

        await msg.channel.send(embed = embed)
        await fetching.delete()

    elif (await gb_command_check(msg, "asset")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        map_name = gb_command_fix(msg, "asset")
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Please wait..."))
        hosts_htm = await await_get("https://api.krunker.io/assets?index=2&cat=-1&val=" + requests.compat.quote_plus(map_name))
        maps = json.loads(hosts_htm)['data']
        data = None
        for e_map in maps:
            if e_map["nm"].lower() == map_name.lower():
                data = e_map
                break
        if data == None:
            await message.channel.send(embed=discord.Embed(title = warning + " No asset found!", description = "Make sure you are using correct asset name."))
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            return
        stats = json.loads(data["dat"])
        ismodel = None
        try:
            stats["d"]
            ismodel = "Prefab"
            desc = ""
        except:
            ismodel = "Model"
            desc = """Asset Links:
[Model.obj]({})
[Texture.png]({})

*If a link is broken, it means that part doesn't exist*""".format(
        "https://user-assets.krunker.io/{}/model.obj".format(data["id"]),
        "https://user-assets.krunker.io/{}/model.png".format(data["id"]))
        embed = discord.Embed(colour=discord.Colour(14423783), title=data["nm"], description=desc)
        try:
            stats['t']
            embed.set_image(url="https://user-assets.krunker.io/{}/thumb.png".format(data["id"]))
        except:
            embed.set_image(url="https://krunker.io/img/noimg.png")

        embed.add_field(name="Asset Type", value=ismodel)
        embed.add_field(name="Asset Publisher", value=data["plrn"])
        embed.add_field(name="Size", value=str(data["siz"]) + " kb")
        embed.add_field(name="Category", value=asset_categories[data["cat"]])
        date = data["ini"][:10].split("-")
        embed.add_field(name="Publish Date", value="{} {} {}".format(str(date[2]), month[int(date[1])], date[0]).lower().title())
        embed.add_field(name="Asset Id", value=data["id"])

        await msg.channel.send(embed = embed)
        await fetching.delete()
        
    elif (await gb_command_check(msg, "popular", "", 1)) or (await gb_command_check(msg, "featured", "", 1)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return        
        try:
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            hosts_htm = await await_get("https://api.krunker.io/maps?index=" + str(int(msg.content.lower() != "g.popular")))
            maps = json.loads(hosts_htm)["data"]
            maps = maps[:30]
            with ThreadPoolExecutor(max_workers = 1) as executor:
                if msg.content.lower() == "g.popular":
                    thing = functools.partial(get_search_img, maps, "Popular maps", msg)
                    byte_io = await client.loop.run_in_executor(executor, thing)
                    await msg.channel.send(file=discord.File(byte_io, "popular.png"))
                
                else:
                    thing = functools.partial(get_search_img, maps, "Featured maps", msg, m_key = "map_featured")
                    byte_io = await client.loop.run_in_executor(executor, thing)
                    await msg.channel.send(file=discord.File(byte_io, "featured.png"))
                
            await fetching.delete()
            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e




        
    elif (await gb_command_check(msg, "favs", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not (user_name := (await get_author_command(msg, "favs"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            client.loop.create_task(start_loading(msg))
            
            data = await get_user_data(user_name)
            account_id = data[3]["player_id"]
            hosts_htm = await await_get("https://api.krunker.io/maps?index=4&pos=0&accountId="+str(account_id))
            maps = json.loads(hosts_htm)["data"]
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "No user favourites found"))
                await msg.remove_reaction(loading, client.user)
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            

            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

            
            pages = math.ceil(len(maps)/30)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            await msg.remove_reaction(loading, client.user)
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 30
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 30
                            await ask.delete()
                            current_page -= 1
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        thing = functools.partial(get_asset_img, maps, user_name, msg, start = start, pages_ = current_page, pages_main = pages, arg_ = "mna", arg_2b = False, header = "Favs")
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    ask = await msg.channel.send(file=discord.File(byte_io, "unknown.png"))
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "e.favs", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not (user_name := (await get_author_command(msg, "e.favs"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()
            client.loop.create_task(start_loading(msg))
            data = await get_user_data(user_name)
            account_id = data[3]["player_id"]
            hosts_htm = await await_get("https://api.krunker.io/maps?index=4&pos=0&accountId="+str(account_id))
            maps = json.loads(hosts_htm)["data"]
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "No user favourites found"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return

            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

            
            pages = math.ceil(len(maps)/10)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            ask = None
            await msg.remove_reaction(loading, client.user)
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 30
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 30
                            current_page -= 1
                    ask = await post_emb_page(ask, maps, user_name, msg, start = start, pages_ = current_page, pages_main = pages)
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e



    elif (await gb_command_check(msg, "owners")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            user_name = (await get_author_command(msg, "owners"))
            try:
                id_ = client.skins[user_name.lower()]["i"]
                name_ = client.skins[user_name.lower()]["name"]
            except Exception as e:
                possible_ = difflib.get_close_matches(user_name, client.skins, cutoff = 0, n = 10)
                pre_desc = "" if not possible_ else "**Possible similarities**\n\n"
                embed = discord.Embed(colour=discord.Colour(14423783), title = warning + " No item found", description = pre_desc+("\n".join([e_poss.title() for e_poss in possible_])))
                await msg.channel.send(embed = embed)
                await fetching.delete()
                return
            maps = await get_market(id_)
            maps = maps[4]
            if len(maps) > 30:
                maps = maps[:30]

            with ThreadPoolExecutor(max_workers = 1) as executor:
                thing = functools.partial(make_owners, maps, client, name_)
                byte_io = await client.loop.run_in_executor(executor, thing)
            
            await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            await fetching.delete()
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "editor help", "", 1)):
        await emb_send(msg.channel, """```diff
g.editor
-> Load your map export file
g.editor flip <axis>
->  Flip your map by an axis. Axis may be X or Y or Z
g.editor remove duplicates
->  Remove exact duplicate objects from your map
g.editor scatter <x-range> <y-range> <z-range> <count> <size>
-> Add objects in the map randomly
g.editor remove faces
->  Remove useless hidden faces
g.editor scale <val>
->  Scale the map by <val> times
g.editor scale x:<val> y:<val> z:<val>
->  Scale the map by specific value for each axis. You can select only one axis too.
g.export
->  Export your edited map file
g.clear
->  Clear your map from database
```""",
                       footer_t = "The map data is stored only in ram, temporarily.",
                       title_ = "Map Editing Features")
    elif (await gb_command_check(msg, "layout", "", 1)):
        client.loop.create_task( do_on_message(msg, -2))
        got_tk = await get_tk(msg)
        if got_tk:return
        client.is_operating[msg.author.id] = 1
        quests = {
            0: "**Middle Layer** Image",
            1: "**Bottom Layer** Image, *enter `skip` if you don't have any*",
            2: "**Top Layer** Image, *enter `skip` if you don't have any*"}
        images = {}
        walls_img = {}
        def check(m):return (m.channel == message.channel or m.guild == None) and m.author == message.author
        for x in range(3):
            await message.channel.send("""Upload {} _(You can also post the image in dms)_:""".format(quests[x]))
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling layout maker after timeout...\nPlease try again.");tk(msg);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
            try:
                if msg_.content.lower() == "skip":continue
                if not msg_.attachments[0].size > 1000000:
                    img = await msg_.attachments[0].read()
                    try:img = Image.open(BytesIO(img))
                    except:await emb_send(msg.channel, warning + " Could not decode the image", footer_t = "Make sure you uploaded the correct image.");tk(msg);return
                    images[x] = img
                else:
                    await emb_send(msg.channel, warning + " 1 Mb is the max size. Please try again from start...");tk(msg);return
            except Exception as e:
                await emb_send(msg.channel, warning + " Please attach image. Try again from start!")
                tk(msg);
                raise e
        notfied_error = False
        for img_type, img in images.items():
            noti = ""
            pixels = img.load()
            try:md = str(img.mode)
            except:md = "RGB"
            if md == "RGBA":
                for y in range(img.size[1]):
                    for x in range(img.size[0]):
                        p_c = list(pixels[x, y])
                        if not p_c[-1]:
                            pixels[x, y] = (255, 255, 255, 255)
            img = img.convert("RGB")
            if img.width > 100 or img.height > 100:
                img.thumbnail((100, 100), Image.BOX)
                main = Image.new('RGB', (104,104), (255, 255, 255))
                if not notfied_error:await emb_send(msg.channel, warning + " The image's dimensions are bigger than 100x100. It is resized. Layout may lose quality", footer_t = "Suppressing exception!");notfied_error = True
                await asyncio.sleep(1)
            else:
                main = Image.new('RGB', (img.width+4,img.height+4), (255, 255, 255))
            main.paste(img, (2, 2))
            img = main
            if (0, 0, 0) not in [v for k,v  in list(dict(img.getcolors(img.size[0]*img.size[1])).items())]:
                await emb_send(msg.channel, warning + " No black pixels found!", footer_t = "Black pixel is the color which defines the platform");tk(msg);return
            walls_img[img_type] = img.copy()
            images[img_type] = img.copy()
        await asyncio.sleep(1)
        configs = "```css\n"
        def check(m):return m.channel == message.channel and m.author == message.author and (m.content.isdigit() or m.content.lower() == "cancel")
        to_be_edited = await emb_send(msg.channel, loading + " Enter layout scale:", footer_t = "15 is recommended for 100x100")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                scale = int(msg_.content)
                await msg_.delete()
                await emb_edit(to_be_edited, content = taskdone+" Layout scale is "+ msg_.content)
                configs += "Layout Scale = " + msg_.content + "\n"
                await asyncio.sleep(1.5)
                break
        try:
            images[1]
            has_bottom = True
            def check_int(cnt):
                try:return int(cnt) < 0
                except ValueError:return False
            def check(m):return m.channel == message.channel and m.author == message.author and (check_int(m.content) or m.content.lower() == "cancel")
            await emb_edit(to_be_edited, loading + " Enter the lowest height for your bottom layer of layout:", footer_t = "Must be negative integer\n-70 is recommended")
            while True:
                try:msg_ = await client.wait_for('message', check=check, timeout=100)
                except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
                else:
                    if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                    bottom_pos = int(msg_.content)
                    await msg_.delete()
                    await emb_edit(to_be_edited, content = taskdone+" Lowest layout position is "+ msg_.content)
                    configs += "Lowest Layout Pos = " + msg_.content + "\n"
                    await asyncio.sleep(1.5)
                    break
        except:has_bottom= False

        try:
            images[2]
            has_top = True
            def check(m):return m.channel == message.channel and m.author == message.author and (m.content.isdigit() or m.content.lower() == "cancel")
            await emb_edit(to_be_edited, loading + " Enter the highest height position for your top layer of layout:", footer_t = "70 is recommended")
            while True:
                try:msg_ = await client.wait_for('message', check=check, timeout=100)
                except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
                else:
                    if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                    top_pos = int(msg_.content)
                    await msg_.delete()
                    await emb_edit(to_be_edited, content = taskdone+" Highest layout position is "+ msg_.content)
                    configs += "Highest Layout Pos = " + msg_.content + "\n"
                    await asyncio.sleep(1.5)
                    break
        except:has_top= False
        def check(m):return m.channel == message.channel and m.author == message.author and (m.content.lower() in ["cancel", "yes", "no"])
        await emb_edit(to_be_edited, loading + " Do you want to enable accuracy?\n*Enabling accuracy will keep decimals in positions and sizes.*", footer_t = "Enter 'yes' or 'no'. Enabling recommended.")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                accuracy = True if msg_.content.lower() == "yes" else False
                await msg_.delete()
                await emb_edit(to_be_edited, content = taskdone+(" Enabled Accuracy!" if accuracy else " Disabled Accuracy!"))
                configs += "Accuracy = " + ("enabled" if accuracy else "disabled") + "\n"
                await asyncio.sleep(1.5)
                break

        await emb_edit(to_be_edited, loading + " Do you want to enable walls?", footer_t = "Enter 'yes' or 'no'")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                walls = True if msg_.content.lower() == "yes" else False
                await msg_.delete()
                await emb_edit(to_be_edited, content = taskdone+(" Enabled Walls!" if walls else " Disabled Walls!"))
                configs += "Walls = " + ("enabled" if walls else "disabled") + "\n"
                await asyncio.sleep(1.5)
                if walls:
                    def check(m):return m.channel == message.channel and m.author == message.author and (m.content.isdigit() or m.content.lower() == "cancel")
                    await emb_edit(to_be_edited, loading + " Enter the height of walls: ", footer_t = "100 is recommended")
                    try:msg_ = await client.wait_for('message', check=check, timeout=100)
                    except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
                    else:
                        if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                        walls_y = int(msg_.content)
                        await msg_.delete()
                        await emb_edit(to_be_edited, content = taskdone+" Height of walls is "+ msg_.content)
                        configs += "Wall height = " + msg_.content + "\n"
                        await asyncio.sleep(1.5)
                break

        def check(m):return m.channel == message.channel and m.author == message.author and (m.content.isdigit() or m.content.lower() == "cancel")
        await emb_edit(to_be_edited, loading + " Enter height of layout platform:", footer_t = "The height is the y size of layout.\n10 is recommended")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);tk(msg);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");tk(msg);return
                platform_y = int(msg_.content)
                await msg_.delete()
                await emb_edit(to_be_edited, content = taskdone+" Height of layout platform is "+ msg_.content)
                configs += "Layout Y = " + msg_.content + "\n"
                await asyncio.sleep(1.5)
                break

        configs += "```"
        await emb_edit(to_be_edited, content = configs, title_ = "Configs")
                       
        output_objects = []
        to_be_edited = await emb_send(chl, loading + " **I am working on your map's layout.**\n*It may take 2 seconds to 1 minute, depending on your configurations*")
        #unwrap_image(img, scale, lay_y = 10, accuracy = True, y_pos_in = 0, ramp_y = 50)
        def get_nearby_p(pmap, x, y, color_):
            try:return True if pmap[x, y] == color_ else False
            except:pass
            try:return True if pmap[x-1, y] == color_ else False
            except:pass
            try:return True if pmap[x, y-1] == color_ else False
            except:pass
            try:return True if pmap[x+1, y] == color_ else False
            except:pass
            try:return True if pmap[x, y+1] == color_ else False
            except:pass
            return False
        for image_ind, img in images.items():
            if image_ind == 0:
                thing = functools.partial(unwrap_image,
                                          img, scale, platform_y,
                                          accuracy, if_ramps = False)
            if image_ind == 1:
                thing = functools.partial(unwrap_image,
                                          img, scale, platform_y,
                                          accuracy, bottom_pos)
            if image_ind == 2:
                thing = functools.partial(unwrap_image,
                                          img, scale, platform_y,
                                          accuracy, top_pos,
                                          invert = True)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                try:some_stuff = await client.loop.run_in_executor(executor, thing)
                except Exception as e:
                    await emb_edit(to_be_edited, warning + " An error occured while uploading the image.", footer_t = "Make sure you uploaded the correct image.");tk(msg);raise e
            try:
                if some_stuff > 1000:await emb_edit(to_be_edited, warning + " Image is too complex!", footer_t = "Make sure you uploaded the correct image. Try turning off walls if you have enabled them");tk(msg);return
            except:pass
            output_objects += some_stuff
            if walls:
                if image_ind == 0:
                    img = outline_image(walls_img[image_ind], (0, 255, 0))
                    pixels = img.load()
                    try:
                        fut_img = walls_img[1]
                        fut_pixels = fut_img.load()
                        for y in range(img.size[1]):
                            for x in range(img.size[0]):
                                p_c = list(pixels[x, y])
                                if p_c[:3] == [0, 0, 0]:
                                    if get_nearby_p(fut_pixels, x, y, (255, 0, 0)):pixels[x, y] = (255, 255, 255)
                                    if get_nearby_p(fut_pixels, x, y, (0, 255, 0)):pixels[x, y] = (255, 255, 255)
                    except:pass
                    try:
                        fut_img = walls_img[2]
                        fut_pixels = fut_img.load()
                        for y in range(img.size[1]):
                            for x in range(img.size[0]):
                                p_c = list(pixels[x, y])
                                if p_c[:3] == [0, 0, 0]:
                                    if get_nearby_p(fut_pixels, x, y, (255, 0, 0)):pixels[x, y] = (255, 255, 255)
                                    if get_nearby_p(fut_pixels, x, y, (0, 255, 0)):pixels[x, y] = (255, 255, 255)
                    except:pass
                    await asyncio.sleep(30)
                    thing = functools.partial(unwrap_image, img, scale, walls_y, accuracy, 0)
                if image_ind == 1:
                    img = outline_image(walls_img[image_ind], (255, 0, 0))
                    thing = functools.partial(unwrap_image, img, scale, walls_y, accuracy, bottom_pos)
                if image_ind == 2:
                    img = outline_image(walls_img[image_ind], (255, 0, 0))
                    thing = functools.partial(unwrap_image, img, scale, walls_y, accuracy, top_pos)
                with ThreadPoolExecutor(max_workers = 1) as executor:
                    try:some_stuff = await client.loop.run_in_executor(executor, thing)
                    except Exception as e:await emb_edit(to_be_edited, warning + " An error occured while uploading the image.", footer_t = "Make sure you uploaded the correct image. Try turning off walls if you have enabled them.");tk(msg);raise e
                try:
                    if some_stuff > 1000:await emb_edit(to_be_edited, warning + " Image is too complex!", footer_t = "Make sure you uploaded the correct image.");tk(msg);return
                except:pass
                output_objects += some_stuff
            
        client.map_files[msg.author.id] = {'name': 'Gamebot Layout Maker', 'ambient': '#97a0a8', 'light': '#f2f8fc', 'sky': '#dce8ed', 'fog': '#8d9aa0', 'fogD': 2000, 'objects': [], 'spawns': []}
        client.map_files[msg.author.id]["objects"] = output_objects
        await emb_edit(to_be_edited, taskdone+" Your layout is ready.", footer_t = "Export your layout using `g.export`")
        tk(msg)

    elif (await gb_command_check(msg, "editor", "", 1)):
        client.loop.create_task( do_on_message(msg))
        to_be_edited = await emb_send(chl, loading+" Initializing! Please upload your map export file in dms.")
        await msg.author.send("Upload your map export file here!")
        def check(m):
            return m.guild == None and m.author == message.author and m.attachments
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=60)
            except asyncio.TimeoutError:await message.channel.send(warning+" You haven't uploaded any file in dms...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Editing Cancelled!");return
                if not msg_.attachments[0].size > 1000000:
                    data = await msg_.attachments[0].read()
                    data= str(data)[2:-1]
                    try:data = json.loads(data)
                    except:await msg.author.send(warning + " Broken map export file. Please try again...");return
                else:await msg.author.send(warning + " 1 Mb is the max size. Please try again...");return
                break
        await msg.author.send("File received, continue using commands in the server.")
        if type(data) == list:
            client.map_files[msg.author.id] = {'name': 'New Krunker Map', 'ambient': '#97a0a8', 'light': '#f2f8fc', 'sky': '#dce8ed', 'fog': '#8d9aa0', 'fogD': 2000, 'objects': [], 'spawns': []}
            client.map_files[msg.author.id]["objects"] = data
            await emb_edit(to_be_edited, taskdone + " GG {}! File uploaded. Start using commands now.".format(msg.author.mention),
                           footer_t = "Recognized Prefab export. Adjusted your data accordingly.")
        else:
            client.map_files[msg.author.id] = data
            await emb_edit(to_be_edited, taskdone + " GG {}! File uploaded. Start using commands now.".format(msg.author.mention))
    elif (await gb_command_check(msg, "editor scale")):
        try:x = y = z = int(gb_command_fix(msg, "editor scale"))
        except:
            xyz = gb_command_fix(msg, "editor scale").split(" ")
            try:y = int(val) if (val := get_arg(xyz, "y")) != None else 0
            except:y = 0
            try:x = int(val) if (val := get_arg(xyz, "x")) != None else 0
            except:x = 0
            try:z = int(val) if (val := get_arg(xyz, "z")) != None else 0
            except:z = 0
            if not sum([x, y, z]):
                await emb_send(msg.channel, """Heres correct format:
`g.editor scale <val>`
`g.editor scale x:<val> y:<val> z:<val>`

**Examples:**
`g.editor scale 2`
`g.editor scale x:3`
`g.editor scale x:5 y:5`
""", title_ = warning +" Incorrect input");return
        if x == 0:x = 1
        if y == 0:y = 1
        if z == 0:z = 1
        try:data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        for e_obj in data["objects"]:
            if x:e_obj["p"][0] = e_obj["p"][0] * x
            if y:e_obj["p"][1] = e_obj["p"][1] * y
            if z:e_obj["p"][2] = e_obj["p"][2] * z
            if "i" not in list(e_obj.keys()) or ("i", 34) in e_obj.items():
                if x:e_obj["s"][0] = e_obj["s"][0] * x
                if y:e_obj["s"][1] = e_obj["s"][1] * y
                if z:e_obj["s"][2] = e_obj["s"][2] * z
            else:
                try:
                    if x and y and z:
                        try:e_obj["ms"] = e_obj["ms"] * x
                        except:e_obj["ms"] = scales[e_obj["i"]] * x
                except:pass
        await emb_send(msg.channel,
                        taskdone + " Scaled your map by {} x {} x {}".format(x, y, z),
                        footer_t = "Export your map using `g.export`");return
        
    elif (await gb_command_check(msg, "editor remove duplicates", "", 1)):
        try:
            data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        if not list(duplicates(data["objects"], key=dict)):
            await emb_send(msg.channel, taskdone + " No duplicate objects found!");return
        else:
            dups = list(duplicates(data["objects"], key=dict))
            for e_dup in dups:
                data["objects"].remove(e_dup)
            await emb_send(msg.channel,
                           taskdone + " Removed {} duplicate objects".format(len(dups)),
                           footer_t = "Export your map using `g.export`");return
    elif (await gb_command_check(msg, "editor flip y", "", 1)):
        try:
            data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        for e_obj in client.map_files[msg.author.id]["objects"]:
            try:
                e_obj["r"][0] =  get_axis_val(e_obj["r"][0])
                e_obj["r"][1] =  -e_obj["r"][1]
                e_obj["p"][1] =  -e_obj["p"][1]
            except:
                try:
                    e_obj["i"]
                    e_obj["p"][1] =  -e_obj["p"][1]
                    e_obj["r"] =  [math.pi, 0, 0]
                except:
                    e_obj["p"][1] =  int(0-e_obj["p"][1])-int(e_obj["s"][1])
                
        await emb_send(msg.channel, taskdone+" Flipped the map by Y axis", footer_t = "Export your map using `g.export`")
    elif (await gb_command_check(msg, "editor 90", "", 1)):
        try:
            data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        for e_obj in client.map_files[msg.author.id]["objects"]:
            try:
                try:
                    e_obj["i"] and e_obj["r"]
                    e_obj["r"][0] = math.pi + e_obj["r"][0]
                    e_obj["r"][2] = math.pi + e_obj["r"][2]
                except:
                    e_obj["r"][0], e_obj["r"][2] = e_obj["r"][2],  -e_obj["r"][0]
            except:
                try:
                    try:e_obj["r"]
                    except:
                        e_obj["i"]
                        e_obj["r"] =  [0, math.pi, 0]
                except:pass
            e_obj["s"][0], e_obj["s"][2] = e_obj["s"][2], e_obj["s"][0]
            e_obj["p"][0], e_obj["p"][2] = e_obj["p"][2], -e_obj["p"][0]
                
        await emb_send(msg.channel, taskdone+" Rotated the map by 90 degress", footer_t = "Export your map using `g.export`")

    elif (await gb_command_check(msg, "editor flip x", "", 1)):
        try:
            data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        for e_obj in client.map_files[msg.author.id]["objects"]:
            try:
                try:
                    e_obj["i"] and e_obj["r"]
                    e_obj["r"][0] = math.pi + e_obj["r"][0]
                    e_obj["r"][2] = math.pi + e_obj["r"][2]
                except:
                    e_obj["r"][1] =  -e_obj["r"][1]
                    e_obj["r"][2] =  -e_obj["r"][2]
            except:
                try:
                    try:e_obj["r"]
                    except:
                        e_obj["i"]
                        e_obj["r"] =  [0, math.pi, 0]
                except:pass
            e_obj["p"][0] =  -e_obj["p"][0]
                
        await emb_send(msg.channel, taskdone+" Flipped the map by X axis", footer_t = "Export your map using `g.export`")
    elif (await gb_command_check(msg, "editor flip z", "", 1)):
        try:
            data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        for e_obj in client.map_files[msg.author.id]["objects"]:
            try:
                try:
                    e_obj["i"] and e_obj["r"]
                    if e_obj["r"][0]:
                        e_obj["r"][0] = math.pi + e_obj["r"][0]
                    if e_obj["r"][2]:
                        e_obj["r"][2] = math.pi + e_obj["r"][2]
                except Exception as e:
                    e_obj["r"][0] = -e_obj["r"][0]
                    e_obj["r"][2] = -e_obj["r"][2]
            except:
                try:
                    try:e_obj["r"]
                    except:
                        e_obj["i"]
                        e_obj["r"] =  [0, math.pi, 0]
                except:pass
            e_obj["p"][2] =  -e_obj["p"][2]
                
        await emb_send(msg.channel, taskdone+" Flipped the map by Z axis", footer_t = "Export your map using `g.export`")

    elif (await gb_command_check(msg, "editor scatter")):
        try:data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        try:
            provided_args = gb_command_fix(msg, "editor scatter")
            provided_args = provided_args.split(" ")
            range_x =int(int(provided_args[0])/2)
            range_y =int(int(provided_args[1])/2)
            range_z =int(int(provided_args[2])/2)
            count_ = int(provided_args[3])
            size_  = int(provided_args[4])
        except:
            await emb_send(msg.channel,
                           warning + " Invalid arguments provided. Here is the correct format:\n`g.editor scatter <x-range> <y-range> <z-range> <count> <size>`",
                           footer_t = "Example:\ng.editor scatter 100 100 100 50 10");return
        to_be_added = []
        for _ in range(count_):
            r_obj = random.choice(client.map_files[msg.author.id]["objects"])["p"]
            p_sizes = [random.randint(r_obj[0]-range_x, r_obj[0]+range_x),
                       random.randint(r_obj[1]-range_y, r_obj[1]+range_y),
                       random.randint(r_obj[2]-range_z, r_obj[2]+range_z)]
            to_be_added.append({'p': p_sizes, 's': [size_]*3})
        client.map_files[msg.author.id]["objects"] += to_be_added
        await emb_send(msg.channel, taskdone+" Added scattered cubes in the map randomly.", footer_t = "Export your map using `g.export`")

    elif (await gb_command_check(msg, "editor remove faces", "", 1)) and msg.author.id == 669816890163724288:
        try:data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        fetching = await emb_send(msg.channel, loading+" Added your map in the Queue. Removing useless faces", footer_t = "That might take 15 to 40 seconds depending on your map size")
        thing = functools.partial(remove_faces, json.dumps(client.map_files[msg.author.id], separators = (",", ":")))
        with ThreadPoolExecutor(max_workers = 1) as executor:
            some_stuff = await client.loop.run_in_executor(executor, thing)
        client.map_files[msg.author.id] = json.loads(some_stuff[0])
        old_faces = some_stuff[1]
        new_faces = some_stuff[2]
        time_taken = some_stuff[3]
        footer_t = "Old Faces: {}\nNew Faces: {}\nFaces Removed: {}\nTime taken: {} seconds\n\nExport your map using `g.export`".format(
            old_faces,
            new_faces,
            old_faces-new_faces,
            "{:.1f}".format(time_taken))
            
        await emb_send(msg.channel, taskdone+" Removed useless faces", footer_t = footer_t)
        await fetching.delete()

    elif (await gb_command_check(msg, "export", "", 1)):
        try:data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return

        f = discord.File(BytesIO(bytes(json.dumps(data, separators = (",", ":")), encoding = "utf-8")), filename=data["name"]+".txt")
        try:
            await msg.author.send("Here is your edited map export:", file = f)
        except:
            await emb_send(chl, warning + " Please turn your dms on and try again");return
        await emb_send(msg.channel, taskdone+" Check your dms to view your export file.", footer_t = "Clear your map from database using `g.clear`")
    elif (await gb_command_check(msg, "clear", "", 1)):
        try:data = client.map_files[msg.author.id]
        except:await emb_send(msg.channel, warning + " You haven't loaded any map file. Start using `g.editor`");return
        del client.map_files[msg.author.id]
        await emb_send(msg.channel, taskdone+" Successfully cleared your map from database")
    elif (await gb_command_check(msg, "ping", "", 1)):
        client.loop.create_task( do_on_message(msg))
        t = time.time()
        msg_ = await message.channel.send('Pong!')
        await msg_.edit(content = 'Ping between bot and this server: `{} ms`\nPing between bot and discord: `{} ms`'.format(int((time.time()-t)*1000), int(client.latency*1000)))
    elif (await gb_command_check(msg, "botdata", "", 1)) and msg.author.id in staff:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        try:
            hitmm = read_format(len(client.get_guild(580620012168151060).members))
            hitmb = read_format(client.get_guild(580620012168151060).premium_subscription_count)
        except:
            hitmb = 0
            hitmm = 0
        await message.channel.send(embed = discord.Embed(colour=discord.Colour(14423783), description = """
Server Members: `{}`
Servers: `{}`
Linked Users: `{}`
Boosts: `{}`

hitthemoney's server members: {}
hitthemoney's server boosts: {}
""".format(
    read_format(len(client.get_guild(ghub).members)),
    read_format(len(client.guilds)),
    read_format(len(old_data)),
    read_format(client.get_guild(ghub).premium_subscription_count),
    hitmm,
    hitmb,
    )))


    elif (await gb_command_check(msg, "invite", "", 1)):
        client.loop.create_task( do_on_message(msg))
        await message.channel.send(embed = discord.Embed(colour=discord.Colour(14423783), description = """
**Invite link:** https://discord.com/api/oauth2/authorize?client_id=coming-soon&permissions=129088&scope=bot

Discord Support Server: https://discord.gg/coming-soon
Support us on Patreon: https://www.patreon.com/ComingSoonBTW

Servers: `{}`
Shards: `{}`
Users: `{}`
""".format(read_format(len(client.guilds)), read_format(len(client.shards)), read_format(len(client.users)))))

    elif (await gb_command_check(msg, "server", "", 1)):
        client.loop.create_task( do_on_message(msg))
        await emb_send(chl, """
**Discord Support Server:** https://discord.gg/coming-soon
Server Members: {}

*Support us on Patreon: https://www.patreon.com/ComingSoonBTW*
""".format(len(client.get_guild(ghub).members)))


    elif (await gb_command_check(msg, "patreon", "")):
        client.loop.create_task( do_on_message(msg))
        await message.channel.send("""
**Support us on Patreon: https://www.patreon.com/ComingSoonBTW**
Benefits:
 ● Upto 3 **Custom Personal/Clan backgrounds**
 ● **No rate limit** for commands
 ● Access to private testing channels
 ● Special Patreon Badge for Profile
 ● Special Dev commands
 ● Early access to content
 ● Commands in dms
 ● Gamebot DJ benefits *(upcoming)*
 ● Extra Customizations for Profile
""".format(len(client.guilds), len(client.users)))








    elif (await gb_command_check(msg, "reg")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if not message.guild == None: print("Command reg", message.guild.name.encode('unicode-escape').decode('utf-8'))
        try:
            user_name = gb_command_fix(msg, "reg")


            with open(graph_data_file, "rb") as file:
                old_data = pickle.load(file)
            for e_p in old_data:
                try:
                    e_p[user_name.lower()]
                    print("Yea")
                    await message.channel.send(embed=discord.Embed(title = warning+ " User already registered", colour=discord.Colour(14423783)))
                    if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                    return
                except:pass

            with open(pfp_id_file, "rb") as file:
                ppl_ids = pickle.load(file)
            #pids_ppls = [ppl.lower() for ppl in list(old_data.keys())]
            ppl_ids = {k.lower(): v for k, v in ppl_ids.items()}
            try:
                ppl_id = ppl_ids[user_name.lower()]
            except:
                data = await get_user_data(user_name)
                #maps = data[4]
                ppl_id = data[3]['player_id']

            
            hosts_htm = await await_get(api_maps_url+str(ppl_id))
            maps = json.loads(hosts_htm)['data']
            #return json.loads(hosts_htm.text.replace("false", "'false'").replace("true", "'true'"))["games"]
        
            if not len(maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user maps found"))
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                #await fetching.delete()
                return
            #{'Sidney': [{'map':{'likes':[0,0,0,0,0,0], 'plays':[]}}]}
            new_ppl_reg = {}
            map_g_data = []
            for e_map in maps:
                map_g_data_int = {}
                map_g_data_int['likes'] = [e_map['map_votes']] + list([None]*13)
                map_g_data_int['plays'] = [e_map['map_pl']] + list([None]*13)
                map_g_data_int['funds'] = [e_map['fund']] + list([None]*13)
                map_g_data.append({e_map['map_name'].lower(): map_g_data_int})
            #map_votes = [{: } for e_map in maps]

            new_ppl_reg[user_name.lower()] = map_g_data
            new_ppl_reg["player_id"] = ppl_id
            #new_ppl_reg['date'] = "today"

            old_data.append(new_ppl_reg)
            with open(graph_data_file, "wb") as file:
                pickle.dump(old_data, file)
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = recipt+" User registered", footer_t = "It will take few days to make a nice and beautiful plot."))
            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e




        

    elif (await gb_command_check(msg, "graph")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading +" Generating Graph"))
        try:
            map_name = gb_command_fix(msg, "graph")
            map_data = await get_map_g(map_name, message)
            if map_data == None:
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            try:
                funds = map_data['funds']
            except:
                funds = [None] * 14
            thing = functools.partial(graph_make, map_data['likes'], map_data['plays'], funds, Map_Name = map_name)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
            
            await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            await fetching.delete()
            
        except Exception as e:
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "lobbies")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading +" Generating Graph"))
        try:
            map_name = gb_command_fix(msg, "lobbies")
            try:
                main_data = client.hosting_cache[map_name.lower()]
                map_data = [[d[0] for d in main_data], [d[1] for d in main_data], [d[2] for d in main_data]]
            except:
                await fetching.delete();await emb_send(chl, warning + " Seems like nobody hosted your map with last hour <a:TE_Noooooo:803528735638159370>");
                return
            if map_data == None:
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            thing = functools.partial(lobbies_make, map_data[0], map_data[1], map_data[2], Map_Name = map_name)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
            
            await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            await fetching.delete()
            
        except Exception as e:
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
            


    elif (await gb_command_check(msg, "update_graph", "")) and message.author.id == 669816890163724288:
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Updating Graph Data. This may take a while"))        
        await UpdateGData()
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Graph Data Updated!"))
        await fetching.delete()

            
    elif (await gb_command_check(msg, "full_help", "")):
        
        client.loop.create_task( do_on_message(msg))
        embed = discord.Embed(colour=discord.Colour(14423783), description="""
[Support Server](https://discord.gg/coming-soon) | [Invite Url](https://discord.com/api/oauth2/authorize?client_id=coming-soon&permissions=129088&scope=bot) | [Support us on Patreon](https://www.patreon.com/ComingSoonBTW)

Prefix:  `g.`

**Commands:

Profile**
> ```css
> g.pf <kr-username>     Check krunker user profile
> g.maps <kr-username>   Check krunker user maps
> g.mods <kr-username>   Check krunker user mods
> g.assets <kr-username> Check krunker user assets
> g.cstats <kr-username> Check your stats on each class
> g.posts <kr-username>  Check the posts of a user
> g.stats                Track your profile stats```
**Account Linking**
> ```css
> g.link <kr-username>   Get the best experience by linking your kr username with discord account
> g.unlink <kr-username> Unlink your linked account
> g.incognito            If you want to go incognito after linking, use this command
> g.alts                 Get list of your linked accounts
> g.alts set             Switch between your linked accounts
> g.pbg <user-name>      Change your personal background
> g.cbg <clan-name>      Change your clan background```
**Servers**
> ```css
> g.find [map-name] [-u] [-p] ...  Find hosted server links of map, or random games. Use `g.help find`
> g.online                         Get list of most active custom maps
> g.gameinfo <game-url>            Get info about a hosted game
> g.popular                        Get all maps in popular section
> g.featured                       Get all maps in featured section```
**Maps**
> ```css
> g.map <map-name>       Check a specific map
> g.online [kr-username] Get list of online players on your maps
> g.favs <kr-username>   Check krunker user's favourite maps
> g.search <keyword>     Search for maps using keyword
> g.theme                Get 3 random themes for map making```
**Map Editing**
> ```css
> g.editor               Launch the editor
> g.layout               Image to Map Layout converter
> g.editor help          Get all map editing commands```
**Leaderboards & Skins**
""")
        embed2 = discord.Embed(colour=discord.Colour(14423783), description="""
> ```css
> g.leaders <key>         key: [level][kills][wins][time][kr][clans][1v1][2v2][4v4][challenge][egg][wars]
> ---|                    Get leaderboard of the key
> g.skin <skin-name> [-t] Check a skin, or its texture files
> g.owners <skin-name>    Find owners of a skin```
**Clans & Others**
> ```css
> g.clan <clan-name>                 Check krunker clan
> g.wars [clan-name] [region:<reg>]  Check clanwars
> g.leaders wars                     View soldier leader boards for clan
> g.applications                     Set configurations for appyling
> g.apply <kr-username>              Apply for clan, shows if you are qualified or not
> g.mod <mod-name>                   Check mod details
> g.asset <asset-name>               Check asset details
> g.hub <name>                       Get links to social hub
> g.class <class-name>               View information about a class
> g.update <version>                 View any krunker update```
**Sweeps & Graphs**
> ```css
> g.reg <kr-username>    Register krunker user to start using graphs
> g.graph <map-name>     Likes and plays of map in the form of graphs
> g.sweeper help         Get list of sweep commands```
**Fun Stuff**
> ```css
> g.reply <msg>          Replies a reply to your <message>
> g.cat                  Get a cat photo
> g.dog                  Get a dog photo
> g.bird                 Get a bird photo
> g.joke                 Get a random joke
> g.meme                 Laugh at memes
> g.tinyurl <url>        Make a url tiny```
**Server Management:**
> ```css
> g.set_chl <#channel>      Set a channel where commands can be used
> g.list_chl                See the list of channels configured as bot commands channels
> g.auto_manage help        Get the help context of server auto managing module
> g.levels                  Get level roles (20+, 30+, 40+) automatically
> g.auto_updates #<channel> Auto post krunker updates in your server```
""")
        embed3 = discord.Embed(colour=discord.Colour(14423783), description="""
**Utility**
> ```css
> g.staff                Get list of all Gamebot Staff members
> g.invite               Invite gamebot to a server
> g.patreon              Support on patreon and get ton of benefits
> g.ping                 Check Bot Latency
> g.help                 View help context
> g.help <module>        View help about a module
> g.full_help            View detailed help context```

[Support Server](https://discord.gg/coming-soon) | [Invite Url](https://discord.com/api/oauth2/authorize?client_id=coming-soon&permissions=129088&scope=bot) | [Support us on Patreon](https://www.patreon.com/ComingSoonBTW)

For more support, visit [Support Server](https://discord.gg/coming-soon) or use `g.staff`
_`<>` are not needed when using commands_
_Syntax: <> required, [] optional_
""")

        embed.set_author(name="Help", icon_url="https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
        embed3.set_footer(text="Made by 39x. Check the bot out on Github: https://github.com/39x/GameBot.")

        try:
            await message.author.send(embed = embed)
            await message.author.send(embed = embed2)
            await message.author.send(embed= embed3)
            if not message.guild == None: await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783),title = mail+ " You've received mail!"))
        except:
            await message.channel.send(embed= embed)
            await message.channel.send(embed= embed2)
            await message.channel.send(embed= embed3)

    elif (await gb_command_check(msg, "statusc")) and message.author.id in admins:
        status_ = gb_command_fix(msg, "statusc")
        watching_ = status_.replace("{servers}", str(len(client.guilds)))
        await client.change_presence(status=client.bstatus, activity=discord.Activity(type=discord.ActivityType.competing, name=watching_))
    
    elif (await gb_command_check(msg, "statusw")) and message.author.id in admins:
        status_ = gb_command_fix(msg, "statusw")
        watching_ = status_.replace("{servers}", str(len(client.guilds)))
        await client.change_presence(status=client.bstatus, activity=discord.Activity(type=discord.ActivityType.watching, name=watching_))
    elif (await gb_command_check(msg, "dm")) and message.author.id in admins:
        status_ = gb_command_fix(msg, "dm")
        id_ = status_.split(" ", 1)[0]
        msg_t = status_.split(" ", 1)[1]
        dm_ = await (await get_u_(int(id_))).send(msg_t)
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "join")) and message.author.id == dev:
        status_ = gb_command_fix(msg, "join")
        if status_.lower() in blacklisted_servers and message.author.id != 669816890163724288:
            await msg.channel.send(warning +" You don't have the perm to access this server!");return

        
        req_guild = discord.utils.get(client.guilds, name=status_)
        if req_guild == None:await msg.channel.send(warning +" No server found!");return
        try:inv = await req_guild.text_channels[0].create_invite(max_uses = 1, max_age = 120, reason = "Needed by staff for linking profiles")
        except Exception as e:print(e);await msg.channel.send(warning +" Couldn't create invite!");return
        await msg.author.send("Here is your requested invite \n"+str(inv))
        await asyncio.sleep(5)
        await msg.delete()
    elif (await gb_command_check(msg, "staff", "", 1)):
        """available = []
        offline = []
        desc = ""
        statuses= {
            "online": "<:online:787624209312514078>",
            "offline": "<:offline:787624209492606976>",
            "dnd": "<:do_not_disturb:787624209500995595>",
            "idle": "<:idle:787624209454989313>"}
        for e_st in list(staff):
            try:
                mem = client.get_guild(708067789830750449).get_member(e_st)

                if mem.raw_status != "offline":
                    his_status = "<:Using_Mobile:787628645392187393>" if (mem.is_on_mobile() and mem.raw_status == "online") else statuses[mem.raw_status]
                    available.append(his_status + " "+ mem.mention)
                else:
                    offline.append("<:offline:787624209492606976> "+ mem.mention)
            except Exception as e:print(e)
        if available:
            desc = "__**Available:**__\n"
            desc += "\n".join(available)
            desc += "\n\n"
        if offline:
            desc += "__Offline__:\n"
            desc += "\n".join(offline)
            desc += "\n\n"
        """
        desc = "\n".join([await get_um(e_st) for e_st in list(staff)])
        await emb_send(msg.channel, desc, title_ = "Gamebot Staff", footer_t = "Developer: 39x. Check the bot out on Github: https://github.com/39x/GameBot")
    elif (await gb_command_check(msg, "uptime", "", 1)):
        
        delta_uptime = datetime.datetime.utcnow() - client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await emb_send(msg.channel, f"{days}d, {hours}h, {minutes}m, {seconds}s")

    elif (await gb_command_check(msg, "update", "", dual = True)):
        get_first = False
        if msg.content.lower() != "g.update":
            status_ = gb_command_fix(msg, "update") + " "
        else:
            status_ = None
            get_first = True
        updates = await get_update_data()
        updates = updates.split("""
 == """)
        if not get_first:
            found_update = ""
            for update in updates:
                if str(status_.lower()).strip() == str(update.replace("UPDATE ", "").split("\n", 1)[0].split(" ", 1)[0].lower()).strip():
                    found_update = update.split("\n", 1)[-1]
                    break
        else:
            found_update = updates[5].split("\n", 1)[-1]
            status_ = str(updates[5].replace("UPDATE ", "").split("\n", 1)[0].split(" ", 1)[0].lower()).strip()
        if not found_update:
            await msg.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ "No Update found"))
            return
        embed=discord.Embed(colour=discord.Colour(14423783), title = "== UPDATE {} ==".format(status_))
        found_update = found_update.split("\n")
        while "" in found_update:
            found_update.remove("")
        main_updates = []
        if len(found_update) > 25:
            main_updates.append(found_update[:26])
            main_updates.append(found_update[26:])
        else:
            main_updates = [found_update]
        for main_update in main_updates:
            total_lines = 0 
            for i, k in zip(main_update[0::2], main_update[1::2]):
                embed.add_field(name = i.strip().replace("<br/>", "\u200b"), value = k.strip().replace("<br/>", "\u200b"), inline  = False)
                total_lines += 2
            if total_lines != len(main_update):
                embed.add_field(name = main_update[-1].strip().replace("<br/>", "\u200b"), value = "\u200b", inline  = False)
            await message.channel.send(embed = embed)
            embed=discord.Embed(colour=discord.Colour(14423783))



    elif (await gb_command_check(msg, "post_update", "", 1)) and msg.author.id == dev:
        def check(m):return m.channel == message.channel and m.author == message.author
        found_update = []
        await emb_send(chl, "**Enter Update Version:**")
        for x in range(40):
            if x == 1:
                await emb_send(chl, "**Enter the fields:**", footer_t = "One message = One field\n'done' to stop\n'cancel' to cancel")
            try:msg_ = await client.wait_for('message', check=check, timeout=345)
            except asyncio.TimeoutError:
                await msg.add_reactin(warning);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Update Cancelled!");return
                if msg_.content.lower() == "done":break
                if msg_.content == "n":
                    found_update.append("\u200b")
                else:
                    from_ = 3 if msg_.content.startswith("...") else 0
                    found_update.append(("" if not x else " - ")[from_:] + str(msg_.content)[from_:])
        await emb_send(chl, "**Enter the channel where you want to post it:**")
        try:msg_ = await client.wait_for('message', check=check, timeout=345)
        except asyncio.TimeoutError:
            await msg.add_reactin(warning);return
        else:
            chl_ = msg_.channel_mentions[0]
        embed=discord.Embed(colour=discord.Colour(14423783), title = "Gamebot got an update! v{}".format(found_update[0]))        
        del found_update[0]
        while "" in found_update:
            found_update.remove("")
        main_updates = []
        if len(found_update) > 25:
            main_updates.append(found_update[:26])
            main_updates.append(found_update[26:])
        else:
            main_updates = [found_update]
        pinged_everyone = "@everyone"
        for main_update in main_updates:
            total_lines = 0 
            for i, k in zip(main_update[0::2], main_update[1::2]):
                embed.add_field(name = i.strip(), value = k.strip(), inline  = False)
                total_lines += 2
            if total_lines != len(main_update):
                embed.add_field(name = main_update[-1].strip(), value = "\u200b", inline  = False)
            if not pinged_everyone:
                embed.set_footer(text="Keep using gamebot", icon_url = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
            await chl_.send(pinged_everyone, embed = embed)
            pinged_everyone = ""
    
            embed=discord.Embed(colour=discord.Colour(14423783))


    elif (await gb_command_check(msg, "profit")):
        status_ = gb_command_fix(msg, "profit")
        data = status_.split(" ")
        buy_price = int(data[0])
        sell_price = int(data[1])
        fee = math.floor(sell_price * 0.05)
        profit = sell_price - fee - buy_price
        raw_desc = """
Buy Price: {}
Sell Price: {}
Market Fee: {}

Profit: {}
"""
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783),
                                                       title = "Profit Calculator",
                                                       description = raw_desc.format(
                                                           "{:,}".format(buy_price),
                                                           "{:,}".format(sell_price),
                                                           "{:,}".format(fee),
                                                           "{:,}".format(profit)
                                                           )))
        
    elif (await gb_command_check(msg, "suggest")):
        client.loop.create_task( do_on_message(msg))
        if msg.author.id in suggestors:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783),title = "ERROR!", description = "You can only post one suggestion per 10 mins"))
            return
        sample_raw = """```
{}

By - {}
```"""
        status_ = gb_command_fix(msg, "suggest")
        ats = []
        if msg.attachments:
            for e_a in msg.attachments:
                at = await e_a.to_file()
                ats.append(at)
        sugg_poll = await client.get_guild(708067789830750449).get_channel(737670502872645634).send(sample_raw.format(status_, str(msg.author)), files = ats)
        
        suggestors.append(msg.author.id)
        await msg.add_reaction(check_mark)
        await sugg_poll.add_reaction(check_mark)
        await sugg_poll.add_reaction(error)
        await remove_id_from_2(msg)
        

        
    elif (await gb_command_check(msg, "get_token", '')) and message.author.id == dev:
        token = await get_cpt_tokenprev()
        await message.channel.send(token)
    elif (await gb_command_check(msg, "stuck")) and message.author.id in staff:
        status_ = gb_command_fix(msg, "stuck")
        client.is_operating[int(status_)] = 0
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "user_search")):
        status_ = gb_command_fix(msg, "user_search").lower()
        old_data = client.scache
        total_maps = []
        for e_acc, acc_d in old_data.items():
            try:
                if status_ in acc_d["player_name"].lower():
                    total_maps.append(acc_d["player_name"])
            except:pass
        def check(reaction, user_, msg, ask):
            return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
        entries_count = 15
        if len(total_maps) > 15:
            maps = total_maps[:entries_count];has_pages = True; overall_viewed = entries_count
        else:maps = total_maps;has_pages = False; overall_viewed = len(total_maps)
        main_pages = math.ceil(len(total_maps)/entries_count)
        current_page = 1
        start = 0
        started = False
        def get_spaces(text, max_l = 30):
            return text + str(" " * (max_l - len(text)))
        while True:
            try:
                if started:reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
            except asyncio.TimeoutError:await ask.clear_reactions();return
            else:
                if started:
                    if str(reaction.emoji) == stop:
                        await ask.clear_reactions();break
                    elif str(reaction.emoji) == next_page:
                        await ask.remove_reaction(next_page, msg.author)
                        if current_page == main_pages:
                            continue;
                        start += entries_count
                        maps = total_maps[start:start+entries_count]
                        overall_viewed = start+entries_count if start+entries_count <= len(total_maps) else len(total_maps)

                        current_page += 1
                    elif str(reaction.emoji) == prev_page:
                        await ask.remove_reaction(prev_page, msg.author)
                        if current_page == 1:
                            continue;
                        start -= entries_count
                        maps = total_maps[start:start+entries_count]; overall_viewed = start+entries_count
                        current_page -= 1
                footer_t = "Page # {} of {}\nShowing entries {} - {} of {}".format(
                    current_page, main_pages, start+1, overall_viewed, len(total_maps)

                )
                if not started:
                    ask = await emb_send(chl, taskdone + " **Found {} results through cache**\n\n```\n".format(len(total_maps))+"\n".join(maps) + "```", footer_t = footer_t)
                else:
                    await emb_edit(ask, taskdone + " **Found {} results through cache**\n\n```\n".format(len(total_maps))+"\n".join(maps) + "```", footer_t = footer_t)
                if not has_pages or main_pages == 1:break
                started = True
                await ask.add_reaction(prev_page)
                await ask.add_reaction(stop)
                await ask.add_reaction(next_page)
    elif (await gb_command_check(msg, "exec")) and message.author.id in devs:
        status_ = gb_command_fix(msg, "exec")
        try:
            token = exec(status_)
        except Exception as e:
            await message.channel.send(str(e))
            raise e
        try:await message.channel.send(token)
        except:pass
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "eval")) and message.author.id in devs:
        status_ = gb_command_fix(msg, "eval")
        try:
            token = eval(status_)
        except Exception as e:
            await message.channel.send(e)
        await message.channel.send(token)
    elif (await gb_command_check(msg, "server mute", "", 1)) and message.author.id in staff:
        muted_servers.append(msg.guild.id)
        await msg.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " WARNING!!", description = "This server has been muted for 5 mins."))
        await auto_unmute_serv(uid = msg.guild.id)
        
    elif (await gb_command_check(msg, "mute")) and message.author.id in staff:
        if len(msg.mentions) == 0:
            uid = gb_command_fix(msg, "mute")
            if uid.isdigit() and len(uid) == 18:
                uid = int(uid)
            else:return
        else:
            uid = msg.mentions[0].id
            
        if uid in [dev]:return
        
        muted_users.append(uid)
        await msg.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " WARNING!!", description = "{} has been disregarded for 5 mins".format(await get_um(uid))))
        await auto_unmute(uid = uid)

    elif (await gb_command_check(msg, "pin")) and message.author.id == 669816890163724288:
        status_ = gb_command_fix(msg, "pin")
        msgs = status_.split("|")
        
        msg1 = int(msgs[0].strip())
        msg2 = int(msgs[1].strip())

        if msg1 != 0:
            msg1 = await message.channel.fetch_message(msg1)
            await msg1.unpin()
        
        msg2 = await message.channel.fetch_message(msg2)
        await msg2.pin()
        
    elif (await gb_command_check(msg, "exit", "", 1)) and message.author.id == dev:
        await client.logout()
    elif (await gb_command_check(msg, "ss", "")) and message.author.id in admins:
        client.disable_status = 1 if not client.disable_status else 0
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "statusp")) and message.author.id in admins:
        status_ = gb_command_fix(msg, "statusp")
        watching_ = status_.replace("{servers}", str(len(client.guilds)))
        await client.change_presence(status=client.bstatus, activity=discord.Game(name=watching_))
    elif (await gb_command_check(msg, "vote", "", 1)):
        await emb_send(chl, """
**Voting Pages**
Gamebot | *top.gg*: coming soon
Krunker Logo Maker | top.gg: https://top.gg/bot/748085376484376586/vote

**Review Pages**
Gamebot | *top.gg*: coming soon
Krunker Logo Maker | *top.gg*: https://top.gg/bot/748085376484376586
""")
    elif (await gb_command_check(msg, "website", "", 1)):
        await emb_send(chl, """
Visit our official gamebot website here: http://gamebot-site.github.io/
""")
    elif (await gb_command_check(msg, "sample")) and message.author.id == 669816890163724288:
        data = gb_command_fix(msg, "sample")
        data = data.split(" ")
        user_name, type__ = data[0], data[1]
        data = await get_user_data(user_name, type_= type__)
        print(data)
    elif (await gb_command_check(msg, "badges", "")):
        await emb_send(chl, """
<:Verification:807118977548681286> Verified User
<:Premium:807118974293901324> Premium Profile
<:Krunkitis:807118973924540427> Krunkitis Virus
<:PartnerLevel1:807119766782738452> Level 1 Partner
<:PartnerLevel2:807118973895442434> Level 2 Partner
<:KrunkerDeveloper:807118974142644254> Krunker Developer
<:SingleBooster:807118974994087946> Gamebot Server Booster - Single boost
<:DoubleBooster:807118973820207125> Gamebot Server Booster - Double boosts
<:Patreon:807118974701666344> Patreon Supporter
<:StaffMember:807118983642742794> Gamebot Staff Member""", title_ ="Profile Badges")
    elif (await gb_command_check(msg, "dvm", "")) and message.author.id in devs:
        client.dev_mode = 0 if client.dev_mode else 1
        if client.dev_mode:
            await msg.reply("Turned **on** Dev mode")
        else:
            await msg.reply("Turned **off** Dev mode")
    elif (await gb_command_check(msg, "impressions", "", dual = 1)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        try:
            if not (user_name := (await get_author_command(msg, "impressions"))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            if len(user_name) > 22:
                await emb_send(chl, warning+ " No impressions found!");return
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()

            alts = get_author_list(msg)
            if user_name.lower() not in alts and msg.author.id not in staff+patreons:
                await emb_send(chl, warning + " You can only check your own impressions. Please become a supporter on patreon to view the impressions of others.");return
            
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Reading database..."))
            
            data = client.simpressions
            data = {k.lower():v for k, v in data.items()}
            try:
                number_of_imp = len(data[user_name.lower()])
                real_names = {k.lower():k for k, v in data.items()}
                real_name = real_names[user_name.lower()]
                
            except:
                await emb_send(chl, warning + " No information found in database");
                await fetching.delete();return
        
            template = """
Overall views: {}
Views today: {}
Views this week: {}
Views this month: {}
"""
            thing = functools.partial(impression_make, data[user_name.lower()], user_name)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io, today_views, week_views, month_views = await client.loop.run_in_executor(executor, thing)
            await emb_send(chl, template.format(number_of_imp, today_views, week_views, month_views), title_ = "Views for the profile", file = discord.File(byte_io, "profile_views.png"), image_url = "attachment://profile_views.png")
            await fetching.delete();

            
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "kd")):
        try:
            goal, username = gb_command_fix(msg, "kd").split(" ", 1)
            try:
                goal = float(goal.replace(",",""))
            except:
                goal2 = goal
                goal = float(username.replace(",",""))
                username = goal2
        except:
            await message.channel.send("You need to enter values. Example: g.kd 3.25 sheriffcarry")
            pass
        try:data = client.scache[username.lower()]
        except:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Couldn't locate cache for that account.", description = "Try checking your profile first using `g.pf`"))
            try:client.pre_cached.remove(username.lower())
            except:pass
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            return
        if data == None:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found"))
            return
        currenkdr = round(data["player_kills"] / data["player_deaths"], 2)
        currentkills = data["player_kills"]
        totalkills = int(data["player_deaths"]) * float(goal) +1
        missingkills = int(totalkills) - int(currentkills)
        totalkillsformatted = round(totalkills, 2)
        totalkillsformatted2 = "{:,}".format(totalkillsformatted)
        currentkillsformatted = "{:,}".format(currentkills)
        missingkillsformatted = "{:,}".format(missingkills)
        if str(currenkdr*100) >= str(goal*100):
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ "The KDR Goal is smaller then the current kdr"))
        else:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "KDR Calculator", description = """**Profile: """ + str(data["player_name"]) + """**
    Current KDR: `{}`
    Current Kills: `{}`

    KDR Goal: `{}`
    Lowest possible Kill count for that KDR: `{}`

    **Kills required without any deaths for that KDR: `{}`**""".format(currenkdr, currentkillsformatted,
                                                                   goal, totalkillsformatted2, missingkillsformatted)))
    elif (await gb_command_check(msg, "posts", "", dual = 1)) or (await gb_command_check(msg, "giveaways", "")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        try:
            client.loop.create_task(start_loading(msg))
            if msg.content.lower().startswith("g.posts"):
                if not (user_name := (await get_author_command(msg, "posts"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
                if len(user_name) > 22:
                    await emb_send(chl, warning+ " Account not found!");return
                if user_name == "%":
                    try:user_name = client.cached_cmds[msg.author.id]
                    except Exception as e:print(e);user_name = "%"
                elif user_name == "\%":
                    user_name = "%"
                else:
                    client.cached_cmds[msg.author.id] = user_name.lower()
                with open(pfp_id_file, "rb") as file:
                    ppl_ids = pickle.load(file)
                ppl_ids = {k.lower(): v for k, v in ppl_ids.items()}
                try:ppl_id = ppl_ids[user_name.lower()]
                except:
                    data = await get_user_data(user_name)
                    try:ppl_id = data[3]['player_id']
                    except:
                        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found!", description = "Make sure you are using the correct user name."));return
                data = await get_user_posts(int(ppl_id))
                data = data[1]
                is_giveaway = False
            if msg.content.lower().startswith("g.giveaways"):
                is_giveaway = True
                data = await get_user_posts(0, ["r", "feed", None, None, None, 5, 0, None])
                data = data[3]
            total_maps = data
            try:
                maps = total_maps[0]
            except:
                await emb_send(chl, warning+ " You haven't posted anything yet. Post now at [Social Hub](https://krunker.io/social.html)");return
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

            if len(total_maps) > 1:
                has_pages = True
            else:has_pages = False
            start = 0
            started = False
            #await fetching.delete()
            await msg.remove_reaction(loading, client.user)
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if start == len(total_maps) - 1:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 1
                            maps = total_maps[start]
                            await ask.delete()
                        elif str(reaction.emoji) == prev_page:
                            if not start:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 1
                            maps = total_maps[start]
                            await ask.delete()
                    else:
                        started = True
                        
                    thing = functools.partial(make_posts, maps, client.skins, PyJsHoisted_getPreview_, client, is_giveaway)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    
                    ask = await emb_send(chl, "Post Link: [Click here](https://krunker.io/social.html?p=post&q={})".format(maps["pid"]),
                                   file = discord.File(byte_io, "gamebot_posts.png"),
                                    image_url = "attachment://gamebot_posts.png")
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "statusl")) and message.author.id in admins:
        status_ = gb_command_fix(msg, "statusl")
        watching_ = status_.replace("{servers}", str(len(client.guilds)))
        await client.change_presence(status=client.bstatus, activity=discord.Activity(type=discord.ActivityType.listening, name=watching_))
    elif (await gb_command_check(msg, "sdnd", "", 1)) and message.author.id in admins:
        client.bstatus = discord.Status.dnd
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "sidle", "", 1)) and message.author.id in admins:
        client.bstatus = discord.Status.idle
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "sonline", "", 1)) and message.author.id in admins:
        client.bstatus = discord.Status.online
        await msg.add_reaction(taskdone)
    elif (await gb_command_check(msg, "soffline", "", 1)) and message.author.id in admins:
        client.bstatus = discord.Status.offline
        await msg.add_reaction(taskdone)


    elif (await gb_command_check(msg, "update_featured", '', 1)) and message.author.id == 669816890163724288:
        hosts_htm = await await_get("https://api.krunker.io/maps?index=1")
        maps = json.loads(hosts_htm)['data']
        old_data = []
        for e_map in maps:
            old_data.append(e_map['map_name'].lower())
        with open(featured_maps_file, "wb") as file:
            pickle.dump(old_data, file)

    elif (await gb_command_check(msg, "update_sweeps", '', 1)) and message.author.id == dev:
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+" Resetting sweeps"))
        await UpdateSweeps()
        await fetching.delete()
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = taskdone+" Task done!"))
        
            
    elif (await gb_command_check(msg, "dismiss", '', 1)) and message.author.id == 669816890163724288:
        client.dismiss_ = True
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "Graph Update Dismissed"))
    elif (await gb_command_check(msg, "no_dismiss", '', 1)) and message.author.id == 669816890163724288:
        client.dismiss_ = False
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "Graph Update Engaged"))

    elif (await gb_command_check(msg, "reg_count", '', 1)) and message.author.id == 669816890163724288:
        with open(graph_data_file, "rb") as file:
            old_data = pickle.load(file)
        
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = "More than {} users have been registered".format(len(old_data))))

    elif (await gb_command_check(msg, "warn")) and message.author.id in patreons:
        status_ = msg.clean_content[len("g.warn"):]
        for e_w in client.banned_words:
            if e_w in status_.lower():
                return
            if e_w.lower() in status_.lower().replace("1", "i").replace("3", "e").replace("4", "a").replace("5", "s").replace("0", "o").replace("8", "b"):
                return
        await message.channel.send(status_)
    elif (await gb_command_check(msg, "tc", "")):
        client.loop.create_task( do_on_message(msg))
        embed = discord.Embed(colour=discord.Colour(14423783), description="""

Krunker.io is owned and licensed by Yendis AG Switzerland (copyright)
and operated by Yendis Entertainment Pty Ltd. Australia (copyright)

Bot developed by 39x
This bot is open source and is under the [MIT](https://opensource.org/licenses/MIT) license on GitHub: https://github.com/39x/GameBot.

**== TERMS AND CONDITIONS ==**
If you continue to use this bot, you are agreeing to comply with and be bound by the following terms and conditions of use.
 - If you disagree with any part of these terms and conditions, do not continue the use of this bot.

_The use of this bot is subject to the following terms of use:_


 - The content displayed by the bot is for your general information and use only. It is subject to change without notice.
 - This bot displays material which is owned by or licensed to Yendis Entertainment Pty Ltd. a corporation registered in Australia and Yendis AG a corporation registered in Switzerland. I do not own anything
""")

        embed.set_author(name="Terms And Conditions", icon_url="https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
        embed.set_footer(text="Bot developed by 39x.")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "say")) and message.author.id in patreons:
        status_ = msg.clean_content[len("g.say"):]
        for e_w in client.banned_words:
            if e_w in status_.lower():
                return
            if e_w.lower() in status_.lower().replace("1", "i").replace("3", "e").replace("4", "a").replace("5", "s").replace("0", "o").replace("8", "b"):
                return
        await message.channel.send(status_)
    elif (await gb_command_check(msg, "theme", '', 1)):
        with open("Data/themes.bt", "r") as file:
            data_ = file.read().splitlines()
            themes_ = []
            for _ in range(3):
                theme_ = random.choice(data_)
                if theme_.lower()[0] in ['a', 'e', 'i', 'o', 'u']:
                    theme_ = "an " + theme_
                else:
                    theme_ = "a " + theme_
                themes_.append("Make {} map!".format(theme_).title())
            await emb_send(chl, "\n".join(themes_))
    elif (await gb_command_check(msg, "wars", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast. Please try later", ))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        try:
            user_name = gb_command_fix(msg, "wars")
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            spec_reg = user_name.lower().split("region:")
            cu_region_ = None
            if len(spec_reg) == 2:
                spec_reg = spec_reg[-1].strip()[:2]
                try:cu_region_ = region_abbr[spec_reg]
                except Exception as e:
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No region found!", description = """Try:
**gb ● Global**
na ● North America
sa ● South America
we ● Western Europe
af ● Africa
me ● Middle East
as ● Asia
oc ● Oceania
eu ● Eastern Europe
"""))
                    await fetching.delete()
                    return
            
                
            data = await get_user_data("Q", type_= "clanwars")
            try:
                data = data[3]["l"]
            except:
                await emb_send(chl, warning + "Received incorrect data. Just try again.");return
            

            ri_1, ri_2, ri_3, ri_4, ri_5, ri_6, ri_7, ri_8 = [], [], [], [], [], [], [], []
            def sort_reg(e_ri):
                return sorted(e_ri, key = lambda x: x['kl'], reverse = True)
            for e_clan in data:
                eval("ri_"+str(e_clan['ri'])).append(e_clan)
            ri_1 = sort_reg(ri_1)
            ri_2 = sort_reg(ri_2)
            ri_3 = sort_reg(ri_3)
            ri_4 = sort_reg(ri_4)
            ri_5 = sort_reg(ri_5)
            ri_6 = sort_reg(ri_6)
            ri_7 = sort_reg(ri_7)
            ri_8 = sort_reg(ri_8)

            r9_gb = sort_reg(data)

            all_regions = [ri_1, ri_2, ri_3, ri_4, ri_5, ri_6, ri_7, ri_8]

            thing = functools.partial(make_wars, client, all_regions, write_clan_name, regions_x)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)

            world_map = discord.File(byte_io, "image.png")
            
            if msg.content.lower() != "g.wars" and cu_region_ == None:
                possible_regions = []
                for e_clan in data:
                    if e_clan['cn'].lower() == user_name.lower():
                        possible_regions.append(e_clan)
                
                if not possible_regions:
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Clan has not participated in Clan Wars", ))
                    await fetching.delete()
                    return
                possible_regions = sort_reg(possible_regions)
                mdata = possible_regions[0]
                e_ri = eval("ri_"+str(mdata['ri']))

                for x, e_clan in enumerate(e_ri):
                    if e_clan["cn"].lower() == mdata["cn"].lower():
                        break
                
                
                embed = discord.Embed(colour=discord.Colour(14423783),
                                      title = mdata["cn"],
                                      url="https://krunker.io/social.html?p=clan&q="+mdata["cn"])
        
                #embed.set_image(url=prev_url)
                #embed.set_author(name=game_info[-1]['i'], url=user_name, icon_url="https://media.discordapp.net/attachments/575245793313816587/731888937643147312/Krunker-lg.png")
                embed.add_field(name="Kills", value = "{:,}".format(mdata['kl']))
                embed.add_field(name="Deaths", value = "{:,}".format(mdata['dt']))
                embed.add_field(name="Score", value = "{:,}".format(mdata['sc']))
                embed.add_field(name="Players", value = "{:,}".format(mdata['pl']))
                embed.add_field(name="Players Alive", value = "{:,}".format(mdata['c1']))
                embed.add_field(name="Players Dead", value = "{:,}".format(mdata['c3']))
                embed.add_field(name="Region", value = regions_[mdata['ri']-1])
                embed.add_field(name="Region Rank", value = str(x+1))
                try:
                    kdr = "{:.2f}".format(mdata['kl']/mdata['dt'])
                except:
                    kdr = "{:,}".format(mdata['kl'])
                new_gb = {}
                for x, e_clan in enumerate(r9_gb):
                    try:
                        new_gb[e_clan["cn"].lower()]
                        new_gb[e_clan["cn"].lower()]["kl"] += e_clan["kl"]
                        new_gb[e_clan["cn"].lower()]["pl"] += e_clan["pl"]
                    except:
                        new_gb[e_clan["cn"].lower()] = {"kl":e_clan["kl"], "pl":e_clan["pl"], "cn":e_clan["cn"]}
                new_gb = dict(sorted(new_gb.items(), key=lambda x:x[1]["kl"], reverse = True)[:30])
                e_ri = list(new_gb.keys())
                
                try:
                    global_rank = e_ri.index(mdata["cn"].lower()) + 1
                    mkills = list(new_gb.values())[global_rank-1]["kl"]
                    if global_rank-1 == 0:
                        Next_Target = "None"
                    else:
                        Next_Target = list(new_gb.values())[global_rank-2]
                        Next_Target = "{} / +{:,} kills".format(Next_Target["cn"], Next_Target["kl"]-mkills)
                except:
                    global_rank = "Unknown"
                    Next_Target = "Unknown"
                embed.add_field(name="Global Rank", value = global_rank)
                embed.add_field(name="KDR", value = kdr)
                try:
                    if global_rank != 1:excepted_color = color_name_by_code[clan_colors[global_rank]]
                    else:excepted_color = "Rainbow"
                except:excepted_color = "Gray"
                
                embed.add_field(name="Expected Color", value = excepted_color)
                
                embed.add_field(name="Next Global Target", value = Next_Target)

            
                embed.set_image(url="attachment://image.png")   
            
            
                await message.channel.send(embed = embed, file = world_map)
            elif cu_region_ != None:
                try:
                    if cu_region_.lower() != "global":
                        e_ri = all_regions[regions_.index(cu_region_)]
                        new_gb = {}
                        for x, e_clan in enumerate(e_ri):
                            if x == 30:break
                            new_gb[e_clan["cn"]] = {"kl":e_clan["kl"], "pl":e_clan["pl"]}
                    else:
                        #new_gb = {"clan":{"kl":}}
                        new_gb = {}
                        for x, e_clan in enumerate(r9_gb):
                            try:
                                new_gb[e_clan["cn"]]
                                new_gb[e_clan["cn"]]["kl"] += e_clan["kl"]
                                new_gb[e_clan["cn"]]["pl"] += e_clan["pl"]
                            except:
                                new_gb[e_clan["cn"]] = {"kl":e_clan["kl"], "pl":e_clan["pl"]}
                        new_gb = dict(sorted(new_gb.items(), key=lambda x:x[1]["kl"], reverse = True)[:30])
                    e_ri = new_gb
                except Exception as e:
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No region found!", description = """Try:
**gb ● Global**
na ● North America
sa ● South America
we ● Western Europe
af ● Africa
me ● Middle East
as ● Asia
oc ● Oceania
eu ● Eastern Europe
gb ● Global
"""))
                    await fetching.delete()
                    return
                thing = functools.partial(make_lwars, e_ri, client)
                with ThreadPoolExecutor(max_workers = 1) as executor:
                    byte_io = await client.loop.run_in_executor(executor, thing)
                await message.channel.send(file=discord.File(byte_io, "unknown.png"))
            else:
                await message.channel.send(file = world_map)
                
            await fetching.delete()
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "leaders wars", "", 0)) or (await gb_command_check(msg, "leaders war", "", 0) or (await gb_command_check(msg, "leaders clanwars", "", 0)) or (await gb_command_check(msg, "leaders clanwar", "", 0))):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast. Please try later", ))
            return
        try:
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))

                
            data = await get_user_data("Q", type_= "clanwars")
            maps = data[3]["p"]
            def filter_votes(votes):
                if not votes:return [13, (100, 100, 100), '', '', votes]
                elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
                elif votes < 0: return [6, (235, 10, 10), '', '', votes]
                elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
            def filter_color(verification):
                if verification:
                    return (64, 196, 255)
                return Main_Color
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
            total_maps = maps
            try:maps = total_maps[:20];has_pages = True
            except:has_pages = False
            main_pages = math.ceil(len(total_maps)/20)
            current_page = 1
            start = 0
            started = False
            await fetching.delete()
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == main_pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page -= 1
                    else:
                        started = True
                    thing = functools.partial(make_leadersw, maps, client, main_pages, current_page)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    ask = await message.channel.send(file=discord.File(byte_io, "unknown.png"))
                    if not has_pages or main_pages == 1:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                    
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
        
    elif (await gb_command_check(msg, "leaders")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast. Please try later", ))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        try:
            user_name = gb_command_fix(msg, "leaders")
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))

            cmd_l = {'level' : 'player_score',  'lvl' : 'player_score',
                     'kills' : 'player_kills',  'kill': 'player_kills',
                     'wins'  : 'player_wins',
                     'time'  : 'player_timeplayed',
                     'funds' : 'player_funds',  'kr' : 'player_funds',
                     'clans' : 'player_clan',   'clan' : 'player_clan',
                     '1v1'   : 'player_elo',
                     '2v2'   : 'player_elo2',
                     '4v4'   : 'player_elo4',
                     'challenge':'player_chal', 'chal':'player_chal',
                     'egghunt':'player_eventcount', 'eggs':'player_eventcount', 'egg':'player_eventcount',
                     'flw'   : 'player_followed','follower': 'player_followed',
                     'followers': 'player_followed', 'following': 'player_followed', 'flw': 'player_followed',
                     'raid': 'player_eventtime', 'raids': 'player_eventtime'}

            try:
                type_ = cmd_l[user_name.lower()]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Incorrect key"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
                
            data = await get_user_data_led(type_)
            
            try:maps = data[3]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
        
            def filter_votes(votes):
                if not votes:return [13, (100, 100, 100), '', '', votes]
                elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
                elif votes < 0: return [6, (235, 10, 10), '', '', votes]
                elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
            def filter_color(verification):
                if verification:
                    return (64, 196, 255)
                return Main_Color
            def filter_color2(clan_):
                return (130, 130, 130)
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
            total_maps = maps
            try:maps = total_maps[:20];has_pages = True
            except:has_pages = False
            main_pages = math.ceil(len(total_maps)/20)
            current_page = 1
            start = 0
            started = False
            await fetching.delete()
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == main_pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 20
                            try:maps = total_maps[start:start+20]
                            except:maps = total_maps[start:]
                            await ask.delete()
                            current_page -= 1
                    else:
                        started = True
                    thing = functools.partial(make_leaders, maps, type_, filter_color, client, user_name, write_clan_name)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    ask = await message.channel.send(file=discord.File(byte_io, "unknown.png"))
                    if not has_pages or main_pages == 1:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e



    

    elif (await gb_command_check(msg, "search")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        input_ = gb_command_fix(msg, "search").split("|")
        map_name = input_[0].strip()
        filters = {}
        if len(input_) > 1:
            for e_map in input_:
                e_map = e_map.strip()
                split_data = e_map.split(":")
                if split_data[0].startswith("like"):
                    filters['likes'] = range(int(split_data[1].split("-")[0]), int(split_data[1].split("-")[1]) + 1)
                elif split_data[0].startswith("by"):
                    filters['by'] = split_data[1]
        try:
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+" Searching..."))
            hosts_htm = await await_get("https://api.krunker.io/search?type=map&val=" + requests.compat.quote_plus(map_name))
            try:
                maps = json.loads(hosts_htm)['data']
            except:maps = []
            
            o_maps = []
            for e_map in maps:
                try:
                    if not e_map['map_votes'] in filters['likes']:continue
                except:pass
                try:
                    if not e_map['creatorname'].lower() ==  filters['by'].lower():continue
                except:pass
                o_maps.append(e_map)
            if not len(o_maps):
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No Maps found..."))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return

            try:
                maps = o_maps[:35]
            except:
                maps = o_maps
            with open(featured_maps_file, "rb") as file:
                old_data = pickle.load(file)
            for e_map in maps:
                if e_map['map_name'].lower() in old_data:
                    e_map['map_verified'] = 0
                else:e_map['map_verified'] = None
                
            thing = functools.partial(get_search_img, maps, "Keyword: "+map_name, msg)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
            await msg.channel.send(file=discord.File(byte_io, "unknown.png"))
                
            
            await fetching.delete()
            
        except Exception as e:
            #await message.channel.send(embed=discord.Embed(title = str(e)))
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.channel.send("Missing embed permissions")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e

    elif (await gb_command_check(msg, "auto_manage link", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]+devs:return
        clan_name = data["cn"]
        data = await get_user_data(clan_name, "clan")
        clan_members = [e_map["p"].lower() for e_map in data[3]["members"]]
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("Enter the in-game name of member you want to link.\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling linking after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Linking Cancelled!");return
                if msg_.content.lower() not in clan_members:
                    await message.channel.send(warning+" You can only link `"+clan_name+"` clan members!");return
                ign = msg_.content.lower()
                break
        while True:
            await message.channel.send("Mention the member you wan't to link *(You can also paste id)*.\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling linking after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Linking Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        try:
                            mentioned_one = await get_um(user_)
                        except:await message.channel.send(warning+" Incorrect Id!");await asyncio.sleep(2);continue
                            
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        old_data[ign.lower()] = user_
        with open("Data/linked.bt", "wb") as file:
            pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + "User linked sucessfully")
        await msg.channel.send(embed = embed)
        embed=discord.Embed(colour=discord.Colour(16711689),
                            description = msg.author.mention + " linked "+ mentioned_one + " with `" + ign + "`")
        await client.get_guild(708067789830750449).get_channel(745692242584535090).send(embed = embed)
    elif (await gb_command_check(msg, "auto_manage add", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]+devs:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("Mention the member you wan't to add as manager *(You can also paste id)* . *You must trust the member you are adding*\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling manager add setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        try:
                            mentioned_one = await get_um(user_)
                        except:await message.channel.send(warning+" Incorrect Id!");await asyncio.sleep(2);continue
                            
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        old_data[msg.guild.id]["mng"] = list(data["mng"] + [user_])
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + mentioned_one + " has been added as manager")
        await msg.channel.send(embed = embed)
    
    elif (await gb_command_check(msg, "auto_manage remove", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]+devs:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("Mention the member you wan't to remove as manager *(You can also paste id)*.\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling manager add setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        mentioned_one = await get_um(user_)
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        try:
            if user_ == 669816890163724288:
                await message.channel.send(warning+" This user can't be removed!");return
            old_data[msg.guild.id]["mng"].remove(user_)
        except:
            await message.channel.send(warning+" User is not a manager");return
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + mentioned_one + " has been removed from managers")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "auto_manage logs", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]+devs:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            desc = ""
            try:
                desc = msg.guild.get_channel(old_data[msg.guild.id]["logs"]).mention + " *is the current configured channel.*\n"
            except:pass
            await message.channel.send(desc+"Mention the channel you wan't to select as log channel. *Type `0` to remove current channel as logs channel*\n\nYou can cancel by typing `cancel`")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling manager add setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.channel_mentions[0].id
                except:
                    if msg_.content != "0":
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                    else:user_ = 0
                break
        old_data[msg.guild.id]["logs"] = user_
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + msg_.channel_mentions[0].mention +" has been selected as log channel")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "auto_manage roles", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]+devs:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("\n\n`Enter the Clan-Member Role Name, Don't Ping!`\n*- Its CaSe SeNsItIvE*\n\n*Type `skip` to skip this step*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                if msg_.content.lower() == "skip":role = "skip";break
                role = discord.utils.get(msg.guild.roles, name= msg_.content)
                if role == None:await message.channel.send(warning + " No role found\n");await asyncio.sleep(2)
                else:break
        while True:
            await message.channel.send("`Do you have` *`Recruit, Soldier, Captain`* `roles as well?`")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                elif msg_.content.lower() == "no":roles_list = [];break
                elif msg_.content.lower() == "yes":
                    while True:
                        await message.channel.send("Enter your roles in the following **exact** format:\n\n`recruit|soldier|captain`")
                        try:msg_ = await client.wait_for('message', check=check, timeout=100)
                        except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
                        else:
                            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                            roles = msg_.content.split("|")
                            roles_list = []
                            try:
                                for role_ in roles:roles_list.append(discord.utils.get(msg.guild.roles, name= role_).id)
                            except:
                                await message.channel.send(warning + " One or more roles not found!\n*Its CaSe SeNsItIvE*")
                                await asyncio.sleep(2)
                            else:break
                    break
        if role != "skip":old_data[msg.guild.id]["rl"] = role.id
        old_data[msg.guild.id]["rank"] = roles_list
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + " Roles have been updated!")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "auto_manage managers", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        desc = ""
        for e_mem in data["mng"]:
            desc += await get_um(e_mem)
            desc += "\n"
            
        embed=discord.Embed(colour=discord.Colour(14423783),
                            title = "Managers List",
                            description = desc)
        embed.set_footer(text = "Add a manager using 'g.auto_manage add'")

        await msg.channel.send(embed = embed)
        

    elif (await gb_command_check(msg, "auto_manage help", "", 1)):
        
        embed=discord.Embed(colour=discord.Colour(14423783),
                            title = "Auto Managing Module Help",
                            description = """
> **`g.auto_manage link`**
__*Link new clan members*__

> **`g.auto_manage roles`**
*Update roles*

> **`g.auto_manage nick`**
*Change nickname template*

> **`g.auto_manage disable`**
*Disable auto managing module*

> **`g.auto_manage enable`**
*Enable auto managing module*

> **`g.auto_manage add`**
*Add a member as manager*

> **`g.auto_manage remove`**
*Remove a member from managers*

> **`g.auto_manage logs`**
*View or Set logs channel*

> **`g.auto_manage managers`**
*Get list of current managers*

*These commands are only accessibly by managers*
""")
        embed.set_footer(text="Auto Managing tracks all clan members, assigns them clan member roles, removes the roles if somebody leaves the clan, changes nickname of all clan members as desired. In short, making server managing easy for you.")
        await msg.channel.send(embed = embed)
        
    elif (await gb_command_check(msg, "auto_manage nick", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:
            return
        def check(m):
            return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("""\n\nEnter the nickname you want clan members to be replaced with (Examples below):\n\n```
[{clan}] {ign}
[{clan}] {ign} {nm}
{nm}```

Note that:
```
{clan} = Clan Name
{ign} = In-Game Name
{nm} = Username On Discord
{nick} = Current User Nick *(selecting only this won't edit nicks)*
```""")
            
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");break
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                name_template = msg_.content
                break
        old_data[msg.guild.id]["msg"] = name_template
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        await msg.channel.send("Nickname template has been saved in database")

    elif (await gb_command_check(msg, "clan", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        try:
            client.loop.create_task(start_loading(msg))
            if (user_name:= gb_command_fix(msg, "clan")) == "%":
                try:user_name = {"cn": client.cached_cmds[msg.author.id], "is_clan": False}
                except Exception as e:print(e);user_name = {"cn":"%", "is_clan":1}
            elif user_name == "\%":
                user_name = {"cn":"%", "is_clan":1}
            elif not (user_name := (await get_author_command(msg, "clan", True))):
                await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");
                await msg.remove_reaction(loading, client.user);return
                    
            if not user_name["is_clan"]:
                try:
                    user_name = client.scache[user_name["cn"].lower()]["player_clan"]
                except:
                    data = await get_user_data(user_name["cn"], "profile")
                    user_name = data[3]["player_clan"]
            else:
                user_name = user_name["cn"]
            if len(user_name) > 5:
                await msg.remove_reaction(loading, client.user);
                await emb_send(chl, warning+ " Clan not found!");return
            data = await get_user_data(user_name, "clan")
            try:
                user_name = data[3]['clan_name']
                creator = data[3]['creatorname']
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No clan found"))
                await msg.remove_reaction(loading, client.user);return
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

            pages = math.ceil(len(data[3]["members"])/20)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 20
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 20
                            await ask.delete()
                            current_page -= 1

                    thing = functools.partial(make_clan_out, data, user_name, creator, chl, start, pages_ = current_page, pages_main = pages)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        tracked_post = await client.loop.run_in_executor(executor, thing)
                    ask = await msg.channel.send(file=discord.File(tracked_post, "unknown.png"))
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                    
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await message.add_reaction(warning);await msg.remove_reaction(loading, client.user)
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "reply")):
        client.loop.create_task( do_on_message(msg))
        await message.channel.trigger_typing()
        input_ = gb_command_fix(msg, "reply")
        data = await await_get("https://cb.totallyusefulapi.ml/" + urllib.parse.quote_plus(input_))
        response = json.loads(data)['reply']
        await msg.channel.send(response)
    elif (await gb_command_check(msg, "joke", "", 1)):
        client.loop.create_task( do_on_message(msg, 2))
        await message.channel.trigger_typing()
        data = await await_get("https://some-random-api.ml/joke")
        response = json.loads(data)['joke']
        await msg.channel.send(response)
    elif (await gb_command_check(msg, "meme", "", 1)):
        client.loop.create_task( do_on_message(msg, 2))
        await message.channel.trigger_typing()
        data = await await_get("https://meme-api.herokuapp.com/gimme")
        data = json.loads(data)
        embed=discord.Embed(colour=discord.Colour(14423783),
                                title = data["title"])
        if data["nsfw"] or data["spoiler"]:
            return
        embed.set_image(url = data["url"])
        await msg.channel.send(embed = embed)
    elif msg.content.lower() == "g.cat" or msg.content.lower() == "g.cats"or msg.content.lower() == "g.dog"or msg.content.lower() == "g.dogs" or msg.content.lower() == "g.bird" or msg.content.lower() == "g.birds":
        client.loop.create_task( do_on_message(msg, 2))
        if "cat" in msg.content.lower():
            tsource = await await_get("https://api.thecatapi.com/v1/images/search")
            hosts_htm = json.loads(tsource)[0]["url"]
            
        elif "dog" in msg.content.lower():
            tsource = await await_get("https://api.thedogapi.com/v1/images/search")
            hosts_htm = json.loads(tsource)[0]["url"]
            
        elif "bird" in msg.content.lower():
            tsource = await await_get("https://some-random-api.ml/img/birb")
            hosts_htm = json.loads(tsource)["link"]
            
        await msg.channel.send(hosts_htm)
    elif (await gb_command_check(msg, "tinyurl")):
        client.loop.create_task( do_on_message(msg, 1))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        to_be_tiny = await emb_send(chl, loading + " Making your url tiny!")
        tu = await tiny_url(gb_command_fix(msg, "tinyurl"))
        await emb_edit(to_be_tiny, taskdone + " Here is your tinyurl: " + tu)
    
        
    elif (await gb_command_check(msg, "find", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+" Searching..."))
            host_data = client.lobbies
            thing = functools.partial(get_lobbies_stuff, msg, client, host_data)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                embed, prom_desc = await client.loop.run_in_executor(executor, thing)
            if embed == None:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No online game found..."))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            await message.channel.send(embed=embed)
            if prom_desc:
                await emb_send(chl, prom_desc, emb_color = 14423783)
            await fetching.delete()
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title = str(e)))
            await fetching.delete()
            raise e
    elif (await gb_command_check(msg, "promote")) and msg.author.id == dev:
        user_name = gb_command_fix(msg, "promote")
        client.promoted.append(user_name)
        await emb_send(chl, taskdone+" Your game has been sponsored")
    elif (await gb_command_check(msg, "gameinfo")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            if not client.lobbies:
                await emb_send(chl, warning + " Bot is currently caching krunker lobbies. You should try again in few seconds.")
                return
            user_name = gb_command_fix(msg, "gameinfo")
            try:
                if client.gamelinks[msg.author.id] >= 2:
                    await msg.reply(content = "You can only have 2 max links. Please try again later when the old ones expire.")
                    return
            except:pass
            #https://krunker.io/?game=NY:eskrh
            try:
                await msg.edit(suppress = True)
            except:pass
            game_info = await async_get_lobby(user_name.split("=")[-1])
            try:
                game_info['error']
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" Game not found..."))
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            except:pass
            map_name = game_info[-1]['i']
            data = await get_user_data(map_name, "map")
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
            if data[3] == None:
                desc = "-"
                likes= "-"
                plays = "-"
                creator = "-"
                prev_url = "https://media.discordapp.net/attachments/708700075517280336/708701477585158256/no_thumb_zoomed_v2.png"
            else:
                desc = data[3]['map_description']
                likes = data[3]['vt']
                plays = data[3]['pl']
                creator = data[3]['map_creator']
                prev_url = map_thumb_url.format(data[3]['map_id'])
            footer_t = ""
            started = False
            ended = False
            posted = False
            old_plays_str = ""
            try:
                game_info[-1]['kr']
                footer_t += "Includes KR rewards"
            except:pass
            try:
                client.gamelinks[msg.author.id] += 1
            except:
                client.gamelinks[msg.author.id] = 1
            for _ in range(2000):
                if started:
                    game_info = await async_get_lobby(user_name.split("=")[-1])
                try:
                    game_info['error']
                    embed = discord.Embed(colour=discord.Colour(14423783), title = warning+" Game Ended")
                    ended = True
                except:
                    
                    embed = discord.Embed(colour=discord.Colour(14423783), title=user_name,
                                          url=user_name, description=desc, timestamp=datetime.datetime.utcnow())
    
                    embed.set_image(url=prev_url)
                    embed.set_author(name=game_info[-1]['i'], url=user_name, icon_url="https://media.discordapp.net/attachments/575245793313816587/731888937643147312/Krunker-lg.png")
                    try:
                        old_plays_str = plays_str
                    except:
                        old_plays_str = ""
                    plays_str = "{} / {}".format(game_info[2], game_info[3])
                    if plays_str == old_plays_str:
                        await asyncio.sleep(5)
                        continue
                    embed.add_field(name="Likes", value=likes)
                    embed.add_field(name="Plays", value=plays)
                    embed.add_field(name="Map Creator", value=creator)
                    embed.add_field(name="Players", value=plays_str)
                    embed.add_field(name="Region", value=regions[game_info[0].split(":")[0]])
                    embed.add_field(name="Game Mode", value=gamemodes[game_info[-1]['g']])
                    embed.set_footer(text = footer_t)
    
                if not posted:
                    posted = await message.channel.send(embed=embed)
                else:
                    await posted.edit(embed = embed)
                started = True
                if ended:
                    print("Ree3")
                    break
                await asyncio.sleep(3)
            print("Ended")
            client.gamelinks[msg.author.id] -= 1

        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e
    elif (await gb_command_check(msg, "lgameinfo")):
        all_links = get_var("links_chl")
        try:
            for e_info in all_links[msg.guild.id]:
                if e_info[0] == msg.channel.id:
                    msg_content = e_info[1]
                    delete_omsg = e_info[2]
                    delete_msg = e_info[3]
                    break
            try:msg_content
            except:return
        except:return
        client.loop.create_task(do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            try:
                if delete_omsg:
                    await msg.delete()
            except:pass
                
            wait_chl = await message.channel.send(embed=discord.Embed(title = warning+ " "+ msg.author.mention+" You are posting links too fast.", description = "Please try again in a few seconds"))
            await asyncio.sleep(7)
            await wait_chl.delete()
            return
        try:
            user_name = gb_command_fix(msg, "lgameinfo")
            try:
                if client.gamelinks[msg.author.id] >= 2:
                    max_link_warning = await msg.reply(content = "You can only have 2 max links. Please try again later when the old ones expire.")
                    if delete_msg:
                        await asyncio.sleep(6)
                        await max_link_warning.delete()
                    if delete_omsg:
                        await msg.delete()
                    return
            except:pass
            #https://krunker.io/?game=NY:eskrh
            if delete_omsg:
                await msg.delete()
            else:
                try:
                    await msg.edit(suppress = True)
                except:pass
            lobby_code = user_name.split("=", 1)[1].split(" ", 1)[0]
            try:
                msg_content += " "+ msg.clean_content.split("=", 1)[1].split(" ", 1)[1]
            except:pass
            game_info = await async_get_lobby(lobby_code)
            try:
                game_info['error']
                not_found = await message.reply(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" Game not found..."))
                if delete_msg:
                    await asyncio.sleep(3)
                    await not_found.delete()
                if delete_omsg:
                    await msg.delete()
                return
            except:pass
            game_url = "https://krunker.io/?game="+lobby_code
            map_name = game_info[-1]['i']
            data = await get_user_data(map_name, "map")
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
            if data[3] == None:
                desc = "-"
                likes= "-"
                plays = "-"
                creator = "-"
                prev_url = "https://media.discordapp.net/attachments/708700075517280336/708701477585158256/no_thumb_zoomed_v2.png"
            else:
                desc = data[3]['map_description']
                likes = data[3]['vt']
                plays = data[3]['pl']
                creator = data[3]['map_creator']
                prev_url = map_thumb_url.format(data[3]['map_id'])
            footer_t = ""
            started = False
            ended = False
            posted = False
            old_plays_str = ""
            deleted = 0
            try:
                game_info[-1]['kr']
                footer_t += "Includes KR rewards\n"
            except:pass
            try:
                client.gamelinks[msg.author.id] += 1
            except:
                client.gamelinks[msg.author.id] = 1
            for _ in range(2000):
                if started:
                    game_info = await async_get_lobby(lobby_code)
                try:
                    game_info['error']
                    embed = discord.Embed(colour=discord.Colour(14423783), title = warning+" Game Ended")
                    ended = True
                    if delete_msg:
                        deleted = True
                        try:
                            await posted.delete()
                        except:pass
                    else:
                        try:
                            await posted.add_reaction(warning)
                        except:pass
                except:
                    
                    embed = discord.Embed(colour=discord.Colour(14423783), title=game_url,
                                          url=game_url, description=desc, timestamp=datetime.datetime.utcnow())
    
                    embed.set_image(url=prev_url)
                    embed.set_author(name=game_info[-1]['i'], url=game_url, icon_url="https://media.discordapp.net/attachments/575245793313816587/731888937643147312/Krunker-lg.png")
                    try:
                        old_plays_str = plays_str
                    except:
                        old_plays_str = ""
                    plays_str = "{} / {}".format(game_info[2], game_info[3])
                    if plays_str == old_plays_str:
                        await asyncio.sleep(5)
                        continue
                    embed.add_field(name="Likes", value=likes)
                    embed.add_field(name="Plays", value=plays)
                    embed.add_field(name="Map Creator", value=creator)
                    embed.add_field(name="Players", value=plays_str)
                    embed.add_field(name="Region", value=regions[game_info[0].split(":")[0]])
                    embed.add_field(name="Game Mode", value=gamemodes[game_info[-1]['g']])
                    embed.set_footer(text = footer_t+str(msg.author), icon_url = msg.author.avatar_url)
                if not deleted:
                    if not posted:
                        posted = await message.channel.send(msg_content, embed=embed)
                    else:
                        await posted.edit(content=msg_content, embed = embed)
                    started = True
                if ended:
                    print("Ree3")
                    break
                await asyncio.sleep(3)
            print("Ended")
            client.gamelinks[msg.author.id] -= 1

        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e
    elif (await gb_command_check(msg, "class")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            user_name = gb_command_fix(msg, "class")
            for x, e_class in enumerate(classes):
                if e_class["name"].lower() == user_name.lower():
                    #img = Image.new('RGB', (250,500), (54, 57, 63))
                    
                    thing = functools.partial(make_class, x, e_class, client)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    
                    await message.channel.send(file=discord.File(byte_io, "unknown.png"))
                    return

            possible_ = difflib.get_close_matches(user_name, [e_class["name"] for e_class in classes], cutoff = 0, n = 5)
            await emb_send(chl, warning+" **No class found**\n\nSimilarities:\n\n"+"● " + ("\n● ".join(possible_)), )
            

                    
                    
                
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e


    elif (await gb_command_check(msg, "cstats", "", dual = True)) or (await gb_command_check(msg, "xp", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        try:
            
            if msg.content.lower().startswith("g.cstats"):
                if not (user_name := (await get_author_command(msg, "cstats"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            elif msg.content.lower().startswith("g.xp"):
                if not (user_name := (await get_author_command(msg, "xp"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
                    
            if user_name == "%":
                try:user_name = client.cached_cmds[msg.author.id]
                except Exception as e:print(e);user_name = "%"
            elif user_name == "\%":
                user_name = "%"
            else:
                client.cached_cmds[msg.author.id] = user_name.lower()

            fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), description  = loading+ " Please wait"))
            mdata = await get_user_data(unquote(unquote(user_name)), pf__ = 1)
            if mdata == ['cpt']:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Websocket issue. It must be fixed within few hours or mins.", description = "If the problem persists, contact bot dev"))
                await fetching.delete()
                return
                
            try:data = mdata[3]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            if data == None:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found"))
                await fetching.delete()
                return
            try:stats = json.loads(data['player_stats'])
            except:stats = {}
            for ind in range(13):
                if ind >= 10:ind += 1
                try:
                    stats["c"+str(ind)]
                except:
                    stats["c"+str(ind)] = 0
            output_stats = []
            total_maps = []
            def get_corr_ind(ind):
                return ind+1 if ind >= 10 else ind
            sub_list = []
            for ind in range(13):
                if ind >= 10:
                    tind = 1 + ind
                else:tind = ind
                score = stats["c"+str(tind)]
                tmpRank = 0.03 * math.sqrt(score)
                level = math.floor(tmpRank)
                offset = pow(level / 0.03, 2) if 1 < level else 0
                levelProg = str(math.floor(score - offset)) + ' / ' + str(math.floor(pow((level + 1) / 0.03, 2) - offset))
                levelProgstr = human_format(math.floor(score - offset)) + ' / ' + human_format(math.floor(pow((level + 1) / 0.03, 2) - offset))
                #levelProgstr = "{:,}".format(math.floor(score - offset)) + ' / ' + "{:,}".format(math.floor(pow((level + 1) / 0.03, 2) - offset))
                level += 1
                sub_list.append([sclasses[ind]["name"], sclasses[ind]["wp"], level, levelProg, levelProgstr])
                total_maps += [sub_list[-1]]
            
            total_maps = sorted(total_maps, key = lambda x:x[2], reverse = True)
            sub_list = []
            for ind, e_ind in enumerate(total_maps):
                sub_list.append(e_ind)
                if len(sub_list) == 4 or ind == 12 or ind == 0:
                    output_stats.append(sub_list)
                    sub_list = []
            maps = output_stats
            await fetching.delete()
                    
            thing = functools.partial(make_cstats, maps, total_maps, get_corr_ind, client, data, stats, get_level_int_c,sclasses_names)
            with ThreadPoolExecutor(max_workers = 1) as executor:
                byte_io = await client.loop.run_in_executor(executor, thing)
            
            ask = await message.channel.send(file=discord.File(byte_io, "unknown.png")) 
                
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e

    elif (await gb_command_check(msg, "skin")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            
            user_name = gb_command_fix(msg, "skin")
            is_text = False
            if user_name.lower().endswith(" -t"):
                user_name = user_name[:-3]
                is_text = True
            elif user_name.lower().endswith("-t"):
                user_name = user_name[:-2]
                is_text = True
            if not is_text:
                try:
                    try:
                        if client.skins[user_name.lower()]["keyW"].lower().startswith("spray"):
                            desc_raw = " • [Price]({}) • [Listing]({})".format(str(PyJsHoisted_getPrice_(client.skins[user_name.lower()]))[1:-1],
                                                                        str(PyJsHoisted_getListings_(client.skins[user_name.lower()]))[1:-1]
                                                                        )
                        else:raise TimeoutError()
                    except:desc_raw = " • [Price]({}) • [Listing]({}) • [Model]({})".format(str(PyJsHoisted_getPrice_(client.skins[user_name.lower()]))[1:-1],
                                                                        str(PyJsHoisted_getListings_(client.skins[user_name.lower()]))[1:-1],
                                                                        str(PyJsHoisted_getViewer_(client.skins[user_name.lower()]))[1:-1]
                                                                    )
                    try:
                        color = __rarities[str(client.skins[user_name.lower()]["rarity"])]
                    except:
                        color = 1
                    embed = discord.Embed(title=client.skins[user_name.lower()]["name"],
                                          description = desc_raw,
                                          color = discord.Colour(color)
                                          
                                          )
                except Exception as e:
                    possible_ = difflib.get_close_matches(user_name, client.skins, cutoff = 0, n = 10)
                    pre_desc = "" if not possible_ else "**Possible similarities**\n\n"
                    embed = discord.Embed(colour=discord.Colour(14423783), title = warning + " No skin found", description = pre_desc+("\n".join([e_poss.title() for e_poss in possible_])))
                    await msg.channel.send(embed = embed)
                    return
                thing = functools.partial(make_skin, str(PyJsHoisted_getPreview_(client.skins[user_name.lower()]))[1:-1], client, client.skins[user_name.lower()], discord.Colour(color).to_rgb())
                with ThreadPoolExecutor(max_workers = 1) as executor:
                    byte_io = await client.loop.run_in_executor(executor, thing)
                
                #ask = await message.channel.send()
                
                embed.set_image(url= "attachment://skin.png")
                
                skin__ = await message.channel.send(embed=embed, file=discord.File(byte_io, "skin.png"))
            else:
                try:
                    try:
                        client.skins[user_name.lower()]
                    except:
                        raise TimeoutError()
                    
                    embed = discord.Embed(title=client.skins[user_name.lower()]["name"],
                                          color = discord.Colour(__rarities[str(client.skins[user_name.lower()]["rarity"])])
                                          )
                    try:
                        embed.set_image(url="https://assets.krunker.io/textures/"+getTexture(client.skins[user_name.lower()])+".png")
                    except:
                        await emb_send(chl, warning + " Couldn't get texture url");return
                    desc = "**Texture Url:** {}\n".format("https://assets.krunker.io/textures/"+getTexture(client.skins[user_name.lower()])+".png")
                    try:
                        if client.skins[user_name.lower()]["glow"]:
                            desc += "\n**Emmisive Texture Url:** "+"https://assets.krunker.io/textures/"+getTexture(client.skins[user_name.lower()])+"_e.png\n"
                    except:pass
                    desc += "\n**Model Url:** {}\n".format("https://assets.krunker.io/textures/"+getTexture(client.skins[user_name.lower()])+".obj")
                    desc += "\n • Average Price: `{:,} KR`".format(client.skins[user_name.lower()]["avgPrice"])
                    embed.description  = desc
                    footer_text = ""
                    try:footer_text = "• By " +client.skins[user_name.lower()]["creator"] + "\n"
                    except:footer_text = "• By Krunker.io\n"
                    
                    try:footer_text += "• From season " + str(client.skins[user_name.lower()]["seas"]) + "\n"
                    except:pass
                    try:footer_text += "• Limited Skin\n" if client.skins[user_name.lower()]["limited"] else ""
                    except:pass
                    try:footer_text += "• Animated Skin\n" if client.skins[user_name.lower()]["frames"] else ""
                    except:pass
                
                    embed.set_footer(text = footer_text)
                    skin__ = await message.channel.send(embed=embed)
                except Exception as e:
                    print(e)
                    possible_ = difflib.get_close_matches(user_name, client.skins, cutoff = 0, n = 10)
                    pre_desc = "" if not possible_ else "**Possible similarities**\n\n"
                    embed = discord.Embed(colour=discord.Colour(14423783), title = warning + " No skin found", description = pre_desc+("\n".join([e_poss.title() for e_poss in possible_])))
                    await msg.channel.send(embed = embed)
                    return

        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e

    elif (await gb_command_check(msg, "inv", "")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        if msg.author.id not in staff:
            await emb_send(chl, warning + " This command is currently private. Please wait for public announcement in Gamebot Support Server")
            return
        try:
            
            #user_name = gb_command_fix(msg, "inv")
            #mdata = ['trD', 'yoboiNitrox', 13651729, [{'i': 169, 'c': 0, 's': 2755840}, {'i': 2728, 'c': 1, 's': 69936239}, {'i': 1901, 'c': 3, 's': 70901485}, {'i': 1910, 'c': 2, 's': 70903264}, {'i': 1914, 'c': 1, 's': 70998294}, {'i': 1913, 'c': 1, 's': 71008735}, {'i': 1907, 'c': 3, 's': 71009758}, {'i': 1908, 'c': 1, 's': 71173049}, {'i': 1904, 'c': 1, 's': 72920545}, {'i': 1131, 'c': 1, 's': 74573613}, {'i': 2454, 'c': 1, 's': 82707569}, {'i': 2710, 'c': 1, 's': 83345183}], [{'i': 1614, 'c': 0, 's': 61268673}, {'i': 1226, 'c': 0, 's': 71459977}, {'i': 1597, 'c': 0, 's': 71626712}, {'i': 1227, 'c': 0, 's': 72293167}, {'i': 1167, 'c': 0, 's': 72390853}, {'i': 1172, 'c': 0, 's': 73353845}, {'i': 875, 'c': 0, 's': 78239619}, {'i': 1954, 'c': 0, 's': 80499682}, {'i': 1590, 'c': 1, 's': 61251808}, {'i': 1589, 'c': 1, 's': 61370581}, {'i': 1352, 'c': 1, 's': 61954147}, {'i': 1367, 'c': 1, 's': 69452576}, {'i': 1325, 'c': 1, 's': 69776996}, {'i': 1269, 'c': 1, 's': 69779275}, {'i': 1101, 'c': 1, 's': 69781747}, {'i': 1429, 'c': 1, 's': 69784228}, {'i': 1594, 'c': 1, 's': 70228361}, {'i': 1371, 'c': 1, 's': 70231253}, {'i': 1508, 'c': 1, 's': 70234358}, {'i': 1296, 'c': 1, 's': 70457696}, {'i': 1916, 'c': 2, 's': 71456501}, {'i': 1911, 'c': 1, 's': 71457224}, {'i': 1915, 'c': 1, 's': 71461427}, {'i': 1907, 'c': 2, 's': 71461708}, {'i': 1544, 'c': 2, 's': 71636785}, {'i': 1900, 'c': 2, 's': 71637704}, {'i': 1585, 'c': 1, 's': 72049553}, {'i': 1390, 'c': 1, 's': 72089445}, {'i': 1416, 'c': 1, 's': 72292294}, {'i': 1286, 'c': 1, 's': 73008315}, {'i': 1901, 'c': 1, 's': 73178351}, {'i': 1272, 'c': 1, 's': 73347496}, {'i': 1274, 'c': 1, 's': 73347555}, {'i': 1415, 'c': 1, 's': 73348536}, {'i': 1319, 'c': 1, 's': 73887507}, {'i': 2356, 'c': 1, 's': 75058347}, {'i': 1203, 'c': 1, 's': 77998451}, {'i': 1470, 'c': 1, 's': 77998551}, {'i': 241, 'c': 1, 's': 77998591}, {'i': 1437, 'c': 1, 's': 78072812}, {'i': 2204, 'c': 1, 's': 78072815}, {'i': 991, 'c': 1, 's': 78078100}, {'i': 1083, 'c': 1, 's': 78078172}, {'i': 1196, 'c': 1, 's': 78078219}, {'i': 1131, 'c': 1, 's': 78078335}, {'i': 1708, 'c': 1, 's': 78078386}, {'i': 1078, 'c': 1, 's': 78082880}, {'i': 609, 'c': 1, 's': 78213703}, {'i': 696, 'c': 1, 's': 78242535}, {'i': 194, 'c': 1, 's': 78242567}, {'i': 639, 'c': 1, 's': 78242590}, {'i': 1633, 'c': 1, 's': 78789632}, {'i': 2131, 'c': 1, 's': 79292496}, {'i': 2421, 'c': 1, 's': 79989425}, {'i': 50, 'c': 1, 's': 80492895}, {'i': 2073, 'c': 1, 's': 80514344}, {'i': 2100, 'c': 1, 's': 80833611}, {'i': 2285, 'c': 1, 's': 81228749}, {'i': 2249, 'c': 1, 's': 81481615}, {'i': 1081, 'c': 1, 's': 81637649}, {'i': 2141, 'c': 1, 's': 82159084}, {'i': 2044, 'c': 1, 's': 82537292}, {'i': 2107, 'c': 1, 's': 83025605}, {'i': 1799, 'c': 1, 's': 83157876}, {'i': 1941, 'c': 1, 's': 83567416}, {'i': 1727, 'c': 1, 's': 83795480}, {'i': 2728, 'c': 1, 's': 83929793}]]
            #mdata = ['trD', 'gornt1', 15393392, [[{'i': 169, 'c': 0, 's': 2755840}, {'i': 1536, 'c': 1, 's': 69936239}, {'i': 1901, 'c': 3, 's': 70901485}, {'i': 1910, 'c': 2, 's': 70903264}, {'i': 1914, 'c': 1, 's': 70998294}, {'i': 1913, 'c': 1, 's': 71008735}, {'i': 1907, 'c': 3, 's': 71009758}, {'i': 1908, 'c': 1, 's': 71173049}, {'i': 1904, 'c': 1, 's': 72920545}, {'i': 1131, 'c': 1, 's': 74573613}, {'i': 2454, 'c': 1, 's': 82707569}, {'i': 2710, 'c': 1, 's': 83345183}], [{'i': 2278, 'c': 1, 's': 77145966}, {'i': 271, 'c': 1, 's': 77905306}, {'i': 263, 'c': 1, 's': 77907034}, {'i': 2358, 'c': 1, 's': 77912607}, {'i': 2165, 'c': 1, 's': 77913138}, {'i': 2480, 'c': 1, 's': 78045236}, {'i': 1862, 'c': 1, 's': 78170843}, {'i': 986, 'c': 1, 's': 78317508}, {'i': 2133, 'c': 1, 's': 78928591}, {'i': 1218, 'c': 1, 's': 79019078}, {'i': 2201, 'c': 1, 's': 80183597}, {'i': 145, 'c': 1, 's': 80311988}, {'i': 201, 'c': 1, 's': 80311989}, {'i': 207, 'c': 1, 's': 80311990}, {'i': 208, 'c': 1, 's': 80311991}, {'i': 48, 'c': 3, 's': 80311997}, {'i': 51, 'c': 2, 's': 80311998}, {'i': 52, 'c': 1, 's': 80311999}, {'i': 1204, 'c': 1, 's': 80326209}, {'i': 2026, 'c': 1, 's': 80695222}, {'i': 393, 'c': 1, 's': 80715073}, {'i': 373, 'c': 1, 's': 80793625}, {'i': 824, 'c': 1, 's': 80793679}, {'i': 2428, 'c': 1, 's': 80803313}, {'i': 408, 'c': 1, 's': 81059593}, {'i': 144, 'c': 1, 's': 81079307}, {'i': 2705, 'c': 1, 's': 81377942}, {'i': 2329, 'c': 1, 's': 81436975}, {'i': 2265, 'c': 2, 's': 81526161}, {'i': 2249, 'c': 1, 's': 81526171}, {'i': 2250, 'c': 1, 's': 81526172}, {'i': 823, 'c': 1, 's': 81589266}, {'i': 822, 'c': 1, 's': 81595894}, {'i': 1268, 'c': 1, 's': 81647975}, {'i': 1272, 'c': 1, 's': 81647978}, {'i': 1282, 'c': 1, 's': 81728486}, {'i': 147, 'c': 1, 's': 81729306}, {'i': 2259, 'c': 1, 's': 81729726}, {'i': 1273, 'c': 1, 's': 81729868}, {'i': 2280, 'c': 1, 's': 81750967}, {'i': 1266, 'c': 1, 's': 81751122}, {'i': 1267, 'c': 1, 's': 81751133}, {'i': 1274, 'c': 1, 's': 81751175}, {'i': 1277, 'c': 1, 's': 81751275}, {'i': 1265, 'c': 1, 's': 81751349}, {'i': 1264, 'c': 1, 's': 81751369}, {'i': 1271, 'c': 1, 's': 81846154}, {'i': 1275, 'c': 1, 's': 81846185}, {'i': 1129, 'c': 1, 's': 81929171}, {'i': 1298, 'c': 1, 's': 81955988}, {'i': 1295, 'c': 1, 's': 81956073}, {'i': 2122, 'c': 1, 's': 82177039}, {'i': 1269, 'c': 1, 's': 82276837}, {'i': 1270, 'c': 1, 's': 82276863}, {'i': 94, 'c': 1, 's': 82276886}, {'i': 43, 'c': 1, 's': 82288478}, {'i': 44, 'c': 1, 's': 82288479}, {'i': 46, 'c': 1, 's': 82288480}, {'i': 49, 'c': 1, 's': 82288481}, {'i': 50, 'c': 1, 's': 82288482}, {'i': 95, 'c': 1, 's': 82288530}, {'i': 146, 'c': 1, 's': 82289964}, {'i': 200, 'c': 1, 's': 82289965}, {'i': 47, 'c': 1, 's': 82289966}, {'i': 0, 'c': 1, 's': 82295922}, {'i': 1778, 'c': 1, 's': 82325731}, {'i': 2390, 'c': 1, 's': 82478550}, {'i': 409, 'c': 1, 's': 82531670}, {'i': 959, 'c': 1, 's': 82531671}, {'i': 2285, 'c': 1, 's': 82804983}, {'i': 2086, 'c': 1, 's': 82830271}, {'i': 2138, 'c': 1, 's': 82948751}, {'i': 1978, 'c': 1, 's': 83152214}, {'i': 2734, 'c': 1, 's': 83245252}, {'i': 1695, 'c': 1, 's': 83430984}, {'i': 2400, 'c': 1, 's': 83465340}, {'i': 2364, 'c': 1, 's': 83465353}, {'i': 74, 'c': 1, 's': 83602205}, {'i': 2150, 'c': 1, 's': 83682068}, {'i': 2465, 'c': 1, 's': 83682069}, {'i': 2341, 'c': 1, 's': 83729675}, {'i': 2547, 'c': 1, 's': 83729676}, {'i': 2215, 'c': 1, 's': 83900619}, {'i': 2226, 'c': 1, 's': 83961026}, {'i': 2729, 'c': 1, 's': 84096181}, {'i': 2337, 'c': 1, 's': 84099351}]]]
            mdata = ['trD', 'StremZ', 5045705, [[{'i': 169, 'c': 0, 's': 2755840}, {'i': 1536, 'c': 1, 's': 69936239}, {'i': 1901, 'c': 3, 's': 70901485}, {'i': 1910, 'c': 2, 's': 70903264}, {'i': 1914, 'c': 1, 's': 70998294}, {'i': 1913, 'c': 1, 's': 71008735}, {'i': 1907, 'c': 3, 's': 71009758}, {'i': 1908, 'c': 1, 's': 71173049}, {'i': 1904, 'c': 1, 's': 72920545}, {'i': 1131, 'c': 1, 's': 74573613}, {'i': 2454, 'c': 1, 's': 82707569}, {'i': 2710, 'c': 1, 's': 83345183}], [{'i': 2425, 'c': 0, 's': 75956755}, {'i': 2423, 'c': 0, 's': 75991790}, {'i': 2115, 'c': 0, 's': 80649804}, {'i': 395, 'c': 1, 's': 19966451}, {'i': 943, 'c': 1, 's': 39496854}, {'i': 942, 'c': 1, 's': 39609213}, {'i': 419, 'c': 1, 's': 41388667}, {'i': 1066, 'c': 1, 's': 42716939}, {'i': 1069, 'c': 2, 's': 46906001}, {'i': 1067, 'c': 1, 's': 50148421}, {'i': 1403, 'c': 1, 's': 53074892}, {'i': 1405, 'c': 1, 's': 53074893}, {'i': 1073, 'c': 1, 's': 53998571}, {'i': 1533, 'c': 1, 's': 54743977}, {'i': 1072, 'c': 1, 's': 56818308}, {'i': 1641, 'c': 1, 's': 57488548}, {'i': 1483, 'c': 1, 's': 60217191}, {'i': 1642, 'c': 1, 's': 61317723}, {'i': 1734, 'c': 1, 's': 63406205}, {'i': 1795, 'c': 1, 's': 64154614}, {'i': 1874, 'c': 1, 's': 65563919}, {'i': 1893, 'c': 2, 's': 69703692}, {'i': 1908, 'c': 182, 's': 70679382}, {'i': 1903, 'c': 27, 's': 70679815}, {'i': 1900, 'c': 155, 's': 70680476}, {'i': 1907, 'c': 139, 's': 70682625}, {'i': 1904, 'c': 137, 's': 70684467}, {'i': 1909, 'c': 35, 's': 70686822}, {'i': 1901, 'c': 152, 's': 70689238}, {'i': 1902, 'c': 18, 's': 70781165}, {'i': 1659, 'c': 1, 's': 70782799}, {'i': 1911, 'c': 133, 's': 70822771}, {'i': 1910, 'c': 101, 's': 70825234}, {'i': 1912, 'c': 5, 's': 70945325}, {'i': 1913, 'c': 85, 's': 71012015}, {'i': 1915, 'c': 6, 's': 71106386}, {'i': 1914, 'c': 11, 's': 71133628}, {'i': 1916, 'c': 93, 's': 71288044}, {'i': 1898, 'c': 1, 's': 71498038}, {'i': 886, 'c': 1, 's': 72844673}, {'i': 1895, 'c': 1, 's': 73211458}, {'i': 1672, 'c': 1, 's': 74872920}, {'i': 1866, 'c': 1, 's': 74968913}, {'i': 2361, 'c': 1, 's': 74982953}, {'i': 2350, 'c': 3, 's': 74982971}, {'i': 2329, 'c': 1, 's': 74983097}, {'i': 1945, 'c': 1, 's': 74983227}, {'i': 2322, 'c': 1, 's': 74983474}, {'i': 2398, 'c': 1, 's': 74983526}, {'i': 2132, 'c': 1, 's': 74985504}, {'i': 2365, 'c': 1, 's': 74985935}, {'i': 2366, 'c': 1, 's': 74986160}, {'i': 2411, 'c': 1, 's': 74987386}, {'i': 2379, 'c': 1, 's': 74987841}, {'i': 2177, 'c': 1, 's': 74988196}, {'i': 2239, 'c': 1, 's': 74988289}, {'i': 2262, 'c': 1, 's': 74988667}, {'i': 2014, 'c': 1, 's': 74989682}, {'i': 2281, 'c': 1, 's': 74989756}, {'i': 2098, 'c': 3, 's': 74989904}, {'i': 2175, 'c': 1, 's': 74990439}, {'i': 2355, 'c': 1, 's': 74991376}, {'i': 2399, 'c': 1, 's': 74991777}, {'i': 2167, 'c': 1, 's': 74992288}, {'i': 1975, 'c': 1, 's': 74992441}, {'i': 2193, 'c': 1, 's': 74992543}, {'i': 2394, 'c': 1, 's': 74992690}, {'i': 2237, 'c': 3, 's': 74993180}, {'i': 2057, 'c': 1, 's': 74993356}, {'i': 1941, 'c': 1, 's': 74993371}, {'i': 2334, 'c': 1, 's': 74994078}, {'i': 1976, 'c': 1, 's': 74994184}, {'i': 1950, 'c': 1, 's': 74994706}, {'i': 2046, 'c': 1, 's': 74994753}, {'i': 2321, 'c': 1, 's': 74995216}, {'i': 2235, 'c': 1, 's': 74995506}, {'i': 1985, 'c': 1, 's': 74996466}, {'i': 1983, 'c': 1, 's': 74998342}, {'i': 2034, 'c': 1, 's': 74999397}, {'i': 2063, 'c': 1, 's': 75000555}, {'i': 2171, 'c': 1, 's': 75000668}, {'i': 2410, 'c': 1, 's': 75000817}, {'i': 2311, 'c': 1, 's': 75000840}, {'i': 2058, 'c': 1, 's': 75002887}, {'i': 2267, 'c': 1, 's': 75004461}, {'i': 2141, 'c': 1, 's': 75004599}, {'i': 2104, 'c': 1, 's': 75004725}, {'i': 2110, 'c': 2, 's': 75004927}, {'i': 2391, 'c': 1, 's': 75008471}, {'i': 2153, 'c': 1, 's': 75009188}, {'i': 2346, 'c': 1, 's': 75013114}, {'i': 2181, 'c': 1, 's': 75013687}, {'i': 2414, 'c': 1, 's': 75014919}, {'i': 2353, 'c': 1, 's': 75015980}, {'i': 1954, 'c': 1, 's': 75016448}, {'i': 2027, 'c': 1, 's': 75020520}, {'i': 2382, 'c': 1, 's': 75028126}, {'i': 1987, 'c': 1, 's': 75029088}, {'i': 2026, 'c': 1, 's': 75035181}, {'i': 2130, 'c': 1, 's': 75195951}, {'i': 2454, 'c': 1, 's': 75368271}, {'i': 2460, 'c': 1, 's': 75692452}, {'i': 2538, 'c': 1, 's': 75987164}, {'i': 1964, 'c': 1, 's': 75990274}, {'i': 2436, 'c': 1, 's': 75994484}, {'i': 2452, 'c': 1, 's': 76091666}, {'i': 2430, 'c': 2, 's': 76407777}, {'i': 1892, 'c': 2, 's': 76643539}, {'i': 2468, 'c': 1, 's': 77026502}, {'i': 1873, 'c': 1, 's': 77464282}, {'i': 1872, 'c': 1, 's': 77477884}, {'i': 1868, 'c': 1, 's': 77477890}, {'i': 1897, 'c': 1, 's': 78265783}, {'i': 2571, 'c': 1, 's': 78542102}, {'i': 2587, 'c': 9, 's': 79200825}, {'i': 2633, 'c': 6, 's': 79200848}, {'i': 2655, 'c': 8, 's': 79200857}, {'i': 2586, 'c': 6, 's': 79200862}, {'i': 2657, 'c': 8, 's': 79200880}, {'i': 2696, 'c': 5, 's': 79200904}, {'i': 2677, 'c': 6, 's': 79200943}, {'i': 2679, 'c': 3, 's': 79200983}, {'i': 2687, 'c': 5, 's': 79203782}, {'i': 2665, 'c': 5, 's': 79203882}, {'i': 2654, 'c': 4, 's': 79203902}, {'i': 2648, 'c': 3, 's': 79204007}, {'i': 2592, 'c': 1, 's': 79204063}, {'i': 2597, 'c': 3, 's': 79204160}, {'i': 2581, 'c': 7, 's': 79204260}, {'i': 2673, 'c': 3, 's': 79204275}, {'i': 2685, 'c': 5, 's': 79204307}, {'i': 2684, 'c': 3, 's': 79204319}, {'i': 2603, 'c': 5, 's': 79204346}, {'i': 2582, 'c': 7, 's': 79204490}, {'i': 2689, 'c': 5, 's': 79204513}, {'i': 2688, 'c': 8, 's': 79205726}, {'i': 2622, 'c': 3, 's': 79205840}, {'i': 2626, 'c': 5, 's': 79205854}, {'i': 2645, 'c': 6, 's': 79205863}, {'i': 2692, 'c': 10, 's': 79206424}, {'i': 2612, 'c': 7, 's': 79206547}, {'i': 2691, 'c': 7, 's': 79206570}, {'i': 2599, 'c': 7, 's': 79206601}, {'i': 2646, 'c': 6, 's': 79206643}, {'i': 2662, 'c': 6, 's': 79206676}, {'i': 2642, 'c': 4, 's': 79206682}, {'i': 2675, 'c': 5, 's': 79206697}, {'i': 2609, 'c': 5, 's': 79206780}, {'i': 2619, 'c': 4, 's': 79206852}, {'i': 2616, 'c': 7, 's': 79206918}, {'i': 2596, 'c': 2, 's': 79206986}, {'i': 2651, 'c': 1, 's': 79207114}, {'i': 2678, 'c': 6, 's': 79207258}, {'i': 2693, 'c': 3, 's': 79207278}, {'i': 2660, 'c': 4, 's': 79207334}, {'i': 2672, 'c': 5, 's': 79207515}, {'i': 2636, 'c': 2, 's': 79207614}, {'i': 2623, 'c': 2, 's': 79207640}, {'i': 2680, 'c': 4, 's': 79207693}, {'i': 2686, 'c': 3, 's': 79207721}, {'i': 2671, 'c': 3, 's': 79207776}, {'i': 2629, 'c': 5, 's': 79207834}, {'i': 2637, 'c': 5, 's': 79207955}, {'i': 2617, 'c': 3, 's': 79208015}, {'i': 2583, 'c': 5, 's': 79214219}, {'i': 2674, 'c': 2, 's': 79214419}, {'i': 2639, 'c': 5, 's': 79214770}, {'i': 2681, 'c': 2, 's': 79214825}, {'i': 2661, 'c': 3, 's': 79214846}, {'i': 2613, 'c': 5, 's': 79214952}, {'i': 2627, 'c': 2, 's': 79214965}, {'i': 2683, 'c': 3, 's': 79214993}, {'i': 2668, 'c': 3, 's': 79215154}, {'i': 2682, 'c': 4, 's': 79215203}, {'i': 2666, 'c': 2, 's': 79215215}, {'i': 2589, 'c': 3, 's': 79215591}, {'i': 2606, 'c': 3, 's': 79215630}, {'i': 2632, 'c': 1, 's': 79222931}, {'i': 2697, 'c': 3, 's': 79223090}, {'i': 2593, 'c': 3, 's': 79223359}, {'i': 2676, 'c': 2, 's': 79223485}, {'i': 2607, 'c': 2, 's': 79227021}, {'i': 2694, 'c': 1, 's': 79669436}, {'i': 2690, 'c': 1, 's': 79669476}, {'i': 1896, 'c': 1, 's': 79679704}, {'i': 2427, 'c': 1, 's': 79685789}, {'i': 2568, 'c': 1, 's': 80472715}, {'i': 1894, 'c': 1, 's': 80765552}, {'i': 2746, 'c': 1, 's': 81614756}, {'i': 2715, 'c': 1, 's': 81872328}, {'i': 2789, 'c': 1, 's': 82916072}, {'i': 2790, 'c': 1, 's': 82938023}, {'i': 2788, 'c': 1, 's': 83028472}, {'i': 2808, 'c': 1, 's': 83283797}, {'i': 2774, 'c': 1, 's': 83377695}, {'i': 2809, 'c': 1, 's': 83467971}, {'i': 2810, 'c': 1, 's': 83467972}, {'i': 2806, 'c': 1, 's': 83467974}, {'i': 2801, 'c': 1, 's': 83467977}, {'i': 2787, 'c': 1, 's': 83467980}, {'i': 2786, 'c': 1, 's': 83467982}, {'i': 2785, 'c': 1, 's': 83467985}, {'i': 2784, 'c': 1, 's': 83467988}, {'i': 2818, 'c': 1, 's': 83467994}, {'i': 2813, 'c': 1, 's': 83467995}, {'i': 2827, 'c': 1, 's': 84109360}, {'i': 2817, 'c': 1, 's': 84109532}]]]

                       
            data = mdata[3][1]

            
            
            #ask = await message.channel.send()
            def check(reaction, user_, msg, ask):
                return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id

        

            pages = math.ceil(len(data)/8)
            if pages > 1:has_pages = True
            else:has_pages = False
            current_page = 1
            start = 0
            started = False
            while True:
                try:
                    if started:
                        reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
                except asyncio.TimeoutError:await ask.clear_reactions();return
                else:
                    if started:
                        if str(reaction.emoji) == stop:
                            await ask.clear_reactions();break
                        elif str(reaction.emoji) == next_page:
                            if current_page == pages:
                                await ask.remove_reaction(next_page, msg.author)
                                continue;
                            start += 8
                            await ask.delete()
                            current_page += 1
                            
                        elif str(reaction.emoji) == prev_page:
                            if current_page == 1:
                                await ask.remove_reaction(prev_page, msg.author)
                                continue;
                            start -= 8
                            await ask.delete()
                            current_page -= 1


                    thing = functools.partial(make_inv, data, client, PyJsHoisted_getPreview_, start)
                    with ThreadPoolExecutor(max_workers = 1) as executor:
                        byte_io = await client.loop.run_in_executor(executor, thing)
                    ask = await msg.channel.send(file=discord.File(byte_io, "inventory.png"))
                
    
                    if not started:
                        started = True
                        await msg.remove_reaction(loading, client.user)
                    if not has_pages:break
                    await ask.add_reaction(prev_page)
                    await ask.add_reaction(stop)
                    await ask.add_reaction(next_page)
                    

        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            raise e
    
    elif (await gb_command_check(msg, "hub")):
        client.loop.create_task( do_on_message(msg))
        map_name = gb_command_fix(msg, "hub")
        desc = """
● [Profile Page](https://krunker.io/social.html?p=profile&q={0})"""
        if len(map_name) <= 5:desc += """
● [Clan Page](https://krunker.io/social.html?p=clan&q={0})"""
        desc += """
● [Mod Page](https://krunker.io/social.html?p=mod&q={0})
● [Map Social Page](https://krunker.io/social.html?p=map&q={0})
● [Quick Map Play](https://krunker.io/?play={0})

*Only choose the page you wanted to check*
"""
        await message.reply(embed=discord.Embed(title = " Social Hub Links:", description = desc.format(map_name), colour=discord.Colour(14423783)))
    elif (await gb_command_check(msg, "auto_manage disable", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):
            return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("**Are you sure** you want to disable auto manage module?")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling *disable* after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" *Disable* Cancelled!");return
                if msg_.content.lower() == "yes":
                    break
                if msg_.content.lower() == "no":
                    return
                
        old_data[msg.guild.id]["disabled"] = True
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        await msg.channel.send("Auto Managing has been disabled")

    elif (await gb_command_check(msg, "auto_manage enable", "", 1)):
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):
            return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("**Are you sure** you want to enable auto manage module?")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling *enable* after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" *Enable* Cancelled!");return
                if msg_.content.lower() == "yes":
                    break
                if msg_.content.lower() == "no":
                    return
                
        old_data[msg.guild.id]["disabled"] = False
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        await msg.channel.send("Auto Managing has been enabled")

        
    elif (await gb_command_check(msg, "auto_manage", "", 1)) and msg.author.id in admins:
        with open("Data/servers.bt", "rb") as file:
            old_data = pickle.load(file)
        #{1234: {"cn": ".map", "rl": role, "mng" : [], "all_linked": True}}
        def check(m):return m.channel == message.channel and m.author == message.author
        await message.channel.send("Alright. This will enable `Server Managing` feature. Follow the instructions...")
        await asyncio.sleep(1.5)
        while True:
            await message.channel.send("`Enter your clan name: `")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");break
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                clan_name = msg_.content;break
        await asyncio.sleep(1)
        while True:
            await message.channel.send("\n\n`Enter the Clan-Member Role Name, Don't Ping!`\n*- Its CaSe SeNsItIvE*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                role = discord.utils.get(msg.guild.roles, name= msg_.content)
                if role == None:await message.channel.send(warning + " No role found\n");await asyncio.sleep(2)
                else:break
        while True:
            await message.channel.send("`Do you have` *`Recruit, Soldier, Captain`* `roles as well?`")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                elif msg_.content.lower() == "no":roles_list = [];break
                elif msg_.content.lower() == "yes":
                    while True:
                        await message.channel.send("Enter your roles in the following **exact** format:\n\n`recruit|soldier|captain`")
                        try:msg_ = await client.wait_for('message', check=check, timeout=100)
                        except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
                        else:
                            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                            roles = msg_.content.split("|")
                            roles_list = []
                            try:
                                for role_ in roles:roles_list.append(discord.utils.get(msg.guild.roles, name= role_).id)
                            except:
                                await message.channel.send(warning + " One or more roles not found!\n*Its CaSe SeNsItIvE*")
                                await asyncio.sleep(2)
                            else:break
                    break
        await asyncio.sleep(1)
        while True:
            await message.channel.send("""\n\nEnter the nickname you want clan members to be replaced with (Examples below):\n\n```
[{clan}] {ign}
[{clan}] {ign} {nm}
{nm}```

Note that:
```
{clan} = Clan Name
{ign} = In-Game Name
{nm} = Username On Discord
{nick} = Current User Nick (selecting this won't edit nicks)
```""")
            
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");break
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                name_template = msg_.content
                break
        data = await get_user_data(clan_name, "clan")
        try:
            user_name = data[3]['clan_name']
            creator = data[3]['creatorname']
        except:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" No clan found"))
            return
        maps = data[3]["members"]
        clan_members = [e_map["p"].lower() for e_map in maps]
        clan_members2 = [e_map["p"] for e_map in maps]
        clan_member_ranks = {e_map["p"].lower():e_map["r"] for e_map in maps}
        if role != None:old_data[msg.guild.id] = {"cn": clan_name, "rl": role.id, "mng": [msg.author.id], "msg": name_template, "rank":roles_list, "disabled": False, "logs":None}
        with open("Data/servers.bt", "wb") as file:pickle.dump(old_data, file)
        await message.channel.send(taskdone+ " Server management has been enabled. Note that all clan members must be linked, Use `g.help link`")
        await asyncio.sleep(1)
        notified = False
        notified2 = False
        server_mems = {}
        for e_mem in clan_members:
            try: server_mems[msg.guild.get_member((await get_author_name(None, e_mem)).id)] = e_mem.lower()
            except: pass
        for member, ln_acc in server_mems.items():
            try:
                if creator.lower() == ln_acc.lower():
                    continue
                mem_nick = member.nick if member.nick != None else member.name
                nick_n = name_template.replace("{clan}", user_name).replace("{ign}", clan_members2[clan_members.index(ln_acc)]).replace("{nm}", member.name).replace("{nick}", mem_nick)
                if mem_nick != nick_n and name_template != "{nick}":
                    await member.edit(nick = nick_n)
                    await asyncio.sleep(0.4)
                if role not in member.roles:
                    await member.add_roles(role)
                    await asyncio.sleep(0.4)
                e_role = clan_member_ranks[ln_acc]
                if (rrole := msg.guild.get_role(roles_list[e_role])) not in member.roles:
                    await member.add_roles(rrole)
                    await asyncio.sleep(0.4)
                for e_role in roles_list:
                    if (arole := msg.guild.get_role(e_role)) in member.roles and arole != rrole:
                        await member.remove_roles(arole)
                        await asyncio.sleep(0.4)
                    
                        
            except Exception as e:
                if not notified:
                    await msg.channel.send(warning + " If you haven't enabled Managed Nickname/Manage Roles perms, make sure to enable them")
                    notified = True
                if not notified2:
                    await msg.channel.send(warning + " If some clan members are not linked, please have them linked before a server manage occurs! Use `g.help link` to get more details...")
                    notified2 = True
        roles_list_obj = [msg.guild.get_role(e_role) for e_role in roles_list]
        try:
            all_roled_mems = list(set(role.members + roles_list_obj[0].members + roles_list_obj[1].members + roles_list_obj[2].members))
        except:
            all_roled_mems = role.members
        for member in all_roled_mems:
            try:
                if (user := (await get_author_obj(None, member.id, False)).lower()) not in clan_members:
                    if creator.lower() == user.lower():
                        continue
                    await member.edit(nick = member.name);
                    if role in member.roles:
                        await member.remove_roles(role)
                    for e_role in roles_list:
                        if (rrole := msg.guild.get_role(e_role)) in member.roles:
                            await member.remove_roles(rrole)
                            await asyncio.sleep(0.4)
                    await asyncio.sleep(1)
            except:pass
    elif (await gb_command_check(msg, "set_levels", "", 1)) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        if not msg.channel.permissions_for(msg.guild.me).manage_roles:
            await emb_send(chl, warning+" Bot needs manage roles perm",
                           footer_t = "Also ensure that the gamebot role is above the roles you want it to assign")
            return
        data = get_var("levels")
        def check(m):return m.channel == message.channel and m.author == message.author
        await message.channel.send("This will enable assigning level roles to members automatically!")
        await asyncio.sleep(1.5)
        await message.channel.send("""Enter the names your roles in the following **exact** format, don't ping:

`20+|30+|40+`

*Use `skip` instead of name if you don't have the role*""")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                roles = msg_.content.split("|")
                roles_list = []
                try:
                    for role_ in roles:
                        if role_ == "skip":
                            roles_list.append(0)
                        else:
                            roles_list.append(discord.utils.get(msg.guild.roles, name= role_).id)
                except:
                    await message.channel.send(warning + " One or more roles not found!\n*Its CaSe SeNsItIvE*")
                    await asyncio.sleep(2)
                else:break
        await asyncio.sleep(1)
        data[msg.guild.id] = {"20": roles_list[0], "30": roles_list[1], "40": roles_list[2]}
        define_var("levels", data)
        await emb_send(chl, taskdone+ " Now server members can use `g.level` to get level roles.", footer_t = "User must be linked")
    elif (await gb_command_check(msg, "level", "", 1)) or (await gb_command_check(msg, "levels", "", 1)):
        client.loop.create_task(do_on_message(msg, -1))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            return
        try:
            role_data = get_var("levels")[msg.guild.id]
        except:await emb_send(chl, warning + " Please enable automated level assigning using `g.set_levels`")
        try:
            if (await gb_command_check(msg, "level", "", 1)):
                if not (user_name := (await get_author_command(msg, "level"))):
                    await emb_send(chl,
                                   title_ = warning + " Please get your account linked to get level roles automatically!",cnt = "Use `g.link <kr-username>` to link your account");return
            elif (await gb_command_check(msg, "levels", "", 1)):
                if not (user_name := (await get_author_command(msg, "levels"))):
                    await emb_send(chl,
                                   title_ = warning + " Please get your account linked to get level roles automatically!",cnt = "Use `g.link <kr-username>` to link your account");return

            mdata = await get_user_data(unquote(unquote(user_name)), pf__ = 1)
            if mdata == ['cpt']:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Websocket issue. It must be fixed within few hours or mins.", description = "If the problem persists, contact bot dev"))
                await fetching.delete()
                return
            try:data = mdata[3]
            except:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Received incorrect data.", description = "Try again. If problem persists, contact bot dev"))
                await fetching.delete()
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                return
            if data == None:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " No user account found"))
                await fetching.delete()
                return
            user_level = max(1, math.floor(0.03 * math.sqrt(data["player_score"])))
            assigned_roles = 0
            for num in range(20, 41, 10):
                if role_data[str(num)]:
                    role = msg.guild.get_role(role_data[str(num)])
                    if user_level >= num and role not in msg.author.roles:
                        await msg.author.add_roles(role)
                        assigned_roles += 1
                    elif user_level < num and role in msg.author.roles:
                        await msg.author.remove_roles(role)
                        assigned_roles -= 1
                    

            if assigned_roles > 0:
                await emb_send(chl, taskdone + " Added {} roles".format(assigned_roles))
            elif assigned_roles == 0:
                await emb_send(chl, taskdone + " Your roles are up-to-date")
            else:
                await emb_send(chl, taskdone + " Removed {} roles".format(abs(assigned_roles)))
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            await fetching.delete()
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "unsweep", "", 1)) and msg.author.id in staff:
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        def check(m):return m.channel == message.channel and m.author == message.author
        await message.channel.send("`Enter server ID: `")
        try:msg_ = await client.wait_for('message', check=check, timeout=100)
        except asyncio.TimeoutError:pass
        else:
            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Unsweepment Cancelled!");return
            del old_data[int(msg_.content)]
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
    elif (await gb_command_check(msg, "sweeper", "", 1)) and msg.author.id in staff:
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        #{".map": {"mng":[], "tm":1 or 7 or 30}}
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("`Enter your clan name to register for sweeps: `")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling registration after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Registration Cancelled!");return
                clan_name = msg_.content;break
        await asyncio.sleep(0.7)
        data = await get_user_data(clan_name, "clan")
        mngers = [msg.author.id]
        if 669816890163724288 not in mngers:mngers.append(669816890163724288)
        old_data[msg.guild.id] = {"cn":clan_name.lower(), "data": data[3],"mng":mngers, "tm":2, "p": "2"}
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Registered for sweeps")
        await asyncio.sleep(2)
        await message.channel.send("Note default privacy is `Private, accessible for clan members`, and interval is `Never (Custom Reset)`. You can change these. Use `g.sweeper help`")
    elif (await gb_command_check(msg, "sweeper overall", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        s_data = old_data[msg.guild.id]
        data = await get_user_data(s_data["cn"], "clan")

        old_scores = sum([e_map["s"] for e_map in s_data["data"]["members"]])
        scores = sum([e_map["s"] for e_map in data[3]["members"]])
        
        embed=discord.Embed(colour=discord.Colour(14423783), title = "Overall sweep stats for "+s_data["cn"].upper())
        embed.add_field(name="Old Scores", value=convert_int(old_scores))
        embed.add_field(name="New Scores", value=convert_int(scores))
        embed.add_field(name="Difference", value= convert_int(scores - old_scores))
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "sweeper add", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("Mention the member you wan't to add as manager *(You can also paste id)* . *You must trust the member you are adding*\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling manager add setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        try:
                            mentioned_one = await get_um(user_)
                        except:await message.channel.send(warning+" Incorrect Id!");await asyncio.sleep(2);continue
                            
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        old_data[msg.guild.id]["mng"] = list(data["mng"] + [user_])
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + mentioned_one + " has been added as manager")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "sweeper remove", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("Mention the member you wan't to remove from managers *(You can also paste id)*.\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:
                await message.channel.send(warning+" Automatically cancelling manager add setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        mentioned_one = await get_um(user_)
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        try:
            if user_ == 669816890163724288:
                await message.channel.send(warning+" This user can't be removed!");return
            old_data[msg.guild.id]["mng"].remove(user_)
        except:
            await message.channel.send(warning+" User is not a manager");return
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        embed=discord.Embed(colour=discord.Colour(14423783),
                            description = taskdone + mentioned_one + " has been removed as manager")
        await msg.channel.send(embed = embed)
    elif (await gb_command_check(msg, "sweeper reset", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        data = await get_user_data(data["cn"], "clan")
        old_data[msg.guild.id]["data"] = data[3]
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Resetted sweeps")
    elif (await gb_command_check(msg, "sweeper help", "", 1)):
                
        embed=discord.Embed(colour=discord.Colour(14423783),
                            title = "Sweeper Module Help",
                            description = """
> **`g.sweep <clan-name>`**
*Check clan's sweep*

> **`g.sweeper reset`**
*Reset the sweeps*

> **`g.sweeper add`**
*Add a member as manager*

> **`g.sweeper remove`**
*Remove a member from managers*

> **`g.sweeper managers`**
*Get list of current managers*

> **`g.sweeper privacy`**
*Change sweep's privacy*

> **`g.sweeper interval`**
*Change sweep's reset interval*

*These commands are only accessible by managers\nUse these commands in your clan server*
""")
        await msg.channel.send(embed = embed)

    elif (await gb_command_check(msg, "sweeper managers", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        desc = ""
        for e_mem in data["mng"]:
            desc += await get_um(e_mem)
            desc += "\n"
            
        embed=discord.Embed(colour=discord.Colour(14423783),
                            title = "Managers List",
                            description = desc)
        embed.set_footer(text = "Add a manager using 'g.sweeper add'")

        await msg.channel.send(embed = embed)

    elif (await gb_command_check(msg, "sweeper privacy", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("""Choose privacy:

1 - Private
2 - Private but accessible for clan members
3 - Public

Enter the value:""")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                elif msg_.content not in ["1", "2", "3"]:
                    await message.channel.send(warning+" Incorrect Value!")
                    await asyncio.sleep(1)
                else:publicity = msg_.content;break
        old_data[msg.guild.id]["p"] = publicity
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Changed sweeps privacy!")
    elif (await gb_command_check(msg, "add_background", "", 1)) and msg.author.id in admins:
        old_data = await async_open("Data/backgrounds.bt")
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await emb_send(chl, """Choose background type:

1 - Personal
2 - Clan

Enter the index:""")
            try:msg_ = await client.wait_for('message', check=check, timeout=150)
            except asyncio.TimeoutError:await msg.add_reaction(warning);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                elif msg_.content not in ["1", "2"]:
                    await message.channel.send(warning+" Incorrect Value!")
                    await asyncio.sleep(1)
                else:bg_type = msg_.content;break
        while True:
            await emb_send(chl, "Upload Background:")
            try:msg_ = await client.wait_for('message', check=check, timeout=150)
            except asyncio.TimeoutError:await msg.add_reaction(warning);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    if not msg_.attachments[0].size > 1000000:
                        img = await msg_.attachments[0].read()
                        img_name = msg_.attachments[0].filename
                        img_ext = img_name.rsplit(".", 1)[-1].lower()
                        try:img = Image.open(BytesIO(img))
                        except:await emb_send(msg.channel, warning + " Could not decode the image", footer_t = "Make sure you uploaded the correct image.");return
                        if img.width != 719 or img.height != 464:
                            await emb_send(msg.channel, warning + " Incorrect dimensions. Must be `719 x 464`");return
                        if img.mode not in ["RGBA", "RGB", "P"]:
                            await emb_send(msg.channel, warning + " Incorrect Image mode. Must be RGB/RGBA");return
                        if img_ext not in ["png", "gif"]:
                            await emb_send(msg.channel, warning + " Incorrect Image type. Must be PNG/GIF");return
                        break
                    else:
                        await emb_send(msg.channel, warning + " 1 Mb is the max size. Please try again from start...");return
                except Exception as e:
                    await emb_send(msg.channel, warning + " Please attach image. Try again from start!")
                    raise e
        await emb_send(chl, "Enter the name:")
        try:msg_ = await client.wait_for('message', check=check, timeout=150)
        except asyncio.TimeoutError:await msg.add_reaction(warning)
        else:
            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
            name = msg_.content
        await emb_send(chl, "Is this a premium background?")
        try:msg_ = await client.wait_for('message', check=check, timeout=150)
        except asyncio.TimeoutError:await msg.add_reaction(warning)
        else:
            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
            prem = 1 if msg_.content.lower() == "yes" else 0
        while True:
            await emb_send(chl, "Who owns this background *(You can also paste id)* . *He'll be able to change it later*\n\n*You can type `cancel` to cancel this request*")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await msg.add_reaction(warning);return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                try:
                    user_ = msg_.mentions[0].id
                    mentioned_one = msg_.mentions[0].mention
                except:
                    if len(msg_.content) == 18 and msg_.content.isdigit():
                        user_ = int(msg_.content)
                        try:
                            mentioned_one = await get_um(user_)
                        except:await message.channel.send(warning+" Incorrect Id!");await asyncio.sleep(2);continue
                            
                    else:
                        await message.channel.send(warning+" No mention found");await asyncio.sleep(2);continue
                break
        await emb_send(chl, "Enter the color for the User Name text and the XP bar:\n`#Hex` or `R, G, B` or `skip` for default color")
        utc = await get_color_input(msg)
        if utc == None:return
        if utc == "skip":utc = (227, 126, 255)
        
        for ind in range(1, 1500):
            if not os.path.exists("Data/backgrounds/tem{}".format(ind)+"."+img_ext):
                img.save("Data/backgrounds/tem{}".format(ind)+"."+img_ext, format = img_ext.upper(), save_all = True)
                image_ind = str(ind)+"."+img_ext
                break
        img_data = {"file": "tem"+image_ind,
                    "cm":name,
                    "owners": [dev, user_],
                    "ut":utc,
                    "xp":utc,
                    "hd":(191, 176, 190),
                    "txt": "",
                    "lgc": 0,
                    "prem": prem}
        old_data = await async_open("Data/backgrounds.bt")
        try:
            old_data["p" if bg_type == "1" else "c"].append(img_data)
        except:
            old_data["p" if bg_type == "1" else "c"] = [img_data]
        
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Saved the background")
        await compile_bgs()
        await client.get_guild(708067789830750449).get_channel(756471541281325146).send("`New background: {}` - `Creator` -> {}".format(name, msg.author))
    elif (await gb_command_check(msg, "add")) and msg.author.id in admins:
        data = gb_command_fix(msg, "add")
        data = data.split(" ", 2)
        prem = 0
        if data[0].lower() == "pbg":
            bg_type = "1"
        elif data[0].lower() == "cbg":
            bg_type = "2"
            if data[2].endswith("space"):
                data[2] = data[2][:-5] + " "
        elif data[0].lower() == "ppbg":
            bg_type = "1"
            prem = 1
        old_data = await async_open("Data/backgrounds.bt")
        
        img = client.default_bg[0].copy()
        img_ext = "png"
        name = data[2]
        user_ = int(data[1])
        mentioned_one = await get_um(user_)
        utc = (227, 126, 255)
        
        for ind in range(1, 1500):
            if not os.path.exists("Data/backgrounds/tem{}".format(ind)+"."+img_ext):
                img.save("Data/backgrounds/tem{}".format(ind)+"."+img_ext, format = img_ext.upper(), save_all = True)
                image_ind = str(ind)+"."+img_ext
                break
        img_data = {"file": "tem"+image_ind,
                    "cm":name,
                    "owners": [dev, user_],
                    "ut":utc,
                    "xp":utc,
                    "hd":utc,
                    "txt": "",
                    "lgc": 0,
                    "prem": prem,
                    "brd":{"outl":1, "shd":0, "xpb":1, "clr":(255, 255, 255)}}
        try:
            old_data["p" if bg_type == "1" else "c"].append(img_data)
        except:
            old_data["p" if bg_type == "1" else "c"] = [img_data]
        
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Saved the background")
        await compile_bgs()
        await client.get_guild(708067789830750449).get_channel(756471541281325146).send("`New background: {}` - `Creator` -> {}".format(name, msg.author))
    elif (await gb_command_check(msg, "sweeper interval", "", 1)):
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        data = old_data[msg.guild.id]
        if msg.author.id not in data["mng"]:return
        def check(m):return m.channel == message.channel and m.author == message.author
        while True:
            await message.channel.send("""Choose the reset interval:

1 - Once a day
2 - Never *(Custom Reset, Recommended)*

Enter the value:""")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                elif msg_.content not in ["1", "2"]:
                    await message.channel.send(warning+" Incorrect Value!")
                    await asyncio.sleep(1)
                else:value = msg_.content;break
        old_data[msg.guild.id]["tm"] = int(value)
        with open("Data/sweep.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone+" Changed sweep's reset interval!")
    elif (await gb_command_check(msg, "sweep", "", dual = True)):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        if client.cptpause:await emb_send(chl, client.cptnotice);return
        with open("Data/sweep.bt", "rb") as file:
            old_data = pickle.load(file)
        main_data = old_data.copy()
            
        if not (user_name := (await get_author_command(msg, "sweep", True)))["cn"] and not user_name["is_clan"]:
            await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
            
        if not user_name["is_clan"]:
            try:
                user_name = client.scache[user_name["cn"].lower()]["player_clan"]
            except:
                data = await get_user_data(user_name["cn"], "profile")
                user_name = data[3]["player_clan"]
        else:
            user_name = user_name["cn"]
        kr_user = user_name
        old_data = {data["cn"].lower():data  for id_, data in old_data.items()}
        sweep_id = {data["cn"].lower():id_ for id_, data in main_data.items()}
        try:
            
            s_data = old_data[kr_user.lower()]
            if msg.author.id in s_data["mng"]:pass
            elif s_data["p"] == "1" and msg.author.id not in s_data["mng"]:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Sweeps are private", description = "Contact clan owner or sweeps manager to view the sweeps."));return
            elif s_data["p"] == "2" and msg.author.id not in s_data["mng"]:
                if not (user_name := get_author_list(msg)):
                    await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Sweeps are private", description = "Contact clan owner or sweeps manager to view the sweeps."));return
                else:
                    data = await get_user_data(kr_user, "clan")
                    clan_members = {e_map["p"].lower():[e_map["s"], e_map["p"]] for e_map in data[3]["members"]}
                    found = False
                    for e_user in user_name:
                        if e_user.lower() in list(clan_members.keys()):
                            found = True
                    if not found:
                        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Sweeps are private", description = "Contact clan owner or sweeps manager to view the sweeps."));return
            elif s_data["p"] == "3":
                pass
                
        except Exception as e:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Clan not registered", description = "To have sweeps enabled for your clan, contact the bot developer,"));return
        try:
            found
        except:
            data = await get_user_data(kr_user, "clan")
            clan_members = {e_map["p"].lower():[e_map["s"], e_map["p"]] for e_map in data[3]["members"]}
        to_find_clan_members = {e_map["p"].lower():e_map for e_map in data[3]["members"]}

        old_data = s_data["data"]

        old_clan_members = {e_map["p"].lower():[e_map["s"], e_map["p"]] for e_map in old_data["members"]}
        scores = {}
        update_data = False
        for e_p in clan_members.keys():
            if e_p not in old_clan_members.keys():
                main_data[sweep_id[kr_user.lower()]]["data"]["members"].append(to_find_clan_members[e_p])
                update_data = True
        if update_data:
            with open("Data/sweep.bt", "wb") as file:
                pickle.dump(main_data, file)
        for e_p in old_clan_members.keys():
            try:clan_members[e_p]
            except:continue
            try:
                old_score = old_clan_members[e_p][0]
                user_p = old_clan_members[e_p][1]
            except:
                old_score = clan_members[e_p][0]
                user_p = clan_members[e_p][1]
            try:
                scores[user_p] = clan_members[e_p][0] - old_score
            except:pass

        total_maps = sorted(list(scores.items()), key = lambda x:x[1], reverse = True)
        def check(reaction, user_, msg, ask):
            return user_ == msg.author and (str(reaction.emoji) == next_page or str(reaction.emoji) == stop or str(reaction.emoji) == prev_page) and reaction.message.id == ask.id
        entries_count = 15
        try:maps = total_maps[:entries_count];has_pages = True
        except:has_pages = False
        main_pages = math.ceil(len(total_maps)/entries_count)
        current_page = 1
        start = 0
        started = False
        def get_spaces(text, max_l = 30):
            return text + str(" " * (max_l - len(text)))
        sweep_template = "**{}**\n`+ {}`\n"
        while True:
            try:
                if started:reaction, _ = await client.wait_for('reaction_add', check = lambda r, u: check(r, u, msg, ask), timeout=100)
            except asyncio.TimeoutError:await ask.clear_reactions();return
            else:
                if started:
                    if str(reaction.emoji) == stop:
                        await ask.clear_reactions();break
                    elif str(reaction.emoji) == next_page:
                        await ask.remove_reaction(next_page, msg.author)
                        if current_page == main_pages:
                            continue;
                        start += entries_count
                        try:maps = total_maps[start:start+entries_count]
                        except:maps = total_maps[start:]
                        current_page += 1
                    elif str(reaction.emoji) == prev_page:
                        await ask.remove_reaction(prev_page, msg.author)
                        if current_page == 1:
                            continue;
                        start -= entries_count
                        try:maps = total_maps[start:start+entries_count]
                        except:maps = total_maps[start:]
                        current_page -= 1
                desc = "The new scores since last time the sweeps were resetted.\n\n"
                
                for e_p, e_s in maps:
                    desc += "**`" + get_spaces(e_p+"`**`") + " + " + convert_int(e_s) + "`\n"

                embed = discord.Embed(colour=discord.Colour(14423783),
                                      title="Sweeps for "+kr_user.upper(),
                                      description = desc)
                embed.set_footer(text="To view the overall stats, use g.sweeper overall\nPage # {} of {}".format(current_page, main_pages))
                if not started:ask = await message.channel.send(embed = embed)
                else:
                    await ask.edit(embed = embed)
                if not has_pages or main_pages == 1:break
                started = True
                await ask.add_reaction(prev_page)
                await ask.add_reaction(stop)
                await ask.add_reaction(next_page)
                
    elif (await gb_command_check(msg, "link_count", "")) and msg.author.id in staff:
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        await message.channel.send("{} number of accounts have been linked".format(len(old_data)))
    elif (await gb_command_check(msg, "is_linked")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        try:
            kr_user = int(gb_command_fix(msg, "is_linked"))
        except:
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Expected User Id (Integer), found non-integers"));return
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        old_data = {v:k for k, v in old_data.items()}
        try:
            if (await get_u_(kr_user)).id not in get_var("incognito"):
                await msg.channel.send("{} is linked with `{}`".format(str(await get_u_(kr_user)), old_data[kr_user]))
            else:
                await msg.channel.send("{} is linked.".format(str(await get_u_(kr_user))))
        except:
            await msg.channel.send(str(await get_u_(kr_user)) + " is not linked")
    elif (await gb_command_check(msg, "is_clan_linked")):
        client.loop.create_task( do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        kr_user = gb_command_fix(msg, "is_clan_linked")
        data = await get_user_data(kr_user, "clan")
        clan_members = [e_map["p"].lower() for e_map in data[3]["members"]]
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        linked_tem = "`{}` is not linked!\n"
        output = ""
        for e_mem in clan_members:
            try:
                old_data[e_mem]
            except:
                output += linked_tem.format(e_mem)
        if output:
            if len(output) > 1990:
                output = output[:1990] + "...."    
            await msg.channel.send(output)
        else:await msg.channel.send("All clan members are linked")

        
    elif (await gb_command_check(msg, "link")) and msg.author.id in staff:
        try:
            map_name = gb_command_fix(msg, "link")
            map_name = map_name.split(" ", 1)
            if len(map_name) == 1:
                await msg.channel.send(warning + " Invalid command usage. Correct usage: `g.link <id/mention> <kr-username>`  *Only for staff*");return
            try:
                user = msg.mentions[0].id
                user_m = msg.mentions[0].mention
                user_obj = msg.mentions[0]
            except:
                try:
                    user = int(map_name[0])
                    user_obj = await get_u_(user)
                    if user_obj == None:
                        await msg.channel.send(warning + " The user you are trying to link doesn't share any server with the bot.");return
                    user_m = user_obj.mention
                except Exception as e:
                    print(e)
                    await msg.channel.send(warning + " Invalid command usage. Correct usage: `g.link <id/mention> <kr-username>`  *Only for staff*")
                    return
            kr_user = map_name[-1]
            send_dm = False
            if kr_user.lower().endswith(" -d"):
                kr_user = kr_user[:-len(" -d")]
                send_dm = True
            with open("Data/linked.bt", "rb") as file:
                old_data = pickle.load(file)
            try:
                old_data[kr_user.lower()]
                ask = await msg.channel.send("This username `{}` is already linked with `{}`\nDo you wish to overwrite?".format(kr_user, str(await get_u_(old_data[kr_user.lower()]))))
                await ask.add_reaction(check_mark)
                await ask.add_reaction(stop)
                
                def check(reaction, user_, msg, ask):
                    return user_ == msg.author and (str(reaction.emoji) == check_mark or str(reaction.emoji) == stop) and reaction.message.id == ask.id
                try:
                    reaction, _ = await client.wait_for('reaction_add', timeout=60.0, check= lambda r, u: check(r, u, msg, ask))
                except asyncio.TimeoutError:
                    await emb_send(message.channel, warning + " Received no output");return
                    return
                else:
                    if str(reaction.emoji) == check_mark:
                        old_data[kr_user.lower()] = user
                        with open("Data/linked.bt", "wb") as file:
                            pickle.dump(old_data, file)
                        await emb_send(message.channel, taskdone+" User linked successfully...")
                    else:
                        await emb_send(message.channel, warning + " Overwrite failed");return
            except:
                old_data[kr_user.lower()] = user
                with open("Data/linked.bt", "wb") as file:
                    pickle.dump(old_data, file)
                await emb_send(message.channel, taskdone+" User linked successfully...")
            embed=discord.Embed(colour=discord.Colour(14423783),
                                    description = msg.author.mention + " linked "+ user_m + " with `" + kr_user + "`")
            await client.get_guild(708067789830750449).get_channel(745692242584535090).send(embed = embed)
            if send_dm:
                await user_obj.send(taskdone+" Your profile has been linked.")
        except Exception as e:
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "unlink")) and msg.author.id in staff:
        try:
            map_name = gb_command_fix(msg, "unlink")
            with open("Data/linked.bt", "rb") as file:
                old_data = pickle.load(file)
            try:
                del old_data[map_name.lower()]
            except:
                await message.channel.send("ERROR!! User not linked")
                return
            with open("Data/linked.bt", "wb") as file:
                pickle.dump(old_data, file)
            await message.channel.send("User unlinked successfully...")
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title = str(e)))
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "unlink")):
        try:
            map_name = gb_command_fix(msg, "unlink")
            with open("Data/linked.bt", "rb") as file:
                old_data = pickle.load(file)
            alts = get_author_list(msg)
            if map_name.lower() in alts:
                ask = await msg.channel.send(msg.author.mention+f" Are you sure you want to unlink `{map_name}`??")
                await ask.add_reaction(warning)
                await ask.add_reaction(taskdone)
                
                def check(reaction, user_, msg, ask):return user_ == msg.author and (str(reaction.emoji) == taskdone or str(reaction.emoji) == warning) and reaction.message.id == ask.id
                try:
                    reaction, _ = await client.wait_for('reaction_add', timeout=30, check= lambda r, u: check(r, u, msg, ask))
                except asyncio.TimeoutError:
                    await emb_send(message.channel, warning + msg.author.mention + " You took to long to respond :/", footer_t = "Please try again!");return
                else:
                    if str(reaction.emoji) == taskdone:
                        del old_data[map_name.lower()]
                    else:
                        await ask.clear_reactions();return
            else:
                await emb_send(chl, warning+ """ Couldn't unlink this account. Heres why:

```css
- It doesn't belong to you
- It isn't linked```""",
                               footer_t = "For more help, please contact staff using 'g.staff'");return
            await emb_send(chl, taskdone+" " + msg.author.mention +f" You have been successfully unlinked from `{map_name}`")
            embed=discord.Embed(colour=discord.Colour.blue(),
                                    description = msg.author.mention + " got unlinked from `"+ map_name + "`")
            await client.get_guild(708067789830750449).get_channel(745692242584535090).send(embed = embed)
            with open("Data/linked.bt", "wb") as file:
                pickle.dump(old_data, file)
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title = str(e)))
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "link")):
        got_tk = await get_tk(msg, "You are already trying to link your profile.")
        if got_tk:return
        tk(msg, 1);
        client.loop.create_task(do_on_message(msg, -1))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":
            await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"))
            tk(msg);return
        if client.cptpause:await emb_send(chl, client.cptnotice);tk(msg);return
        try:
            kr_user = gb_command_fix(msg, "link")
            if kr_user.lower() in blacklisted_linking:
                await emb_send(chl, warning+" This account can't be linked.");tk(msg);return
            if msg.author.id in linkers:
                await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" You've already used your chance to get your account linked"));return
                
            elif msg.mentions:await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+" Incorrect command usage! Found a mention in your link request."));return
            with open("Data/linked.bt", "rb") as file:
                old_data = pickle.load(file)
            try:
                old_data[kr_user.lower()]
                if (await get_u_(old_data[kr_user.lower()])) == msg.author:
                    await emb_send(chl, taskdone+" You are already linked m8. Chill");tk(msg);return
                elif (await get_u_(old_data[kr_user.lower()])).id not in get_var("incognito"):
                    await emb_send(chl, "This username `{}` is already linked".format(kr_user)+
                               " with `{}`\nIf its yours, please reach out to a staff member.".format(str(await get_u_(old_data[kr_user.lower()]))), footer_t = "Use command g.staff")
                    tk(msg);return
                else:
                    await emb_send(chl, "This username `{}` is already linked".format(kr_user), footer_t = "Use command g.staff for more info")
                    tk(msg);return
                                   
            except:
                mdata = await get_user_data(unquote(unquote(kr_user)), pf__ = 1)
                try:
                    userLevel = max(1, math.floor(0.03 * math.sqrt(mdata[3]["player_score"]))) <= 10
                    userLevel2 = max(1, math.floor(0.03 * math.sqrt(mdata[3]["player_score"]))) <= 5
                except:
                    await emb_send(chl, warning+" The profile you are trying to link doesn't exist",
                                    footer_t = "Please try again");tk(msg);return
                linking_methods = emote_one+" - Linking by **changing flag**\n"
                if not userLevel2:
                    linking_methods += emote_two +" - Linking by **publishing a map**\n"
                else:
                    linking_methods += emote_two +" ~~- Linking by **publishing a map**~~\n"
                if not userLevel:
                    linking_methods += emote_three +" - Linking by **posting on social hub**\n"
                else:
                    linking_methods += emote_three +" ~~- Linking by **posting on social hub**~~\n"
                linking_methods += warning + " - Cancel this operation"
                ask = await emb_send(chl, linking_methods, title_ = "Choose a linking method:")
                publish_map = 0
                final_msg = ""
                linking_by_flag = 0
                await ask.add_reaction(emote_one)
                if not userLevel2:
                    await ask.add_reaction(emote_two)
                if not userLevel:
                    await ask.add_reaction(emote_three)
                await ask.add_reaction(warning)
                def check(reaction, user_, msg, ask):
                    return user_.id == msg.author.id and str(reaction.emoji) in [warning, emote_one, emote_two, emote_three] and reaction.message.id == ask.id
                try:
                    reaction, _ = await client.wait_for('reaction_add', timeout=60*7, check= lambda r, u: check(r, u, msg, ask))
                except asyncio.TimeoutError as e:
                    try:await ask.clear_reactions()
                    except:pass
                    tk(msg);
                    return
                else:
                    if str(reaction.emoji) == emote_one:
                        linking_by_flag = 1
                        try:
                            flg = json.loads(mdata[3]['player_stats'])["flg"]
                        except:flg = -1
                        expected_flg = random.choice(Countries_names)
                        desc_text = """**Change your profile's country flag** to verify the account is yours.
```diff
- Log into krunker with your account
- Go to your profile settings
+ Change your country flag to '{}'
+ Enter the game and kill a few enemies
- Once done, react below.
```""".format(expected_flg[0])
                        sleep_time = 30
                        img_url = ""
                    elif str(reaction.emoji) == emote_two:
                        if userLevel2:
                            await emb_send(chl, warning+ " Whoops. Thats not a valid method for you to get linked.");
                            tk(msg);return
                        publish_map = 1
                        random.choice(string.ascii_letters)
                        expected_name_ = "gb-" + "".join([random.choice(string.ascii_letters + string.digits) for _ in range(9)])
                        sample_map = '{"name":"'+expected_name_+'","objects":[{"p":[0,0,0],"s":[0,0,0]}],"spawns":[[0,0,0]]}'
                        desc_text = """**Publish the following map** on [Krunker Hub](https://krunker.io/social.html?p=maps&openPub) to verify the account is yours.
```diff
- Visit Krunker social hub. 'https://krunker.io/social.html?p=maps&openPub'
+ Post this code -> {}
- Once done, react below.
```""".format(sample_map)
                        sleep_time = 5
                        final_msg = "\nYou can now delete this published map in My Games tab on [Krunker Social](https://krunker.io/social.html?p=maps)"
                        img_url = "https://media.discordapp.net/attachments/723242840980979792/806837007967846450/howtopublish.png"

                    elif str(reaction.emoji) == emote_three:
                        if userLevel:
                            await emb_send(chl, warning+ " Whoops. Thats not a valid method for you to get linked.");
                            tk(msg);return
                        keyCODE = "gb-" + "".join([random.choice(string.ascii_letters + string.digits) for _ in range(12)])
                        desc_text = """**Post text shown below** on Krunker Hub to verify the account is yours.
```diff
- Visit Krunker social hub. 'krunker.io/social.html'
+ Post this code ->   {}
- Once done, react below.
```""".format(keyCODE)
                        sleep_time = 7
                        img_url = "https://media.discordapp.net/attachments/708700075517280336/767340133007360010/howtopost.png"
                    else:
                        print(str(reaction.emoji))
                        try:await ask.clear_reactions()
                        except:pass
                        await emb_send(message.channel, warning + " Verification Failed!");tk(msg);return
                    try:await ask.clear_reactions()
                    except:pass
                    tk(msg);
                inst = ask
                await emb_edit(ask, desc_text,
                                      title_ = "Almost there...",
                                      footer_t = "You have 7 mins to verify your account.", image_url = img_url)
                await inst.add_reaction(taskdone)
                await inst.add_reaction(warning)
                def check(reaction, user_, msg_auth_id, ask):
                    if reaction.message.id == ask.id:
                        print(str(reaction.emoji) in [taskdone, warning], user_ == msg_auth_id, user_, msg_auth_id)
                    return user_ == msg_auth_id and str(reaction.emoji) in [taskdone, warning] and reaction.message.id == ask.id
                msg_auth_id = message.author
                try:
                    reaction, _ = await client.wait_for('reaction_add', timeout=60*7, check= lambda r, u: check(r, u, msg_auth_id, inst))
                except asyncio.TimeoutError as e:
                    try:await inst.clear_reactions()
                    except:pass
                    try:await req.delete()
                    except:pass
                    tk(msg);
                else:
                    if str(reaction.emoji) == taskdone:
                        try:await inst.clear_reaction(warning)
                        except:pass
                        req = await emb_send(
                            chl,
                            loading+" Your request has been added in the queue.",
                            footer_t = "Please close the krunker tab and wait for some time")
                        await asyncio.sleep(sleep_time)
                        if linking_by_flag and not publish_map:
                            mdata = await get_user_data(unquote(unquote(kr_user)), pf__ = 1)
                            try:
                                new_flg = json.loads(mdata[3]['player_stats'])["flg"]
                            except:new_flg = 0
                            if new_flg != expected_flg[2]:
                                await req.delete()
                                await emb_send(message.channel, warning+" "+msg.author.mention+" This profile doesn't belong to you.",
                                               footer_t = "It does? Try it again. Make sure you kill few enemies and play the game before leaving.")
                                tk(msg);return
                        elif not publish_map:
                            data = await get_user_posts(mdata[3]["player_id"])
                            data = data[1]
                            is_him = False
                            for e_post in data:
                                if e_post["txt"].strip() == keyCODE:
                                    is_him = True
                            if not is_him:
                                await req.delete()
                                await emb_send(message.channel, warning+" "+msg.author.mention+" This profile doesn't belong to you.",
                                               footer_t = "It does? Try it again. Make sure you posted the code correctly.")
                                tk(msg);return
                        else:
                            mdata = await get_user_data(unquote(unquote(kr_user)), pf__ = 1)
                            all_maps = mdata[4]
                            maps = [e_m["map_name"] for e_m in all_maps]
                            if expected_name_ not in maps:
                                await req.delete()
                                await emb_send(message.channel, warning+" "+msg.author.mention+" This profile doesn't belong to you.",
                                               footer_t = "It does? Try it again. Make sure you kill few enemies and play the game before leaving.")
                                tk(msg);return
                            
                        with open("Data/linked.bt", "rb") as file:
                            old_data = pickle.load(file)
                        old_data[kr_user.lower()] = msg.author.id
                        with open("Data/linked.bt", "wb") as file:
                            pickle.dump(old_data, file)
                        await emb_send(message.channel,
                                       taskdone+" " + msg.author.mention + " You are successfully linked with `{}`{}".format(kr_user, final_msg),
                                       footer_t = "Join Gamebot Hub. Use g.server")
                        embed=discord.Embed(colour=discord.Colour.gold(),
                                    description = msg.author.mention + " got linked with `"+ kr_user + "`")
                        await client.get_guild(708067789830750449).get_channel(745692242584535090).send(embed = embed)
                        tk(msg);

                    else:
                        try:await inst.clear_reaction(taskdone)
                        except:pass
                        try:await req.delete()
                        except:pass
                        await emb_send(message.channel, warning + " Verification Failed!");tk(msg);return
                    await req.delete()
            tk(msg);
        except Exception as e:
            tk(msg);
            try:await message.channel.send(embed=discord.Embed(title = str(e)))
            except:await msg.author.send("Bot is missing some permissions in the channel you used a command. Please contact server admin or staff members for support")
            if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
            raise e
    elif (await gb_command_check(msg, "alts", "", dual = True)) and msg.content.lower() != "g.alts set":
        client.loop.create_task(do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        alts = []
        if len(msg.mentions) == 0 and msg.content.lower() != "g.alts":
            output = gb_command_fix(msg, "alts")
            if output.isdigit() and len(output) == 18:
                alts = get_author_list(msg, int(output), True)
                mentioned_one = await get_um(int(output))
        elif msg.mentions:
            alts = get_author_list(msg, msg.mentions[0].id, True)
            mentioned_one = msg.mentions[0].mention
        else:
            alts = get_author_list(msg)
            mentioned_one = msg.author.mention
        if msg.content.lower().startswith("g.alts set"):
            await emb_send(chl, warning + " Incorrect commands usage. No argument is required. Simply use `g.alts set` without anything.")
            return
        if not alts:await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
        if len(alts) >= 2:
            alts[-1] += "  <<< Main account"
        desc = ""
        for x, e_acc in enumerate(alts, 1):
            desc += "\n{}. {}".format(x, e_acc)
        await emb_send(msg.channel,
                       "**Linked accounts for** "+mentioned_one+"\n```css\n"+desc + "```""",
                       footer_t = "Change your main account using `g.alts set'")
        
    elif (await gb_command_check(msg, "alts set", "", 1)):
        client.loop.create_task(do_on_message(msg))
        coold_check = await cool_down_check(message)
        if coold_check == "Error":await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = warning+ " Using commands too fast.", description = "Please try again in a few seconds"));return
        alts = get_author_list(msg)
        if not alts:
            await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");return
        desc = ""
        for x, e_acc in enumerate(alts, 1):
            desc += "\n{}. {}".format(x, e_acc)
        emb_a = await emb_send(msg.channel,
                       "**Linked accounts for** "+msg.author.mention+"\n```css\n"+desc + "```\n\n__Enter the **index** of your alt you want to select:__"
        )
        def check(m):return m.channel == message.channel and m.author == message.author
        try:msg_ = await client.wait_for('message', check=check, timeout=100)
        except asyncio.TimeoutError:return
        else:
            if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
            try:new_in = int(msg_.content)-1
            except:
                await emb_a.add_reaction(stop);return
        with open("Data/linked.bt", "rb") as file:
            old_data = pickle.load(file)
        del old_data[alts[new_in]]
        old_data[alts[new_in]] = msg.author.id
        with open("Data/linked.bt", "wb") as file:
            pickle.dump(old_data, file)
        await emb_send(msg.channel, taskdone + " Successfully changed your main account to `{}`".format(alts[new_in]))
    elif (await gb_command_check(msg, "manage_servers", "")) and message.author.id in staff:
        fetching = await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = loading+ " Managing Servers. This may take a while"))        
        await UpdateRolesNicks()
        await message.channel.send(embed=discord.Embed(colour=discord.Colour(14423783), title = taskdone+ " Managed all Servers!"))
        await fetching.delete()
    elif (await gb_command_check(msg, "applications", "", 1)) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        data = get_data()
        try:
            stats = data["apl"][msg.guild.id]
            try:stats["acc"]
            except:stats["acc"] = 0
        except:
            stats = {"lvl":0, "kdr": 0, "spk": 0, "kpg":0, "n":0, "acc": 0, "chl":0}
        type_keys = {"lvl": "Level", "kdr": "KDR", "spk": "SPK", "kpg": "KPG", "n":"Nukes", "chl":"Channel", "acc":"Accuracy"}
        def _get_type(msg, tp, val):
            if tp != "chl":
                if val:return str(val) + ("%" if tp =="acc" else "")
                else:return "Any" + ("%" if tp =="acc" else "")
            else:
                try: return "#"+msg.guild.get_channel(val).name
                except:return "#Any"
        def get_desc(stat):
            desc = "```css\n"
            for x, (stat_n, type_) in enumerate(stat.items(), 1):
                desc += "{}. {}: {}\n".format(x, type_keys[stat_n], _get_type(msg, stat_n, type_))
            return desc + "```\n\n*Use `select <index>` to edit a stat's value.*"
        def auto_del(mm, m, tm = 6):
            client.loop.create_task(c_auto_del(mm, m, tm))
        async def c_auto_del(mm, m, tm = 6):
            await asyncio.sleep(tm)
            try:
                await m.delete()
            except:pass
            await asyncio.sleep(1.5)
            try:await mm.delete()
            except:pass
        def check(m):return m.channel == message.channel and m.author == message.author and (m.content.lower() == "cancel" or m.content.lower() == "save" or m.content.lower().startswith("select ")  or m.content.lower().startswith("set "))
        to_be_edited = await emb_send(chl, get_desc(stats), title_ = "Current Application Configurations")
        while True:
            try:msg_ = await client.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:await to_be_edited.add_reaction(warning);return
            else:
                if msg_.content.lower() == "cancel":await emb_edit(to_be_edited, warning+" Application Configurations Cancelled!");return
                elif msg_.content.lower() == "save":
                    data["apl"][msg.guild.id] = stats
                    rewrite_data(data)
                    await emb_send(chl, taskdone+ " Saved your clan's minimal stats")
                    return
                elif msg_.content.lower().startswith("select "):
                    try:
                        selected = list(stats.items())[int(msg_.content.lower().replace("select ", ""))-1]
                        await emb_edit(to_be_edited,
                                       get_desc(stats),
                                       title_ = "Current Application Configurations",
                                       footer_t = "Currently selected '{}'\nUse 'set <val>' to set a new minimum value".format(type_keys[selected[0]]))

                        to_be_del = await emb_send(chl, taskdone+" Selected `"+type_keys[selected[0]]+"`", footer_t = "Now use 'set <val>'")
                        auto_del(msg, to_be_del)
                    except:
                        to_be_del = await emb_send(chl, warning+" Please enter a valid index")
                        auto_del(msg, to_be_del)
                elif msg_.content.lower().startswith("set "):
                    try:
                        if msg_.channel_mentions and selected[0] == "chl":
                            changed_to = msg_.channel_mentions[0].id
                            stats[selected[0]] = changed_to
                        else:
                            changed_to = float(msg_.content.lower().replace("set ", ""))
                            stats[selected[0]] = changed_to
                        await emb_edit(to_be_edited,
                                       get_desc(stats),
                                       title_ = "Current Application Configurations")
                        to_be_del = await emb_send(chl,
                                                   taskdone+" Changed {}'s value to {}".format(type_keys[selected[0]],
                                                                                               changed_to),
                                                   footer_t = "Once done, use 'save'")
                        auto_del(msg, to_be_del)
                    except Exception as e:
                        print(e)
                        to_be_del = await emb_send(chl, warning+" Please Enter a valid Value\n\n*if you did,*   Please select a stat first.\nUse `select <index>`")
                        auto_del(msg, to_be_del)
    elif ((await gb_command_check(msg, "del_pbg")) or (await gb_command_check(msg, "del_cbg"))) and msg.author.id in admins:
        if msg.content.lower().startswith("g.del_pbg"):
            name = gb_command_fix(msg, "del_pbg")
            is_clan = 0
        if msg.content.lower().startswith("g.del_cbg"):
            name = gb_command_fix(msg, "del_cbg")
            is_clan = 1
        old_data = await async_open("Data/backgrounds.bt")
        if is_clan:data = old_data["c"]
        else:data = old_data["p"]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            data["owners"]
        except:
            await emb_send(chl, warning+" No such background!");return
        del old_data["c" if is_clan else "p"][ind]
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(chl, taskdone+" Deleted the background")
        await compile_bgs()
        await client.get_guild(708067789830750449).get_channel(756471541281325146).send("`Deleted background: {}` - `Deleted by` -> {}".format(name, msg.author))
    elif (await gb_command_check(msg, "bglist", "")):
        client.loop.create_task(do_on_message(msg))
        old_data = await async_open("Data/backgrounds.bt")
        owner = message.author.id
        mentioned_one = message.author.mention
        backgrounds = []
        bgts = {"c": " - Clan", "p": " - Personal"}
        desc = "Backrounds for: {}\n\n".format(mentioned_one)
        for bgt in ["c", "p"]:
            for e_bg in old_data[bgt]:
                if owner in [int(e_o) for e_o in e_bg["owners"]]:
                    backgrounds.append([e_bg["cm"], [bgt]])
                    desc += "`" + e_bg["cm"].ljust(40)+bgts[bgt] + "`\n"
        if not backgrounds:
            desc += "None"
        await emb_send(chl, desc)
    elif (await gb_command_check(msg, "find_bgo")) and msg.author.id in staff:
        old_data = await async_open("Data/backgrounds.bt")
        if len(msg.mentions) == 0:
            output = gb_command_fix(msg, "find_bgo")
            if output.isdigit() and len(output) == 18:
                owner = await get_u_(int(output))
                mentioned_one = owner.mention
                owner = owner.id
            else:
                await emb_send(chl, warning + " Incorrect usage. Use user's id or mention");return
        else:
            owner = msg.mentions[0].id
            mentioned_one = msg.mentions[0].mention
        backgrounds = []
        bgts = {"c": " - Clan", "p": " - Personal"}
        desc = "Backrounds for: {}\n\n".format(mentioned_one)
        for bgt in ["c", "p"]:
            for e_bg in old_data[bgt]:
                if owner in [int(e_o) for e_o in e_bg["owners"]]:
                    backgrounds.append([e_bg["cm"], [bgt]])
                    desc += "`" + e_bg["cm"].ljust(40)+bgts[bgt] + "`\n"
        if not backgrounds:
            desc += "None"
        await emb_send(chl, desc)
    elif ((await gb_command_check(msg, "def_pbg")) or (await gb_command_check(msg, "def_cbg"))) and msg.author.id in staff:
        if msg.content.lower().startswith("g.def_pbg"):
            name = gb_command_fix(msg, "def_pbg")
            is_clan = 0
        if msg.content.lower().startswith("g.def_cbg"):
            name = gb_command_fix(msg, "def_cbg")
            is_clan = 1
        with open("Data/backgrounds.bt", "rb") as file:
            old_data = pickle.load(file)
        if is_clan:data = old_data["c"]
        else:data = old_data["p"]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            client.default_bg[0].save("Data/backgrounds/"+data["file"])
        except:
            await emb_send(chl, warning+" No such background!");return
        await compile_bgs()
        await msg.add_reaction(taskdone)
        await client.get_guild(708067789830750449).get_channel(756471541281325146).send("`Reseted background: {}` - `Rested by` -> {}".format(name, msg.author))
    elif ((await gb_command_check(msg, "prem_pbg")) or (await gb_command_check(msg, "prem_cbg"))) and msg.author.id in admins:
        if msg.content.lower().startswith("g.prem_pbg"):
            name = gb_command_fix(msg, "prem_pbg")
            is_clan = 0
        if msg.content.lower().startswith("g.prem_cbg"):
            name = gb_command_fix(msg, "prem_cbg")
            is_clan = 1
        old_data = await async_open("Data/backgrounds.bt")
        if is_clan:data = old_data["c"]
        else:data = old_data["p"]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            if msg.author.id not in data["owners"]:
                await emb_send(chl, warning+" You are not background owner.\n\nPlease contact:\n"+ "\n".join([(await get_um(user)) for user in data["owners"]]))
        except:
            await emb_send(chl, warning+" No such background!");return
        try:old_data["c" if is_clan else "p"][ind]["prem"]
        except:old_data["c" if is_clan else "p"][ind]["prem"] = 0
        
        if not old_data["c" if is_clan else "p"][ind]["prem"]:
            old_data["c" if is_clan else "p"][ind]["prem"] = 1
        else:
            old_data["c" if is_clan else "p"][ind]["prem"] = 0
        prem_n = {1:"Premium",
                  0:"Classic"}
        
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await emb_send(chl, taskdone+" Changed the background's subscription to {}".format(prem_n[old_data["c" if is_clan else "p"][ind]["prem"]]))
        await compile_bgs()
        await client.get_guild(708067789830750449).get_channel(756471541281325146).send("`Changed subscription of {}` - `Edited by` -> {}".format(name, msg.author))
    elif ((await gb_command_check(msg, "cbgo")) or (await gb_command_check(msg, "pbgo"))) and msg.author.id in staff:
        if msg.content.lower().startswith("g.p"):
            name = gb_command_fix(msg, "cbgo")
            is_clan = 0
        if msg.content.lower().startswith("g.c"):
            name = gb_command_fix(msg, "cbgo")
            is_clan = 1
        old_data = await async_open("Data/backgrounds.bt")
        if is_clan:data = old_data["c"]
        else:data = old_data["p"]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            await emb_send(chl, taskdone+" Background owners:\n"+ "\n".join([(await get_um(int(user))) for user in data["owners"]]))
        except:
            await emb_send(chl, warning + " Something went wrong. Maybe this background doesn't exist")
    elif ((await gb_command_check(msg, "cba")) or (await gb_command_check(msg, "pba")) or (await gb_command_check(msg, "cbr")) or (await gb_command_check(msg, "pbr"))) and msg.author.id in admins:
        uid, name = gb_command_fix(msg, "cba").split(" ", 1)
        btype = msg.content.lower()[2]
        old_data = await async_open("Data/backgrounds.bt")
        data = old_data[btype]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            if msg.content.lower()[4] == "a":
                data["owners"] += [int(uid)]
            else:
                data["owners"].remove(int(uid))
        except:
            await emb_send(chl, warning + " No such background | Incorrect user id");return
        old_data = await async_open("Data/backgrounds.bt")
        for ind, e_p in enumerate(old_data[btype]):
            if e_p["cm"].lower() == name.lower():
                old_data[btype][ind] = data
                break
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await msg.add_reaction(taskdone)

    elif (await gb_command_check(msg, "cblay") or await gb_command_check(msg, "pblay")) and msg.author.id in staff:
        name = gb_command_fix(msg, "cblay")
        btype = msg.content.lower()[2]
        old_data = await async_open("Data/backgrounds.bt")
        data = old_data[btype]
        for ind, e_p in enumerate(data):
            if e_p["cm"].lower() == name.lower():
                data = e_p
                break
        try:
            data
            try:
                data["bglay"] = -1 if data["bglay"] != -1 else 0
            except:
                data["bglay"] = -1
        except:
            await emb_send(chl, warning + " No such background");return
        old_data = await async_open("Data/backgrounds.bt")
        for ind, e_p in enumerate(old_data[btype]):
            if e_p["cm"].lower() == name.lower():
                old_data[btype][ind] = data
                break
        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
        await msg.add_reaction(taskdone)
        await compile_bgs()
        
    elif (await gb_command_check(msg, "pbg", "", dual = True)) or (await gb_command_check(msg, "cbg", "", dual = True)):
        got_tk = await get_tk(msg)
        if got_tk:return
        tk(msg, 1);
        client.loop.create_task(do_on_message(msg, -1))
        try:
            if msg.content.lower().startswith("g.pbg"):
                if msg.content.lower() != "g.pbg":
                    name = gb_command_fix(msg, "pbg")
                elif not (name := (await get_author_command(msg, "pbg"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");tk(msg);return
                is_clan = 0
            if msg.content.lower().startswith("g.cbg"):
                if msg.content.lower() != "g.cbg":
                    name = gb_command_fix(msg, "cbg")
                elif not (name := (await get_author_command(msg, "cbg"))):
                    await emb_send(message.channel,title_ = warning + " You need to link your krunker username with discord account to use commands directly.",cnt = "Use `g.link <kr-username>` to link your account",footer_t = "You can still use commands without linking, its just an extra feature.");tk(msg);return
                else:
                    try:
                        name = client.scache[user_name.lower()]["player_clan"]
                    except Exception as e:
                        name = ""
                is_clan = 1
            old_data = await async_open("Data/backgrounds.bt")
            if is_clan:
                data = old_data["c"]
            else:
                data = old_data["p"]
            for ind, e_p in enumerate(data):
                if e_p["cm"].lower() == name.lower():
                    data = e_p
                    break
            try:
                if msg.author.id not in [int(uid) for uid in data["owners"]]+staff:
                    await emb_send(chl, warning+" You are not background owner.\n\nPlease contact:\n"+ "\n".join([(await get_um(user)) for user in data["owners"]]))
                    tk(msg)
                    return
            except:
                await emb_send(chl, warning+" No such background!", footer_t = "Use 'g.help background' to get one");tk(msg);return
            type_keys = {"file": "Image", "ut": "Username Color", "xp": "Xp Bar Color", "hd":"Heading color", "txt": "Background Motto",
                         "prem": "Subscription", "lgc": "GB Logo Color", "brd": "Layout & Outline",
                         "outl": " [Outlining]", "shd": "Outline Shadows", "clr": "Outline Color", "xpb": "Xp Bar Background"}
            prem_n = {0: "Classic",
                      1: "Premium",
                      -1: "Unknown"}
            def get_brd(stat, start_ = 8):
                nstat = stat.copy()["brd"]
                desc = "```css\n"
                for x, (stat_n, type_) in enumerate(nstat.items(), start_):
                    if stat_n in ["outl", "shd", "xpb"]:
                        otype_ = "On" if nstat[stat_n] else "Off"
                    elif stat_n == "clr":
                        otype_ = "White" if not nstat["clr"] else nstat["clr"]
                    else:
                        otype_ = type_
                    desc += "{}. {}: {}\n".format(x, type_keys[stat_n], otype_)
                return desc + """```
*Type `select 8` to toggle outline*
*Type `select 9` to toggle Outline Shadow*
*Type `select 10` to change Border Color*
*Type `select 11` to toggle Xp Bar*
__*Type `select 12` to switch back to main dashboard*__"""
            def get_desc(stat, start_ = 1):
                nstat = stat.copy()
                del nstat["owners"]
                del nstat["cm"]
                try:
                    nstat["txt"]
                except:nstat["txt"] = "None"
                del nstat["prem"]
                desc = "```css\n"
                for x, (stat_n, type_) in enumerate(nstat.items(), start_):
                    if stat_n == "prem":
                        otype_ = prem_n[type_]
                    elif stat_n == "txt":
                        otype_ = "None" if not nstat["txt"] else nstat["txt"]
                    elif stat_n == "lgc":
                        otype_ = "Defualt" if not nstat["lgc"] else nstat["lgc"]
                    elif stat_n == "brd":
                        otype_ = "On" if nstat["brd"]["outl"] else "Off"
                    else:
                        otype_ = type_
                    desc += "{}. {}: {}\n".format(x, type_keys[stat_n], otype_)
                return desc + """```
*Type `select 1` to change background*
*Type `select 2` to change Username color*
*Type `select 3` to change XP Bar color*
*Type `select 4` to change Heading color*
*Type `select 5` to change Background Text/Motto*
*Type `select 6` to change Gamebot Logo color*
*Type `select 7` to edit outlining settings*"""
            def check(m):return m.channel == message.channel and m.author == message.author
            def def_k(d, k, v):
                try:d[k]
                except:d[k] = v
            try:
                data["txt"] = data["text"]
            except:pass
            try:old_text = data["txt"]
            except:
                old_text = ""
                data["txt"] = ""
            try:data["prem"]
            except:data["prem"] = -1
            try:data["lgc"]
            except:data["lgc"] = 0
            try:dict(data["brd"])
            except:data["brd"] = {}
            try:del data["shd"]
            except:pass
            def_k(data, "bglay", 0)
            def_k(data["brd"], "outl", 0)
            def_k(data["brd"], "shd", 0)
            def_k(data["brd"], "clr", 0)
            def_k(data["brd"], "xpb", 1)
            data_list = ["file", "cm", "owners", "ut", "xp", "hd", "txt", "lgc", "brd", "prem"]
            data = dict([(k, data[k]) for k in data_list])
            img = Image.open("Data/backgrounds/"+data["file"])
            byte_io = BytesIO()
            byte_io.seek(0)
            img.save(byte_io, 'PNG')
            byte_io.seek(0)
            async def update_emb(oem, h = "Background Configurator for '"+name+"'", c = 1, function_ = get_desc):
                if c:oc=getIfromRGB(data["ut"])
                else:oc = 14423783
                await emb_edit(oem, function_(data),
                               emb_color = oc,
                               title_ = h, image_url = "attachment://image.png", file=discord.File(byte_io, "image.png"))
            to_be_edited = await emb_send(chl, get_desc(data),
                                          emb_color = getIfromRGB(data["ut"]),
                                          title_ = "Background Configurator", image_url = "attachment://image.png", file=discord.File(byte_io, "image.png"))
            is_main_conf = 1
            while True:
                try:msg_ = await client.wait_for('message', check=check, timeout=300)
                except asyncio.TimeoutError:tk(msg);await to_be_edited.add_reaction(warning);return
                if is_main_conf:
                    if msg_.content.lower() == "cancel":await emb_edit(to_be_edited, warning+" Background Configurations Cancelled!");tk(msg);return
                    elif msg_.content.lower() == "save":
                        old_data = await async_open("Data/backgrounds.bt")
                        for ind, e_p in enumerate(old_data["c" if is_clan else "p"]):
                            if e_p["cm"].lower() == name.lower():
                                old_data["c" if is_clan else "p"][ind] = data
                                break
                        with open("Data/backgrounds.bt", "wb") as file:pickle.dump(old_data, file)
                        await emb_send(chl, taskdone+ " Saved your background!")
                        await compile_bgs()
                        tk(msg)
                        try:
                            if old_text != data["txt"]:
                                
                                await client.get_guild(708067789830750449).get_channel(756471541281325146).send("Changed text of `{}` to `{}` from `{}` by {}".format(
                                    data["cm"], data["txt"], old_text, msg.author))
                        except:pass
                        return
                    elif msg_.content.lower() == "select 1":
                        while True:
                            await emb_send(chl, "Upload Background:", footer_t = "Make sure it doesn't alternate the stats or make them difficult to read in any way")
                            try:msg_ = await client.wait_for('message', check=check, timeout=150)
                            except asyncio.TimeoutError:await msg.add_reaction(warning);tk(msg);return
                            else:
                                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");tk(msg);return
                                try:
                                    if not msg_.attachments[0].size > 7000000:
                                        img = await msg_.attachments[0].read()
                                        img_name = msg_.attachments[0].filename
                                        img_ext = img_name.rsplit(".", 1)[-1].lower()
                                        frames = []
                                        if img_ext == "gif":
                                            subs = ""
                                            if data["prem"] == 0:subs = "Classic"
                                            elif data["prem"] == -1:subs = "Unknown"
                                            if subs:
                                                await emb_send(chl, warning+" Your background's subscription is `{}`.\n You can't choose animated background. Please upgrade your subscription by becoming a supporter on patreon or increasing your nitro boosts for Gamebot Hub Server".format(subs), footer_t = "For more help, contact staff using 'g.staff'");await asyncio.sleep(3);continue
                                        if img_ext not in ["png", "gif"]:
                                            await emb_send(msg.channel, warning + " Incorrect Image type. Must be PNG/GIF");tk(msg);return
                                        try:img = Image.open(BytesIO(img))
                                        except:await emb_send(msg.channel, warning + " Could not decode the image", footer_t = "Make sure you uploaded the correct image.");tk(msg);return
                                        if img.mode not in ["RGBA", "RGB", "P"]:
                                            await emb_send(msg.channel, warning + " Incorrect Image mode. Must be RGB/RGBA");tk(msg);return
                                        if img.width != 719 or img.height != 464:
                                            await emb_send(msg.channel, warning + " Incorrect dimensions. Must be `719 x 464`.\nException suppressed! Image may be stretched")
                                            if img_ext == "png":
                                                img = img.resize((719, 464))
                                            else:
                                                frames = ImageSequence.Iterator(img)
                                                def thumbnails(frames):
                                                    output_frames = []
                                                    for frame in frames:
                                                        thumbnail = frame.copy()
                                                        output_frames += [thumbnail.resize((719, 464))]
                                                    return output_frames
                                                frames = thumbnails(frames)
                                                img = img.resize((719, 464))
                                        r_o = "junk/"+''.join(random.choices(string.ascii_uppercase + string.digits, k=10))+"."+img_ext
                                        mdata = ['0', 'profile', 'Gamebot', {'player_name': 'Gamebot', 'player_id': 1487185, 'player_kills': 17580, 'player_wins': 995, 'player_games_played': 2635, 'player_deaths': 14733, 'player_timeplayed': 734217526, 'player_funds': 4222, 'player_score': 1987415, 'player_featured': 0, 'player_clan': 'VIP', 'player_hack': 0, 'player_following': 5, 'player_followed': 12, 'player_stats': '{"c":13,"s":219475,"h":35670,"mk":37,"c0":312255,"c1":66175,"c2":193990,"r3":360,"c3":225,"c8":7290,"c4":7380,"c5":625,"r2":143,"r4":34,"c6":225,"hs":2651,"chgP":"5:100,0,0","flg":-1,"wb":15,"c12":5760,"r1":5,"c11":2785,"c9":305,"anp":0,"tmk":11,"fk":1}', 'player_datenew': '2019-01-22T10:19:53.000Z', 'player_elo': 16, 'player_region': 3, 'player_type': 0, 'player_elo2': None, 'player_elo4': None, 'player_chal': 5, 'player_infected': 1, 'player_eventcount': None, 'player_premium': 0, 'partner_approved': 1, 'clan_rank': 37, 'player_alias': None, 'player_twitchname': None}, [1, 2, 3, 4, 5, 6, 7], [0, 1], None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6]]
                                        pfuser_name = "Gamebot"
                                        pfdata = mdata[3]
                                        stats = json.loads(pfdata['player_stats'])
                                        try:pfdata['player_chal'] += 1
                                        except:pfdata['player_chal'] = 0
                                        for e_elo in ["player_elo2", "player_elo4", "player_elo"]:
                                            try:
                                                if not pfdata[e_elo]:pfdata[e_elo] = 0
                                            except:pfdata[e_elo] = 0
                                        muser = await get_author_name(msg, pfuser_name, True)
                                        byte_io = BytesIO()
                                        byte_io.seek(0)
                                        img.save(byte_io, img_ext, save_all = True if img_ext == "gif" else False, append_images = frames)
                                        byte_io.seek(0)
                                        data["bg"] = Image.open(byte_io)
                                        thing = functools.partial(generate_pf, pfdata, stats, pfuser_name, 0, mdata, None, muser, data)
                                        with ThreadPoolExecutor(max_workers = 1) as executor:
                                            byte_io, img_format = await client.loop.run_in_executor(executor, thing)
                                        pfimg = Image.open(byte_io)
                                        pfframes = [frame.copy() for frame in ImageSequence.Iterator(pfimg)]
                                        pfimg.save(r_o, img_ext.upper(), save_all = True if img_ext == "gif" else False, append_images = pfframes[1:])
                                        del data["bg"]
                                        
                                        if os.stat(r_o).st_size > 7000000:
                                            os.remove(r_o)
                                            await emb_send(msg.channel, warning + " 7 mb is the max size. Please try again. ", footer_t = "*Final size is more than expected");
                                        else:
                                            os.remove(r_o)
                                            if data["file"].rsplit(".", 1)[-1].lower() == img_ext:
                                                img.save("Data/backgrounds/"+data["file"], save_all = True if img_ext == "gif" else False, append_images = frames, quality = 80, optimize = True)
                                                image_ind = data["file"]
                                            else:
                                                for ind in range(1, 1000):
                                                    if not os.path.exists("Data/backgrounds/tem{}".format(ind)+"."+img_ext):
                                                        img.save("Data/backgrounds/tem{}".format(ind)+"."+img_ext, format = img_ext.upper(), save_all = True if img_ext == "gif" else False, append_images = frames, quality = 80, optimize = True)
                                                        image_ind = "tem" + str(ind)+"."+img_ext
                                                        break
                                            
                                            await emb_send(chl, taskdone+ " Replaced your image. Don't forget to use `save` to bring it in full effect.")
                                            data["file"] = image_ind
                                            thumb = resizeimage.resize_thumbnail(img, [150, 150])
                                            byte_io = BytesIO();byte_io.seek(0)
                                            thumb.save(byte_io, 'PNG');byte_io.seek(0)
                                            await client.get_guild(708067789830750449).get_channel(756471541281325146).send("Changed **background** of {} - Changed by -> {}".format(data["cm"], msg.author), file=discord.File(byte_io, "image.png"))
                                            break
                                    else:
                                        await emb_send(msg.channel, warning + " 7 mb is the max size. Please try again from start...", footer_t = "Compressing image is not suggested");tk(msg);return
                                except Exception as e:
                                    await emb_send(msg.channel, warning + " Please attach image. Try again from start!");tk(msg);
                                    raise e
                
                    elif msg_.content.lower() == "select 2":
                        await emb_send(chl, "Enter the color for the User Name text:\n`#Hex` or `R, G, B` or `skip` for default")
                        utc = await get_color_input(msg)
                        if utc == None:continue
                        if utc == "skip":utc = (227, 126, 255)
                        data["ut"] = utc
                        await emb_send(chl, taskdone + " Such a cozy color :\). Save your edits using `save` now");await update_emb(to_be_edited)
                    elif msg_.content.lower() == "select 3":
                        await emb_send(chl, "Enter the color for the XP Bar:\n`#Hex` or `R, G, B` or `skip` for default")
                        utc = await get_color_input(msg)
                        if utc == None:continue
                        if utc == "skip":utc = (227, 126, 255)
                        data["xp"] = utc
                        await emb_send(chl, taskdone + " Thats a nice color. You can save your edits using `save` now");await update_emb(to_be_edited)
                    elif msg_.content.lower() == "select 4":
                        await emb_send(chl, "Enter the color for the heading text:\n`#Hex` or `R, G, B` or `skip` for default")
                        utc = await get_color_input(msg)
                        if utc == None:continue
                        if utc == "skip":utc = (227, 126, 255)
                        data["hd"] = utc
                        await emb_send(chl, taskdone +" Hmm. Nice. Save your edits using `save` now");await update_emb(to_be_edited)
                    elif msg_.content.lower() == "select 5":
                        await emb_send(chl, "Enter the text you want to show on your background:", footer_t = "Appears below the XP bar. Enter '0' to remove it.")
                        try:msg_ = await client.wait_for('message', check=check, timeout=150)
                        except asyncio.TimeoutError:await msg.add_reaction(warning);tk(msg);return
                        else:
                           if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");tk(msg);return
                           nope = False
                           for e_word in client.banned_words:
                               if e_word.lower() in msg_.content.lower():nope = True
                               if e_word.lower() in msg_.content.lower().replace("1", "i").replace("3", "e").replace("4", "a").replace("5", "s").replace("0", "o").replace("8", "b"):nope = True
                           if nope:
                               await emb_send(chl, "You can't set this text. Please reselect and try again!");continue
                           if len(msg_.content) > 25:
                               await emb_send(chl, "Max text length limit is 25. Please reselect and try again!");continue
                           if msg_.content == "0":del data["txt"]
                           else:data["txt"] = msg_.content
                           await emb_send(chl, taskdone +" Excited! Done editing? Save your edits using `save` now.");await update_emb(to_be_edited)
                    elif msg_.content.lower() == "select 6":
                        await emb_send(chl, "Enter the color for the Gamebot Logo:\n`#Hex` or `R, G, B` or `skip` for default")
                        old_color = data["lgc"]
                        utc = await get_color_input(msg)
                        if utc == None:continue
                        if utc == "skip":utc = 0
                        if utc:data["lgc"] = '#%02x%02x%02x' % utc
                        else:data["lgc"] = 0
                        if utc != 0:
                            if not bool(sum([e > 128 for e in utc])):
                                await emb_send(chl, warning + " This color is too dark, please reselect and try again")
                                data["lgc"] = old_color
                            else:await emb_send(chl, taskdone +" Hmm. Nice. Done? Save your edits using `save` now");await update_emb(to_be_edited)
                        else:
                            await emb_send(chl, taskdone +" Hmm. Nice. Done? Save your edits using `save` now");await update_emb(to_be_edited)
                    elif msg_.content.lower() == "select 7":
                        await update_emb(to_be_edited, "Background Outline Configurator", 0, get_brd)
                        is_main_conf = 0
                        await emb_send(chl, taskdone + " The dashboard has been updated. Visit it back here: "+to_be_edited.jump_url)
                else:
                    if msg_.content.lower() == "cancel":await emb_edit(to_be_edited, warning+" Background Configurations Cancelled!");tk(msg);return
                    elif msg_.content.lower() == "select 8":
                        data["brd"]["outl"] = 0 if data["brd"]["outl"] else 1
                        await emb_send(chl, taskdone + " Turned " + ("on" if data["brd"]["outl"] else "off") + " outlining. Done? Switch back to your main dashboard using `select 12`");await update_emb(to_be_edited, "Background Outline Configurator", 0, get_brd)
                    elif msg_.content.lower() == "select 9":
                        data["brd"]["shd"] = 0 if data["brd"]["shd"] else 1
                        await emb_send(chl, taskdone + " Turned " + ("on" if data["brd"]["shd"] else "off") + " outline shadows. Switch back to your main dashboard using `select 12`");await update_emb(to_be_edited, "Background Outline Configurator", 0, get_brd)
                    elif msg_.content.lower() == "select 11":
                        data["brd"]["xpb"] = 0 if data["brd"]["xpb"] else 1
                        await emb_send(chl, taskdone + " Turned " + ("on" if data["brd"]["xpb"] else "off") + " XP Bar background. Don't forget to switch back to your main dashboard using `select 12`");await update_emb(to_be_edited, "Background Outline Configurator", 0, get_brd)
                    elif msg_.content.lower() == "select 10":
                        await emb_send(chl, "Enter the color for the border/outline:\n`#Hex` or `R, G, B` or `skip` for white")
                        utc = await get_color_input(msg)
                        if utc == None:continue
                        if utc == "skip":utc = (227, 126, 255)
                        data["brd"]["clr"] = utc
                        await emb_send(chl, taskdone +" Hmm. Nice. Switch back to your main dashboard using `select 12`");await update_emb(to_be_edited, "Background Outline Configurator", 0, get_brd)
                    elif msg_.content.lower() == "select 12":
                        await update_emb(to_be_edited);is_main_conf = 1
                        await emb_send(chl, taskdone + " The dashboard has been updated. Visit it back here: "+to_be_edited.jump_url)
        except Exception as e:
            await emb_send(chl, warning+" Something went wrong.\n```\n"+str(e)+"\n```")
            tk(msg)
            
    elif (await gb_command_check(msg, "set_chl")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        to_channel = msg.channel_mentions
        if to_channel == []:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
        data = get_data()
        if to_channel != None:
            try:data["cmd_chl"][msg.guild.id] += [to_channel]
            except:data["cmd_chl"][msg.guild.id] = [to_channel]
        else:
            try:del data["cmd_chl"][msg.guild.id]
            except:pass
        rewrite_data(data)
        if to_channel == None:
            await emb_send(chl, taskdone+" Any configured channel from this server has been cleared from database. Bot wont auto convert krunker urls anymore.")
        else:
            await emb_send(chl, "{} has been successfully registered for using gamebot commands.".format(chl_mention))
        client.compiled_chls = compile_channels()
    elif (await gb_command_check(msg, "links_chl")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        to_channel = msg.channel_mentions
        if to_channel == []:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
            def check(m):return m.channel == message.channel and m.author == message.author
            linkwarning = """__**PROCEED AT YOUR OWN RISK. I WON'T BE RESPONSILE IF SOMEBODY SPAMS CHANNEL WITH KRUNKER LINKS, IT MAY SPAM PING THE ROLE**__\n*You can prevent this by increasing slowmode*"""
            await message.channel.send("Do you want to ping any role on a link? Enter its name, or Enter `no` to skip.\n"+linkwarning)
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                if msg_.content.lower() == "no":role = ""
                else:
                    role = discord.utils.get(msg.guild.roles, name= msg_.content).mention
                    if role == None:await message.channel.send(warning + " No role found\nPlease try again from start");return
            await message.channel.send("Do you want bot to delete original url message by users? Enter `yes` to confirm, `no` to decline.")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                if msg_.content.lower() == "yes":delete_omsg = 1
                else:delete_omsg = 0
                
            await message.channel.send("Do you want bot to delete embed after game ends? Enter `yes` to confirm, `no` to decline.")
            try:msg_ = await client.wait_for('message', check=check, timeout=100)
            except asyncio.TimeoutError:await message.channel.send(warning+" Automatically cancelling setup after timeout...\nPlease try again.");return
            else:
                if msg_.content.lower() == "cancel":await message.channel.send(warning+" Setup Cancelled!");return
                if msg_.content.lower() == "yes":delete_msg = 1
                else:delete_msg = 0
                

                
        data = get_data()
        if to_channel != None:
            try:data["links_chl"][msg.guild.id] += [[to_channel, role, delete_omsg, delete_msg]]
            except:data["links_chl"][msg.guild.id] = [[to_channel, role, delete_omsg, delete_msg]]
        else:
            try:del data["links_chl"][msg.guild.id]
            except:pass
        rewrite_data(data)
        if to_channel == None:
            await emb_send(chl, taskdone+" Any configured channel from this server has been cleared from database. Commands can be used now in any channel where bot has perm.")
        else:
            await emb_send(chl, "{} has been successfully registered for processing krunker links.\nNote that message should start with krunker url".format(chl_mention))
        client.compiled_chls = compile_channels()

    elif (await gb_command_check(msg, "auto_updates")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        
        to_channel = msg.channel_mentions
        if to_channel == []:
            return
        else:
            chl_mention = to_channel[0]
            
        my_channel = client.get_guild(708067789830750449).get_channel(799911466613342248)
        if not msg.guild.get_member(client.user.id).permissions_in(chl_mention).manage_webhooks:
            await emb_send(chl, warning + " I need `Manage Webhooks` permission for {} to set the channel for krunker updates".format(chl_mention.mention))
        else:
            try:
                await my_channel.follow(destination=chl_mention, reason = "For posting krunker updates, Commanded by "+ str(msg.author))
                await emb_send(chl, "{} has been successfully registered for posting krunker updates.".format(chl_mention.mention))
            except Exception as e:
                await emb_send(chl, warning + " Something bad happened\n```"+str(e)+"```")
            
    elif (await gb_command_check(msg, "leak_updates")) and msg.author.id == dev:
        to_channel = msg.channel_mentions
        if not to_channel:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
        data = get_data()
        if to_channel != None:
            data["leak_chl"][msg.guild.id] = to_channel
        else:
            try:del data["leak_chl"][msg.guild.id]
            except:pass
        rewrite_data(data)
        if not to_channel:
            await emb_send(chl, taskdone+" Any channel configured for krunker updates has been cleared from database.")
        else:
            await emb_send(chl, "{} has been successfully registered for posting krunker updates.".format(chl_mention))
    elif (await gb_command_check(msg, "notify_updates")) and msg.author.id == dev:
        to_channel = msg.channel_mentions
        if not to_channel:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
        data = get_data()
        if to_channel != None:
            data["notif_chl"][msg.guild.id] = to_channel
        else:
            try:del data["notif_chl"][msg.guild.id]
            except:pass
        rewrite_data(data)
        if not to_channel:
            await emb_send(chl, taskdone+" Any channel configured for krunker updates notification has been cleared from database.")
        else:
            await emb_send(chl, "{} has been successfully registered for posting krunker update notifications.".format(chl_mention))


    elif (await gb_command_check(msg, "del_chl")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        to_channel = msg.channel_mentions
        if to_channel == []:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
        data = get_data()
        if to_channel != None:
            try:
                if len(data["cmd_chl"][msg.guild.id]) >= 2:
                    data["cmd_chl"][msg.guild.id].remove(to_channel)
                else:
                    await emb_send(chl, warning+" Please use `g.set_chl 0` to remove all configured channels.");return
            except:
                await emb_send(chl, taskdone+" This channel was never configured for commands anyways.");return
        else:
            await emb_send(chl, warning+" Please define a channel.");return
        rewrite_data(data)
        await emb_send(chl, "{} has been successfully removed from channels accessible by Gamebot.".format(chl_mention))
        client.compiled_chls = compile_channels()

    elif (await gb_command_check(msg, "list_chl", "", 1)) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        data = get_var("cmd_chl")
        try:
            channels = data[msg.guild.id]
            desc = ""
            for e_chl in channels:
                try:
                    desc += msg.guild.get_channel(e_chl).mention + "\n"
                except:
                    desc += "#invalid-channel"
            await emb_send(chl, desc, title_ = "Channels where commands can be used:", footer_t = "Remove a channel using 'g.del_chl'\nAdd a channel using 'g.set_chl'")
        except:
            await emb_send(chl, warning + " You haven't selected any channel for bot commands.", footer_t = "Set a channel using 'g.set_chl'")
            return

    elif (await gb_command_check(msg, "disable")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        cmdname = gb_command_fix(msg, "disable")
        if cmdname not in disableable:
            await emb_send(chl, warning + " This command can't be disabled.");return
        data = get_data()
        try:data["disabled_cmds"][msg.guild.id] += [cmdname]
        except:data["disabled_cmds"][msg.guild.id] = [cmdname]
        rewrite_data(data)
        await emb_send(chl, taskdone+" Disabled the command!")
        client.compiled_cmds = compile_cmds()
    elif (await gb_command_check(msg, "enable")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        cmdname = gb_command_fix(msg, "enable")
        if cmdname not in disableable:
            await emb_send(chl, warning + " This command was never disabled.");return
        data = get_data()
        try:data["disabled_cmds"][msg.guild.id].remove(cmdname)
        except:del data["disabled_cmds"][msg.guild.id]
        rewrite_data(data)
        await emb_send(chl, taskdone+" Enabled the command!")
        client.compiled_cmds = compile_cmds()
    elif (await gb_command_check(msg, "incognito", "", 1)):
        client.loop.create_task(do_on_message(msg, -1))
        if msg.author.id in get_var("incognito"):
            pop_obj_var("incognito", msg.author.id)
            await emb_send(chl, taskdone + " You are now in public mode")
            return
        append_var("incognito", [msg.author.id])
        await emb_send(chl, taskdone + " You are now in invisible mode", footer_t = "Users wont be able to see your discord name and tag on your profile, neither your in-game name using your discord account. Rest assured.")
    elif (await gb_command_check(msg, "cmds", "", 1)) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        client.loop.create_task(do_on_message(msg, -1))
        data = get_var("disabled_cmds")
        try:
            cmds = data[msg.guild.id]
            if cmds == []:
                raise TypeError()
            desc = "```css\n"
            for x, e_chl in enumerate(cmds, 1):
                desc += "{}. g.{}\n".format(x, e_chl)
            desc += "```"
            await emb_send(chl, desc, title_ = "Following are the disabled commands:", footer_t = "Disable a fun command using 'g.disable <cmd>'\nEnable a command using 'g.enable <cmd>'")
        except:await emb_send(chl, warning + " You have not disabled any command.", footer_t = "Disable a fun command using 'g.disable <cmd>'\nEnable a command using 'g.enable <cmd>'")
        
    elif (await gb_command_check(msg, "set_conf")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        to_channel = msg.channel_mentions
        if to_channel == []:to_channel = None
        else:
            chl_mention = to_channel[0].mention
            to_channel = to_channel[0].id
        with open("Data/serverconf.bt", "rb") as file:
            try:confs = pickle.load(file)
            except:confs = {}
        confs[msg.guild.id] = {"chl_id":to_channel}
        with open("Data/serverconf.bt", "wb") as file:
            pickle.dump(confs, file)
        if to_channel == None:
            await message.channel.send("Any configured channel from this server has been cleared from database. The channel wont receive any updates about featured maps")
        else:
            await message.channel.send("{} has been successfully registered for redirecting news about featured maps".format(chl_mention))
    elif (await gb_command_check(msg, "show_conf", "")) and (message.author.guild_permissions.administrator == True or msg.author.id == 669816890163724288):
        with open("Data/serverconf.bt", "rb") as file:
            try:confs = pickle.load(file)
            except:confs = {}
        try:
            chl_ = confs[msg.guild.id]["chl_id"]
            await message.channel.send("{} is the current channel configured for featured map notification".format(msg.guild.get_channel(chl_).mention))
        except Exception as e:
            print(e)
            await message.channel.send("No channel has been set yet")

    elif msg.id in missed_cmds:
        await chl.send(embed=discord.Embed(colour=discord.Colour(14423783), description = warning+ " Missing an argument."))
    elif message.content.lower().startswith(prefix):
        possible_ = await close_matches(message.content.split(" ")[0].lower()[2:], all_commands)
        if possible_:
            if possible_.lower() != message.content.split(" ")[0].lower()[2:]:
                client.loop.create_task(do_on_message(msg))
                if msg.author.id not in ignore_users:await update_cool_d2(message.author.id)
                meant_ = await message.reply(embed=discord.Embed(colour=discord.Colour(14423783), title = question+ " Did you mean `{}` ?".format(prefix+possible_)))
                def check(m):
                    return m.channel == message.channel and m.author == message.author
                try:
                    msg_ = await client.wait_for('message', check=check, timeout=20)
                except asyncio.TimeoutError:
                    return
                else:
                    if "yes" in msg_.content.lower():
                        embed = embed=discord.Embed(colour=discord.Colour(14423783), title = taskdone+" You meant `{}`".format(prefix+possible_))
                        await meant_.edit(embed = embed)
                        message.content = message.content.replace(message.content.split(" ")[0][2:], possible_)
                        custom_msgs.append(message.id)
                        await on_message(message)
                    return

    await asyncio.sleep(0)
                
    

def get_players_c(hosts_data, ___map_name___):
    total_ppl_c = 0
    for hosted_game in hosts_data:
        if hosted_game[-1]["i"].split('_', 1)[1].lower() == ___map_name___.lower():
            total_ppl_c += hosted_game[2]
    return total_ppl_c

        
@client.event
async def on_guild_join(server):
    print("Joined a server - ", server.name)
    if not client.disable_status:
        await client.change_presence(status=client.bstatus, activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds))+" servers"))
    await emb_send(client.get_guild(708067789830750449).get_channel(741704072704425984), "Joined a server - "+ server.name)
    for e_chl in server.text_channels:
        if e_chl.permissions_for(server.me).send_messages:
            await emb_send(e_chl,
                           """Use `g.help` to get list of all commands
Use `g.help chl` to get help in configuring gamebot for your server
Use `g.staff` to get list of our staff members for support
Use `g.server` to join support server

*By using the bot, you agree and comply with our Terms and Conditions. Use `g.tc`*""",
                           title_ = "Thank you for inviting me to your server!")
            break
@client.event
async def on_guild_remove(server):
    print("Left a server - ", server.name)
    if not client.disable_status:
        await client.change_presence(status=client.bstatus, activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds))+" servers"))
    await emb_send(client.get_guild(708067789830750449).get_channel(741704072704425984), "Left a server - "+ server.name)
    try:
        data = get_data()
        del data["cmd_chl"][server.id]
        rewrite_data(data)
        client.compiled_chls = compile_channels()
    except:pass


def make_clan_out(data, user_name, creator, msg_chl, start = 0, pages_ = 1, pages_main = None):
    maps = data[3]["members"]
    mem_count = len(maps)
    #maps = sorted(maps, key = lambda x: x["s"], reverse= True)
    captains  = []
    n_captains = []
    soldiers = []
    n_soldiers = []
    recruits =  []
    n_recruits = []
    commander = []
    n_commander = []
    for e_map in maps:
        #print(repr(e_map))
        if e_map['r'] == 2 and not e_map['p'].lower() == creator.lower():
            captains.append(e_map)
        elif e_map['r'] == 1 and not e_map['p'].lower() == creator.lower():
            soldiers.append(e_map)
        elif e_map['r'] == 0 and not e_map['p'].lower() == creator.lower():
            recruits.append(e_map)
        elif e_map['p'].lower() == creator.lower():
            commander = [e_map]
    captains = sorted(captains, key = lambda x: x["s"], reverse= True)
    soldiers = sorted(soldiers, key = lambda x: x["s"], reverse= True)
    recruits = sorted(recruits, key = lambda x: x["s"], reverse= True)
    total_captains = len(captains)
    total_soldiers = len(soldiers)
    total_recruits = len(recruits)
    del maps

    maps = commander + captains + soldiers + recruits
    for x, e_map in enumerate(maps):
        if x >= start and x < int(start+20):
            if e_map['r'] == 2 and not e_map['p'].lower() == creator.lower():n_captains.append(e_map)
            elif e_map['r'] == 1 and not e_map['p'].lower() == creator.lower():n_soldiers.append(e_map)
            elif e_map['r'] == 0 and not e_map['p'].lower() == creator.lower():n_recruits.append(e_map)
            elif e_map['p'].lower() == creator.lower():n_commander = [e_map]
    del maps

    if n_commander:
        maps = n_commander
    else:
        maps = []
    maps =  maps + n_captains + n_soldiers + n_recruits
    header_offset = 0
    header_offset = 42 * sum([bool(n_r) for n_r in [n_commander, n_captains, n_soldiers, n_recruits]])
    if len(maps) == 0:
        return None
    font_size = 17
    offset = 15
    black_color = (255, 255, 255)
    y = len(maps) * 31
    y += offset + 40 + 5 + 40
    dash_text_offset = 0
    if pages_ == 1:
        y += 40
        dash_text_offset = 40


    img = Image.new('RGBA', (520, y+header_offset), (0, 0, 0, 0))
    #img = newGrad((460, y+header_offset))
    draw = ImageDraw.Draw(img)
    font = client.main_font
    font2 = client.main_font2
    font3 = client.main_font3
    fontn = ImageFont.truetype(font_file, font_size-3)
    unicode_font = ImageFont.truetype("Data/unifont.ttf", font_size+3+2)
    font_size += 10
    def filter_votes(votes):
        if not votes:return [13, (100, 100, 100), '', '', votes]
        elif votes > 0 and votes < 100:return [0, (15, 220, 15), '+', '', votes]
        elif votes < 0: return [6, (235, 10, 10), '', '', votes]
        elif votes > 100:return [0, (15, 220, 15), '', '+', 99]
    def filter_color(verification):
        if verification == 0:
            return (255, 203, 73)
        return (255, 0, 255)
    def write_top(draw, page_ = 1):
        if page_ != 1:
            twidth = write_clan_name(draw, (15, 10), data[3]['clan_rank'], user_name, font3, unicode_font)
            outline_text(draw, 15+twidth+5, 10, (255, 255, 255), (0, 0, 0), " by {}".format(creator), font3, 2)
            if pages_main != 1: outline_text(draw, 370, 10, (200, 200, 200), (0, 0, 0), "PG# {} of {}".format(pages_, pages_main), fontn, 2)
            outline_text(draw, 15, 10+30+7, (200, 200, 200), (0, 0, 0), "LVL "+xp_count(data[3]['clan_score']), font, 2)
            outline_text(draw, 170, 10+30+7, (200, 200, 200), (0, 0, 0), "{} Members".format(mem_count), font, 2)
            outline_text(draw, 350, 10+30+7, (200, 200, 200), (0, 0, 0), str(data[3]['clan_score']), font, 2)
        else:
            pass
            bimg = Image.new('RGB', (493,90), (70, 75, 75))

            bimg = classic_outline(bimg, x_ = 5, y_ = 5, border = 1)
            #bimg = add_corners(bimg, 25)

            img.paste(bimg, (10, 10), bimg)

            imgshd = Image.new('RGBA', (520, y+header_offset), (0, 0, 0, 0))
            #img = newGrad((460, y+header_offset))
            drawshd = ImageDraw.Draw(imgshd)
            
            twidth = write_clan_name(drawshd, (30, 25), data[3]['clan_rank'], user_name, font3, unicode_font)

            outline_text(drawshd, 30+twidth+20, 25, (200, 200, 200), (0, 0, 0), "by {}".format(creator), font3, 2)

            twidth, _ = drawshd.textsize("{:,}".format(data[3]['clan_score']), font)
            outline_text(drawshd, 493-twidth, 25, (200, 200, 200), (0, 0, 0), "{:,}".format(data[3]['clan_score']), font, 2)
            
            outline_text(drawshd, 30, 10+30+7+20, (200, 200, 200), (0, 0, 0), "Level  "+xp_count(data[3]['clan_score']), font, 2)
            twidth, _ = drawshd.textsize("{:,} Members".format(mem_count), font)
            outline_text(drawshd, 493-twidth, 10+30+7+20, (200, 200, 200), (0, 0, 0), "{:,} Members".format(mem_count), font, 2)

            dark_img_ = ImageEnhance.Brightness(imgshd).enhance(0)
            dark_img_ = dark_img_.filter(ImageFilter.GaussianBlur(radius=2))
            dark_img_.paste(imgshd, (0, 0), imgshd)
            img.paste(dark_img_, (0, 0), dark_img_)
            
            #imgshd3.paste(thumb, (50+21+12+num_x, 18+15+60+((335-40-30-20)*rowx)), thumb)
            
    topthr = threading.Thread(target = write_top, args = (draw, pages_))
    topthr.start()
    offset = 44
    n_header_offset = []
    all_headings = []
    for x, e_map in enumerate(maps):
        if creator.lower() == e_map['p'].lower():
            all_headings.append(1)
        elif e_map['r'] == 2:
            all_headings.append(2)
        elif e_map['r'] == 1:
            all_headings.append(3)
        else:
            all_headings.append(4)
    i1nhd = 1 in all_headings
    i2nhd = 2 in all_headings
    i3nhd = 3 in all_headings
    i4nhd = 4 in all_headings
    all_calcs = [sum([i1nhd]), sum([i1nhd, i2nhd]), sum([i1nhd, i2nhd, i3nhd]), sum([i1nhd, i2nhd, i3nhd, i4nhd])]
    all_headings = []
    def write_e_line(x, e_map, all_headings, n_header_offset, all_calcs):
        if creator.lower() == e_map['p'].lower():
            this_type = 1
            
            if 1 not in all_headings:
                all_headings.append(1)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1]-1)*41)+dash_text_offset, (255, 255, 255), (0, 0, 0), "Commanders ----------------- 1/1", font3, 2)
                n_header_offset.append(41)
            m_c = (191, 65, 249)#(235, 64, 52)
        elif e_map['r'] == 2:
            this_type = 2
            if 2 not in all_headings:
                all_headings.append(2)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1]-1)*41)+dash_text_offset, (255, 255, 255), (0, 0, 0), "Captains -------------------- "+str(total_captains)+"/5", font3, 2)
                n_header_offset.append(41)
            m_c = (243, 65, 249)#
        elif e_map['r'] == 1:
            this_type = 3
            if 3 not in all_headings:
                all_headings.append(3)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1]-1)*41)+dash_text_offset, (255, 255, 255), (0, 0, 0), "Soldiers -------------------- {}/25".format(total_soldiers), font3, 2)
                n_header_offset.append(41)

            m_c = (228, 140, 231)
        else:
            this_type = 4
            if 4 not in all_headings:
                all_headings.append(4)
                outline_text(draw, 10, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1]-1)*41)+dash_text_offset, (255, 255, 255), (0, 0, 0), "Recruits -------------------- "+ "{:,}".format(total_recruits), font3, 2)
                n_header_offset.append(41)

            m_c = (243, 189, 242)

        offset_pf = 0
        if e_map['su'] > 0:
            prem = Image.open(prem_img, "r")
            img.paste(prem, (10, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1])*41)+dash_text_offset), prem)
            offset_pf += 21
            
        if bool(e_map['ve']):
            verif = Image.open(verif_img,"r")
            if e_map['pr'] > 0: v_x = 10 + 21
            else:v_x = 10
            img.paste(verif, (31, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1])*41)+dash_text_offset), verif)
        twidth, _ = draw.textsize("|  "+e_map["p"], font=font)
        try:
            if e_map["h"]:
                m_c = (232, 86, 86)
        except:pass
        outline_text(draw, 56, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1])*41)+dash_text_offset, m_c, (0, 0, 0), "|  "+e_map["p"], font)
        outline_text(draw, 400, 12+((font_size+4)*x)+offset+25+((all_calcs[this_type-1])*41)+dash_text_offset, black_color, (0, 0, 0), "LVL "+xp_count(e_map["s"]), font)

    threads = []
    for x, e_map in enumerate(maps):
        e_l_thr = threading.Thread(target= write_e_line, args = (x, e_map, all_headings, n_header_offset, all_calcs))
        e_l_thr.start()
        threads.append(e_l_thr)

    topthr.join()
    for e_t in threads:
        e_t.join()
    
    ngb_logo = client.gb
    __x__, __y__ = img.size
    img.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)   
    dark_img = ImageEnhance.Brightness(img).enhance(0)
    dark_img2 = dark_img.filter(ImageFilter.GaussianBlur(radius=9))
    dark_img = dark_img.filter(ImageFilter.GaussianBlur(radius=2))
    dark_img.paste(dark_img2, (0, 0), dark_img2)
    dark_img.paste(img, (0, 0), img)
    
    if user_name.lower() == "dev":
        gr_img = newGrad((520, y+header_offset), (3, 95, 136), (0, 32, 105))
    else:
        gr_img = newGrad((520, y+header_offset))
    gr_img.paste(dark_img, (0, 0), dark_img)
    gr_img = classic_outline(gr_img)

    byte_io = BytesIO()
    byte_io.seek(0)
    gr_img.save(byte_io, 'PNG')
    byte_io.seek(0)
    return byte_io


async def get_map_g(map_name, msg_):
    if True:
        try:
            with open(graph_data_file, "rb") as file:
                old_data = pickle.load(file)
            maps = []
            for e_map in old_data:maps += list(e_map.values())[0]
            try:
                for e_map in maps:
                    try:map_data = e_map[map_name.lower()]
                    except:pass
                if map_data:pass
            except:
                await msg_.channel.send(embed=discord.Embed(title = warning+ " Please register before using this command",
                                                            description = "Make sure you are using correct map name. If its correct map name, register using `g.reg <user-name>`"))
                return
            return map_data
        except :
            raise TimeoutError()

async def UpdateGData():
    with open(graph_data_file, "rb") as file:
        old_data = pickle.load(file)
    ppls = []
    ppl_ns = []
    for e_map in old_data:
        ppls.append(list(e_map.values())[1])
        ppl_ns.append(list(e_map.keys())[0])
    print("\n\nProcessing\n\n")
    for e_ppl, ppl_n in zip(ppls, ppl_ns):
        print(".")
        while True:
            try:
                hosts_htm = await await_get(api_maps_url+str(e_ppl))
                break
            except:print("Web error")
        maps = json.loads(hosts_htm)['data']
        for x_, each_ppl in enumerate(old_data):
            if list(each_ppl.keys())[0] == ppl_n:
                for e_map in maps:
                    _maps_ = old_data[x_][ppl_n]
                    o_maps_ = {}
                    for _map_ in _maps_:
                        o_maps_[list(_map_.keys())[0]] = list(_map_.values())[0]
                    _maps_ = o_maps_
                    try:
                        _maps_[e_map['map_name'].lower()]
                    except Exception as e:
                        map_g_data = []
                        map_g_data_int = {}
                        map_g_data_int['likes'] = [e_map['map_votes']] + list([None]*13)
                        map_g_data_int['plays'] = [e_map['map_pl']] + list([None]*13)
                        map_g_data_int['funds'] = [e_map['fund']] + list([None]*13)
                        map_g_data.append({e_map['map_name'].lower(): map_g_data_int})
                        continue
                    if len(_maps_[e_map['map_name'].lower()]['likes']) == 14:
                        del _maps_[e_map['map_name'].lower()]['likes'][-1]
                    _maps_[e_map['map_name'].lower()]['likes'].insert(0, e_map['map_votes'])
                    
                    if len(_maps_[e_map['map_name'].lower()]['plays']) == 14:
                        del _maps_[e_map['map_name'].lower()]['plays'][-1]
                    _maps_[e_map['map_name'].lower()]['plays'].insert(0, e_map['map_pl'])
                    try:
                        if len(_maps_[e_map['map_name'].lower()]['funds']) == 14:
                            del _maps_[e_map['map_name'].lower()]['funds'][-1]
                        _maps_[e_map['map_name'].lower()]['funds'].insert(0, e_map['fund'])
                    except:
                        _maps_[e_map['map_name'].lower()]['funds'] = [e_map['fund']] + list([None]*13)
                    
                try:old_data[x_][ppl_n] += map_g_data
                except Exception as e:pass
        await asyncio.sleep(10)
    with open(graph_data_file, "wb") as file:
        pickle.dump(old_data, file)

async def UpdateSweeps():
    with open("Data/sweep.bt", "rb") as file:
        old_data = pickle.load(file)
    to_be_sweeped = {}
    for id_, e_clan in old_data.items():
        if e_clan["tm"] == 1:
            to_be_sweeped[e_clan["cn"]] = id_
    data = await sweep_ws(list(to_be_sweeped.keys()))
    for e_clan in data:
        old_data[to_be_sweeped[e_clan[2].lower()]]["data"] = e_clan[3]
    with open(sweep_file, "wb") as file:
        pickle.dump(old_data, file)
        
async def UpdateRolesNicks():
    print("-------Managing Servers---------")
    with open("Data/servers.bt", "rb") as file:
        old_data = pickle.load(file)
    clans = [e_clan["cn"] for e_clan in old_data.values() if e_clan["cn"]]
    clans_guilds = {e_clan["cn"].lower(): [e_clank, e_clan["msg"], e_clan["rl"], e_clan["rank"], e_clan["disabled"], e_clan["logs"]] for e_clank, e_clan in old_data.items()}
    random.shuffle(clans)
    data = await sweep_ws(clans)
    for e_clan in data:
        try:maps = e_clan[3]["members"]
        except:continue
        clan_members = [e_map["p"].lower() for e_map in maps]
        clan_members2 = [e_map["p"] for e_map in maps]
        clan_member_ranks = {e_map["p"].lower():e_map["r"] for e_map in maps}
        user_name = e_clan[3]["clan_name"]
        creator_name = e_clan[3]["creatorname"]
        if clans_guilds[user_name.lower()][4]:
            continue
        guild = client.get_guild(clans_guilds[user_name.lower()][0])
        try:role = guild.get_role(clans_guilds[user_name.lower()][2])
        except:continue
        roles_list = clans_guilds[user_name.lower()][3]
        server_mems = {}
        for e_mem in clan_members:
            try: server_mems[guild.get_member((await get_author_name(None, e_mem)).id)] = e_mem.lower()
            except: pass
        for member, ln_acc in server_mems.items():
            try:
                if True:
                    if ln_acc.lower() == creator_name.lower():
                        continue
                    mem_nick = member.nick if member.nick != None else member.name
                    nick_n = clans_guilds[user_name.lower()][1].replace("{clan}", user_name).replace("{ign}", clan_members2[clan_members.index(ln_acc)]).replace("{nm}", member.name).replace("{nick}", mem_nick)
                    if nick_n != mem_nick and clans_guilds[user_name.lower()][1] != "{nick}":
                        await member.edit(nick = nick_n)
                        await asyncio.sleep(0.4)
                    if role not in member.roles:
                        await member.add_roles(role)
                        try:
                            log_text = "Updated roles for " + member.mention + " +(Clan Roles...)"
                            embed = discord.Embed(colour=discord.Colour(14423783), description = log_text)
                            await guild.get_channel(clans_guilds[user_name.lower()][5]).send(embed = embed)
                        except:pass
                        await asyncio.sleep(0.4)

                    e_role = clan_member_ranks[ln_acc]
                    if (rrole := guild.get_role(roles_list[e_role])) not in member.roles:
                        await member.add_roles(rrole)
                        await asyncio.sleep(0.4)
                    for e_role in roles_list:
                        if (arole := guild.get_role(e_role)) in member.roles and arole != rrole:
                            await member.remove_roles(arole)
                            await asyncio.sleep(0.4)
                        
            except Exception as e:pass
        try:
            roles_list_obj = [guild.get_role(e_role) for e_role in roles_list]
            try:
                all_roled_mems = list(set(role.members + roles_list_obj[0].members + roles_list_obj[1].members + roles_list_obj[2].members))
            except:
                all_roled_mems = role.members
            for member in all_roled_mems:
                try:
                    m_is_in = False
                    for e_acc in (userrr := get_author_list(None, member.id)):
                        if e_acc in clan_members:
                            m_is_in = e_acc
                    if not m_is_in:
                        await member.edit(nick = member.name);
                        if role in member.roles:
                            await member.remove_roles(role)
                            try:
                                log_text = member.mention+ " left the clan (`{}`)".format(userrr[-1]) + str(" | Profile Unlinked. Please link the member. Use `g.auto_manage link`" if not userrr else "")
                                embed = discord.Embed(colour=discord.Colour(14423783), description = log_text)
                                await guild.get_channel(clans_guilds[user_name.lower()][5]).send(embed = embed)
                            except:
                                pass
                        for e_role in roles_list:
                            if (rrole := guild.get_role(e_role)) in member.roles:
                                await member.remove_roles(rrole)
                                await asyncio.sleep(0.4)
                        await asyncio.sleep(1)
                except:pass
        except:pass
    print("--------Managing Done--------")
        
async def update_trigger():
    while True:
        print("\n\nWaiting")
        await asyncio.sleep(datetime.datetime.now().replace(hour=23, minute=59, second=59).timestamp() - datetime.datetime.now().timestamp())
        if client.dismiss_:
            print("Dismissed")
            client.dismiss_ = False
            continue
        print("Triggered")
        await UpdateGData()
        await UpdateSweeps()
  
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def trim_pro(img):
    img = img.convert("RGBA")
    pixels = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            p_c = list(pixels[x, y])
            if p_c[:3] not in [[0, 0, 0], [255, 0, 0], [0, 255, 0]]:
                pixels[x, y] = (255, 255, 255, 0)
    img = trim(img)
    img = img.convert("RGB")
    return img.copy()
def graph_make(data, data2, data3, Map_Name = "map"):
    import matplotlib.pyplot as plt
    tod = datetime.datetime.now()
    color = "#bababa"
    params = {'legend.fontsize': 'x-large', 'figure.figsize': (10, 5), 'axes.labelsize': 'x-large',
         'ytick.labelsize':12, 'text.color' : "#ffffff", 'axes.labelcolor' : "#ffffff",
        'grid.color':"#ffffff", 'hatch.color':color, 'legend.edgecolor':color,
          'lines.color':color, 'patch.edgecolor': color, 'xtick.color': color,
          'ytick.color': color, 'axes.edgecolor':"#ffffff",}
    pylab.rcParams.update(params)
    _1_d = tod - datetime.timedelta(days = 1);_2_d = tod - datetime.timedelta(days = 2);_3_d = tod - datetime.timedelta(days = 3);_4_d = tod - datetime.timedelta(days = 4);_5_d = tod - datetime.timedelta(days = 5);_6_d = tod - datetime.timedelta(days = 6);_7_d = tod - datetime.timedelta(days = 7);_8_d = tod - datetime.timedelta(days = 8);_9_d = tod - datetime.timedelta(days = 9);_10_d = tod - datetime.timedelta(days = 10);_11_d = tod - datetime.timedelta(days = 11);_12_d = tod - datetime.timedelta(days = 12);_13_d = tod - datetime.timedelta(days = 13)
    x = ["today",
         _1_d.strftime("%d %b"), _2_d.strftime("%d %b"), _3_d.strftime("%d %b"),
         _4_d.strftime("%d %b"), _5_d.strftime("%d %b"), _6_d.strftime("%d %b"),
         _7_d.strftime("%d %b"), _8_d.strftime("%d %b"), _9_d.strftime("%d %b"),
         _10_d.strftime("%d %b"), _11_d.strftime("%d %b"), _12_d.strftime("%d %b"), _13_d.strftime("%d %b")]
    x.reverse()
    y = data
    y.reverse()

    y2 = data2
    y2.reverse()
    y3 = data3
    y3.reverse()
    

    fig = plt.figure()
    host = fig.add_subplot(111)
    def fix_height(y_):
        _y_ = int(((y_*11)//11)/2)
        if _y_ < 5: _y_ = 5
        return _y_
    par1 = host.twinx()
    par2 = host.twinx()
    plt.yticks(fontweight="bold")
    fig.set_size_inches(10, 5)
    host.set_title(Map_Name)
    def fix_color(val):
        val -= 0.9
        if val < 0:val = 0
        return val
    def fix_color2(val):
        val += 0.5
        if val > 1:val = 1
        return val
    yfil = [e_y for e_y in y if e_y]
    if not yfil:yfil = [0]
    y2fil = [e_y for e_y in y2 if e_y]
    if not y2fil:y2fil = [0]
    y3fil = [e_y for e_y in y3 if e_y]
    if not y3fil:y3fil = [0]
    
    offset = fix_height(max(yfil)-min(yfil))
    host.set_ylim([min(yfil)-offset,max(yfil)+offset])
    offset = fix_height(max(y2fil)-min(y2fil))
    par1.set_ylim([min(y2fil)-offset,max(y2fil)+offset])
    try:
        miny3 = min(y3fil)
        maxy3 = max(y3fil)
        offset = fix_height(maxy3-miny3)
        par2.set_ylim([miny3-offset,maxy3+offset])
    except:pass
    
    par1.set_ylabel("Plays")
    par2.set_ylabel("KR")
    host.set_ylabel("Likes")    
    for tick in host.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    for tick in par1.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    host.grid()
    par2.spines["right"].set_position(("axes", 1.15))
    #new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    #par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        #offset=(60, 0))
    plt_ = host.plot(x,y, color=(Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255), linewidth=5)
    plt2_ = par1.plot(x,y2, color=(0.05, 0.8, 1), linewidth=4)
    plt3_ = par2.plot(x, y3, color=(0.8, 0.8, 0), linewidth=3)
    host.legend(prop=dict(weight='bold'))
    y_bars = host.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((fix_color2(x_/len(y_bars))-0.1 ,0.5 , 1))
        y_bar.set_fontweight("bold")
    y_bars = par1.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((0.01 ,fix_color2(x_/len(y_bars)) , fix_color2(x_/len(y_bars))))
        y_bar.set_fontweight("bold")

    y_bars = par2.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((fix_color2(x_/len(y_bars)) ,fix_color2(x_/len(y_bars)) , 0.1))
        y_bar.set_fontweight("bold")
        
    par1.yaxis.label.set_color('cyan')
    par2.yaxis.label.set_color('yellow')
    host.yaxis.label.set_color((Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255))
    plt.yticks(fontweight="bold")
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.autoscale(enable=True, axis='x', tight=True)
    byte_io = BytesIO()
    byte_io.seek(0)
    plt.savefig(byte_io, dpi=200, transparent=True, format='png', bbox_inches='tight')
    byte_io.seek(0)

    bg = Image.open(byte_io)
    ngb_logo = client.gb
    __x__, __y__ = bg.size
    bg.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
            
    new_im = trim(bg)
    byte_io = BytesIO()
    byte_io.seek(0)
    new_im.save(byte_io, format='png')
    byte_io.seek(0)

    plt.clf()
    plt.cla()
    plt.close()
    return byte_io

def lobbies_make(data, data2, data3, Map_Name = "map"):
    import matplotlib.pyplot as plt
    tod = datetime.datetime.now()
    color = "#bababa"
    params = {'legend.fontsize': 'x-large', 'figure.figsize': (10, 5), 'axes.labelsize': 'x-large',
         'ytick.labelsize':12, 'text.color' : "#ffffff", 'axes.labelcolor' : "#ffffff",
        'grid.color':'#ffffff', 'hatch.color':color, 'legend.edgecolor':color,
          'lines.color':color, 'patch.edgecolor': color, 'xtick.color': color,
          'ytick.color': color, 'axes.edgecolor':"#ffffff",}
    pylab.rcParams.update(params)
    
    x = data3
    x.reverse()
    y = data
    y.reverse()

    y2 = data2
    y2.reverse()

    for x_val, e_x in enumerate(x):
        x[x_val] = datetime.datetime.fromtimestamp(e_x)
        

    fig = plt.figure()
    host = fig.add_subplot(111)
    def fix_height(y_):
        _y_ = int(((y_*11)//11)/2)
        if _y_ < 5: _y_ = 5
        return _y_
    par1 = host.twinx()
    plt.yticks(fontweight="bold")
    fig.set_size_inches(10, 5)
    host.set_title(Map_Name)
    def fix_color(val):
        val -= 0.9
        if val < 0:val = 0
        return val
    def fix_color2(val):
        val += 0.5
        if val > 1:val = 1
        return val
    yfil = [e_y for e_y in y if e_y]
    if not yfil:yfil = [0]
    y2fil = [e_y for e_y in y2 if e_y]
    if not y2fil:y2fil = [0]
    
    offset = fix_height(max(yfil)-min(yfil))
    host.set_ylim([min(yfil)-offset,max(yfil)+offset])
    offset = fix_height(max(y2fil)-min(y2fil))
    par1.set_ylim([min(y2fil)-offset,max(y2fil)+offset])
    
    par1.set_ylabel("Lobbies")
    host.set_ylabel("Online")    
    for tick in host.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    for tick in par1.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    host.grid()
    plt_ = host.plot(x, y, color=(Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255), linewidth=5)
    plt2_ = par1.plot(x,y2, color=(0.05, 0.8, 1), linewidth=3)

    
    host.legend(prop=dict(weight='bold'))
    y_bars = host.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((fix_color2(x_/len(y_bars))-0.1 ,0.5 , 1))
        y_bar.set_fontweight("bold")
    y_bars = par1.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((0.01 ,fix_color2(x_/len(y_bars)) , fix_color2(x_/len(y_bars))))
        y_bar.set_fontweight("bold")

        
    par1.yaxis.label.set_color('cyan')
    host.yaxis.label.set_color((Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255))
    plt.yticks(fontweight="bold")
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.autoscale(enable=True, axis='x', tight=True)
    byte_io = BytesIO()
    byte_io.seek(0)
    plt.savefig(byte_io, dpi=200, transparent=True, format='png', bbox_inches='tight')
    byte_io.seek(0)

    bg = Image.open(byte_io)
    ngb_logo = client.gb
    __x__, __y__ = bg.size
    bg.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
            
    new_im = trim(bg)
    
    byte_io = BytesIO()
    byte_io.seek(0)
    new_im.save(byte_io, format='png')
    byte_io.seek(0)

    plt.clf()
    plt.cla()
    plt.close()
    return byte_io

def impression_make(data, user_name = "Unknown"):
    import matplotlib.pyplot as plt
    tod = datetime.datetime.now()
    color = "#bababa"
    params = {'legend.fontsize': 'x-large', 'figure.figsize': (10, 5), 'axes.labelsize': 'x-large',
         'ytick.labelsize':12, 'text.color' : "#ffffff", 'axes.labelcolor' : "#ffffff",
        'grid.color':"#ffffff", 'hatch.color':color, 'legend.edgecolor':color,
          'lines.color':color, 'patch.edgecolor': color, 'xtick.color': color,
          'ytick.color': color, 'axes.edgecolor':"#ffffff",}
    pylab.rcParams.update(params)
    _0_d = tod
    _1_d = tod - datetime.timedelta(days = 1);
    _2_d = tod - datetime.timedelta(days = 2);
    _3_d = tod - datetime.timedelta(days = 3);
    _4_d = tod - datetime.timedelta(days = 4);
    _5_d = tod - datetime.timedelta(days = 5);
    _6_d = tod - datetime.timedelta(days = 6);
    _7_d = tod - datetime.timedelta(days = 7);
    all_days = [_0_d, _1_d, _2_d, _3_d, _4_d, _5_d, _6_d, _7_d]
    all_days = {e_d.date():e_d for e_d in all_days}
    all_days_y = {_0_d:0, _1_d:0, _2_d:0, _3_d:0, _4_d:0, _5_d:0, _6_d:0, _7_d:0}
    for e_d in data:
        that_day = datetime.datetime.fromtimestamp(int(e_d))
        if that_day.date() in all_days.keys():
            all_days_y[all_days[that_day.date()]] += 1
    x = list(all_days_y.keys())
    x = [ed.strftime("%d %b") for ed in x]
    x.reverse()
    
    y = list(all_days_y.values())
    y.reverse()

    fig = plt.figure()
    host = fig.add_subplot(111)
    def fix_height(y_):
        _y_ = int(((y_*11)//11)/2)
        if _y_ < 5: _y_ = 5
        return _y_
    plt.yticks(fontweight="bold")
    fig.set_size_inches(10, 5)
    host.set_title(user_name)
    host.set_ylabel("Views")
    def fix_color(val):
        val -= 0.9
        if val < 0:val = 0
        return val
    def fix_color2(val):
        val += 0.5
        if val > 1:val = 1
        return val
    offset = fix_height(max(y)-min(y))
    host.set_ylim([0,max(y)+offset])
    for tick in host.xaxis.get_major_ticks():
        tick.label.set_fontsize(6)
    host.grid()
    #plt_ = host.fill(x, y, color=(Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255), alpha = 0.5)
    plt.yticks(fontweight="bold")
    
    plt_ = host.bar(x, y, color=(Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255), linewidth=4)
    #plt_ = host.plot(x, y, color=(0.7, 0, 1), linewidth=2)
    #host.fill_between(x, y, 0, where= y, facecolor=(Main_Color[0]/255, Main_Color[1]/255, Main_Color[2]/255), interpolate=True, alpha=0.5)
    host.legend(prop=dict(weight='bold'))
    y_bars = host.get_yticklabels()
    
    for x_, y_bar in enumerate(y_bars, 1):
        y_bar.set_color((fix_color2(x_/len(y_bars))-0.1 ,0.5 , 1))
        y_bar.set_fontweight("bold")
    host.yaxis.label.set_color((0.85, 0, 1))
    #plt.autoscale(enable=True, axis='x', tight=True)
    byte_io = BytesIO()
    byte_io.seek(0)
    plt.savefig(byte_io, dpi=200, transparent=True, format='png', bbox_inches='tight')
    byte_io.seek(0)

    bg = Image.open(byte_io)
    ngb_logo = client.gb
    __x__, __y__ = bg.size
    bg.paste(ngb_logo, (__x__-33, __y__-33), ngb_logo)
            
    new_im = trim(bg)
    byte_io = BytesIO()
    byte_io.seek(0)
    new_im.save(byte_io, format='png')
    byte_io.seek(0)

    plt.clf()
    plt.cla()
    plt.close()

    tod = datetime.datetime.now()
    week_ago = tod - datetime.timedelta(days = 7);
    month_ago = tod - datetime.timedelta(days = 30);
    
    today_views = 0
    week_views = 0
    month_views = 0
    for e_d in data:
        that_day = datetime.datetime.fromtimestamp(int(e_d))
        if that_day.date() == tod.date():
            today_views += 1
        if that_day.date() > week_ago.date():
            week_views += 1
        if that_day.date() > month_ago.date():
            month_views += 1

    return byte_io, today_views, week_views, month_views

async def auto_post_embed():
    while True:
        with open(featured_maps_file, "rb") as file:
            old_data = pickle.load(file)
        maps = await await_get("https://api.krunker.io/maps?index=1")
        maps = json.loads(maps)['data']
        for e_map in maps:
            if e_map["map_name"].lower() not in old_data:
                print("A new featured map")
                
                map_name = e_map['map_name']
                data = await get_user_data(map_name, "map")
                raw_game = "Game Links: [Hub](https://krunker.io/social.html?p=map&q={}) | [Play](https://krunker.io/?play={})".format(requests.compat.quote_plus(e_map["map_name"]), requests.compat.quote_plus(e_map["map_name"]))
                if data[3]['vl']:
                    footer_t = "\n\n{}\nVideo showcase: https://youtu.be/{}".format(raw_game, data[3]['vl'])
                else:
                    footer_t="\n\n{}".format(raw_game)
                embed = discord.Embed(
                                      description=data[3]['map_description']+footer_t,
                                      timestamp=datetime.datetime.utcnow(),
                                      colour=discord.Colour(16760128))
        
                embed.set_image(url=map_thumb_url.format(data[3]['map_id']))
                embed.add_field(name="Map Name", value=e_map['map_name'])
                embed.add_field(name="Map Creator", value=e_map['creatorname'])
                date = data[3]["map_initialdate"][:10].split("-")
                embed.add_field(name="Publish Date", value="{} {} {}".format(str(date[2]), month[int(date[1])], date[0]).lower().title())
                embed.add_field(name="Likes", value=e_map['map_votes'])
                embed.add_field(name="Plays", value=e_map['map_pl'])
                embed.add_field(name="Version", value="v"+str(int(e_map['map_updatecounter'])/10))
                footer_t = "Play {} today! ".format(e_map['map_name'])
                embed.set_author(name= "{} • New Featured Game".format(e_map['map_name']), url="https://krunker.io/?play="+requests.compat.quote_plus(e_map["map_name"]), icon_url = "https://media.discordapp.net/attachments/723499834144981062/736169630686642186/Featured.png")
                embed.set_footer(text=footer_t)
                with open("Data/serverconf.bt", "rb") as file:
                    confs = pickle.load(file)
                for server_ids, server_conf in confs.items():
                    if server_ids == 484192043833491487:
                        embed.set_footer(text=footer_t, icon_url = "https://media.discordapp.net/attachments/575245857675542528/575742155977654292/MMOK_Logo.png?width=636&height=636")
                    else:embed.set_footer(text=footer_t)
                    
                    
                    try: await client.get_guild(server_ids).get_channel(server_conf['chl_id']).send(embed = embed)
                    except Exception as e:print(e)
                old_data.append(e_map["map_name"].lower())
                with open(featured_maps_file, "wb") as file:
                    pickle.dump(old_data, file)
        await asyncio.sleep(60*15)
                
async def auto_manage_servers():
    while True:
        await asyncio.sleep(60*35)
        await UpdateRolesNicks()

async def auto_change_status():
    await asyncio.sleep(15)
    statuses = {
        "{servers} Servers": "w",
        "with {servers} Servers": "p",
        "Krunker.io": "l",
        "g.patreon": "l",
        "g.invite": "l",
        "g.server": "l",
        "Giveaways @ g.server": "w",
        "g.help @ {servers} Servers": "l",
        "with members": "p",
        "commands": "w",
        "g.help @ {servers} Servers": "w",
        "with Gamebot Hub": "p",
        "g.find | Krunker Games": "l"
    }
    def get_corr(stat):
        return stat.replace("{servers}", str(len(client.guilds)))
    while True:
        stat = random.choice(list(statuses))
        act = statuses[stat]
        if act == "w":
            act_ = discord.Activity(type=discord.ActivityType.watching, name=get_corr(stat))
        elif act == "p":
            act_ = discord.Game(name=get_corr(stat))
        elif act == "l":
            act_ = discord.Activity(type=discord.ActivityType.listening, name=get_corr(stat))
        if not client.disable_status:
            await client.change_presence(status=client.bstatus,
                                         activity=act_)
        await asyncio.sleep(60*5)
client.disable_status = 0   
async def clear_update_cache():
    while True:
        try:
            new_update = await await_get("https://krunker.io/docs/versions.txt")
        except:
            await asyncio.sleep(int(60*1.5))
            continue
        if client.recent_update and new_update != client.recent_update:
            print("New krunker update")
            client.recent_update = new_update
            updates = client.recent_update.split("""
 == """)
            found_update = updates[5].split("\n", 1)[-1]
            status_ = str(updates[5].replace("UPDATE ", "").split("\n", 1)[0].split(" ", 1)[0].lower()).strip()
            embed=discord.Embed(colour=discord.Colour(14423783), title = "== UPDATE {} ==".format(status_))
            found_update = found_update.split("\n")
            while "" in found_update:found_update.remove("")
            main_updates = []
            if len(found_update) > 25:
                main_updates.append(found_update[:26])
                main_updates.append(found_update[26:])
            else:
                main_updates = [found_update]
            total_embeds = []
            for main_update in main_updates:
                total_lines = 0 
                for i, k in zip(main_update[0::2], main_update[1::2]):
                    embed.add_field(name = i.strip().replace("<br/>", "\u200b"), value = k.strip().replace("<br/>", "\u200b"), inline  = False)
                    total_lines += 2
                if total_lines != len(main_update):
                    embed.add_field(name = main_update[-1].strip().replace("<br/>", "\u200b"), value = "\u200b", inline  = False)
                embed.set_footer(text="Keep on Krunkin / Keep using gamebot", icon_url = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
                total_embeds.append(embed)
                embed=discord.Embed(colour=discord.Colour(14423783))
            '''for e_guild, e_chl in all_channels.items():
                for x, e_emb in enumerate(total_embeds):
                    try:
                        await client.get_guild(e_guild).get_channel(e_chl[0]).send(content = "" if x else e_chl[1], embed = e_emb)
                    except Exception as e:
                        print(e)'''
            for x, e_emb in enumerate(total_embeds):
                my_msg = await client.get_guild(708067789830750449).get_channel(799911466613342248).send(embed = e_emb)
                await my_msg.publish()

        else:
            client.recent_update = new_update
        await asyncio.sleep(int(60*1.5))
async def get_update_data():
    return client.recent_update




async def leak_updates():
    while True:
        try:
            new_update = await await_get("https://comp.krunker.io/docs/versions.txt")
        except:
            await asyncio.sleep(int(60*1.5))
            print("hmm")
            continue
        if client.update_leaks and new_update != client.update_leaks:
            print("New krunker leak")
            client.update_leaks = new_update
            updates = client.update_leaks.split("""
 == """)
            found_update = updates[5].split("\n", 1)[-1]
            status_ = str(updates[5].replace("UPDATE ", "").split("\n", 1)[0].split(" ", 1)[0].lower()).strip()
            embed=discord.Embed(colour=discord.Colour(14423783), title = "== LEAKED UPDATE {} ==".format(status_))
            found_update = found_update.split("\n")
            while "" in found_update:found_update.remove("")
            main_updates = []
            if len(found_update) > 25:
                main_updates.append(found_update[:26])
                main_updates.append(found_update[26:])
            else:
                main_updates = [found_update]
            total_embeds = []
            for main_update in main_updates:
                total_lines = 0 
                for i, k in zip(main_update[0::2], main_update[1::2]):
                    embed.add_field(name = i.strip().replace("<br/>", "\u200b"), value = k.strip().replace("<br/>", "\u200b"), inline  = False)
                    total_lines += 2
                if total_lines != len(main_update):
                    embed.add_field(name = main_update[-1].strip().replace("<br/>", "\u200b"), value = "\u200b", inline  = False)
                embed.set_footer(text="Keep on Krunkin / Keep using gamebot", icon_url = "https://cdn.discordapp.com/avatars/717416553099952219/0ada419dbd4b71306f13abfbc89ed1e0.png?size=1024")
                total_embeds.append(embed)
                embed=discord.Embed(colour=discord.Colour(14423783))
            all_channels = get_var("leak_chl")
            for e_guild, e_chl in all_channels.items():
                for x, e_emb in enumerate(total_embeds):
                    try:
                        await client.get_guild(e_guild).get_channel(e_chl).send(embed = e_emb)
                    except Exception as e:
                        print(e)

        else:
            client.update_leaks = new_update
        await asyncio.sleep(int(60*1.5))


        

@client.event
async def on_ready():

    print("Bot is up. Keep this window open")

    watching_ = "Updating..."
    
    await client.change_presence(status=client.bstatus, activity=discord.Game(name=watching_))

    client.loop.create_task(update_trigger())
    client.loop.create_task(auto_post_embed())
    client.loop.create_task(auto_manage_servers())
    client.loop.create_task(auto_change_status())
    print(watching_)
    
    

def change_color(r, g, b, img):
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]): # for every pixel:
        for j in range(img.size[1]):
            if list(pixels[i, j])[-1] != 0:
                pixels[i, j] = (r, g, b, list(pixels[i, j])[-1])
async def get_um(id_):
    if client.get_user(id_):
        return client.get_user(id_).mention
    try:
        my_req = await client.fetch_user(id_)
        return my_req.mention
    except:
        return None
async def get_u_(id_):
    if client.get_user(id_):
        return client.get_user(id_)
    try:
        return await client.fetch_user(id_)
    except:return None

async def connect_to_websocket():
    while True:
        ssl_context = ssl._create_unverified_context()
        client.ws = await websockets.connect(uri=client.uri, extra_headers = a_headers, ssl=ssl_context)
        print(client.ws.messages)
        await client.ws.keepalive_ping()
def work_skins(social_data, prices):
    #data = js2py.eval_js(social_data)["skins"]
    data = json.loads(social_data)["store"]["skins"]
    that_skin_name = ""
    for x, e_skin in enumerate(data):
        try:
            that_skin_name = e_skin["name"].lower()
            client.skins[that_skin_name]
            try:
                that_skin_name = e_skin["name"].lower() + " " + weapons[e_skin["weapon"]].lower()
                client.skins[that_skin_name] = e_skin
            except:
                that_skin_name = e_skin["name"].lower() + skin_types[e_skin["type"]].lower()
                client.skins[that_skin_name] = e_skin
                
        except:
            client.skins[e_skin["name"].lower()] = e_skin
        client.skins[that_skin_name]["avgPrice"] = prices[x]
        e_skin["i"] = x
        
async def get_new_ahk():
    while True:
        p = await await_get("https://krunker.io/social.html")
        social_data = p
        p = p.split("window.hcaptchaExpiredCallback=null)}}},function(e){e.exports=")[1].split("}")[0]
        #p = p[p.index(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")-10:p.index(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")+2]
        #p = p.split("=")[1].split("}")[0]
        client.ahk = int(p)
        print(p)
        configs = await await_get("https://social.krunker.io/hub-config")
        prices = json.loads(await await_get("https://api.krunker.io/prices"))
        thing = functools.partial(work_skins, configs, prices)
        with ThreadPoolExecutor(max_workers = 1) as executor:
            await client.loop.run_in_executor(executor, thing)
        await asyncio.sleep(60*5)

client.lobbies = []
async def get_lobbies():
    while True:
        try:
            lobby_data = await await_get(krunker_matchmaker_path)
        except:await asyncio.sleep(6);continue
        thing = functools.partial(json.loads, lobby_data)
        with ThreadPoolExecutor(max_workers = 1) as executor:
            client.lobbies = (await client.loop.run_in_executor(executor, thing))["games"]
        await asyncio.sleep(6)

def sync_manage_host_cache():
    games_o = {}
    for e_map in client.lobbies:
        try:
            games_o[e_map[-1]["i"].lower()]
        except:
            games_o[e_map[-1]["i"].lower()] = [0, 0]
        games_o[e_map[-1]["i"].lower()][0] += e_map[2]
        games_o[e_map[-1]["i"].lower()][1] += 1
    for e_game, game_data in games_o.items():
        try:
            client.hosting_cache[e_game] += [game_data + [int(time.time())]]
        except:
            client.hosting_cache[e_game] = [game_data + [int(time.time())]]
        if len(client.hosting_cache[e_game]) >= 100:
            del client.hosting_cache[e_game][0]
    

    
async def track_lobbies():
    await asyncio.sleep(10)
    while True:
        thing = functools.partial(sync_manage_host_cache)
        with ThreadPoolExecutor(max_workers = 1) as executor:
            await client.loop.run_in_executor(executor, thing)
        await asyncio.sleep(30)
        

def sync_get_lobby(code):
    for e_game in client.lobbies:
        if e_game[0].lower() == code.lower():
            return e_game
    return {"error":1}

async def async_get_lobby(code):
    thing = functools.partial(sync_get_lobby, code)
    with ThreadPoolExecutor(max_workers = 1) as executor:
        return await client.loop.run_in_executor(executor, thing)

def sync_load_file(file_name):
    with open(file_name, "rb") as file:
        return pickle.load(file)

async def async_open(file_name):
    thing = functools.partial(sync_load_file, file_name)
    with ThreadPoolExecutor(max_workers = 1) as executor:
        return await client.loop.run_in_executor(executor, thing)
    

async def control_cache():
    while True:
        await asyncio.sleep(60*1)
        if client.scache:
            async with aiofiles.open("Data/cache.bt", "wb") as file:
                await file.write(pickle.dumps(client.scache))
async def control_imp():
    while True:
        await asyncio.sleep(30)
        if client.simpressions:
            async with aiofiles.open("Data/impressions.bt", "wb") as file:
                await file.write(pickle.dumps(client.simpressions))
                
                
async def clear_smart_cache(user_n):
    await asyncio.sleep(25)
    try:
        client.pre_cached.remove(user_n.lower())
    except:pass
    
client.scache = {}
client.simpressions = {}
client.pre_cached = []
client.skins = {}
client.hosting_cache = {}
client.gamelinks = {}
client.bstatus = discord.Status.online

@client.event
async def on_connect():
    print("Connected")
    client.paused_error = warning + " This command has been **temporarily disabled**. Please try later."
    client.recent_update = ""
    client.update_leaks = ""
    
    
    #client.uri = "wss://social.krunker.io/ws"
    client.uri = "wss://krunker_social.krunker.io/ws"
    #client.uri = "wss://krunker_social_beta.krunker.io/ws"

    #client.uri = "wss://social_beta.krunker.io/ws"
    
    if not client.connected_:
        try:
            async with aiofiles.open("Data/cache.bt", "rb") as file:
                client.scache = pickle.loads(await file.read())
            print("Cache Loaded")
        except Exception as e:print("Cache load error")
        try:
            async with aiofiles.open("Data/impressions.bt", "rb") as file:
                client.simpressions = pickle.loads(await file.read())
            print("Impressions Loaded")
        except Exception as e:print("Impression load error ", e)
        client.launch_time = datetime.datetime.utcnow()
        client.loop.create_task(clear_update_cache())
        client.loop.create_task(leak_updates())
        client.loop.create_task(control_cache())
        client.loop.create_task(control_imp())
        client.loop.create_task(get_lobbies())
        client.loop.create_task(track_lobbies())
        
        client.connected_ = True
        client.prank = 0
        client.pranked = "Sidney" # guy getting pranked
        client.ahk = 0
        await compile_bgs()
        client.loop.create_task(get_new_ahk())
        client.is_operating = {}
        client.promoted = []
        font_offset = 0
        client.font = ImageFont.truetype(font_file, 13+font_offset)
        client.font15 = ImageFont.truetype(font_file, 15+font_offset)
        client.font4 = client.font16 = ImageFont.truetype(font_file, 16+font_offset)
        client.main_font = ImageFont.truetype(font_file, 17+font_offset)
        client.font18 = ImageFont.truetype(font_file, 18+font_offset)
        client.main_font2 = ImageFont.truetype(font_file, 23+font_offset)
        client.main_font3 = ImageFont.truetype(font_file, 20+font_offset)
        client.font2 = ImageFont.truetype(font_file, 22+font_offset)
        client.font3 = ImageFont.truetype(font_file, 10+font_offset)
        client.font5 = ImageFont.truetype(font_file, 11+font_offset)
        client.font6 = ImageFont.truetype(font_file, 12+font_offset)
        client.unicode_font = ImageFont.truetype("Data/unifont.ttf", 24)
        client.country_sheet = Image.open("Data/flags.png")
        client.partn = Image.open("Data/partner1.png", "r").convert("RGBA")
        client.partn.thumbnail((30, 30), Image.ANTIALIAS)
        client.partn2 = Image.open("Data/partner2.png", "r").convert("RGBA")
        client.partn2.thumbnail((30, 30), Image.ANTIALIAS)
        client.dropshadowoutline = Image.open("Data/odropshadow.png", "r").convert("RGBA")
        client.outlining = Image.open("Data/outline.png", "r").convert("RGBA")
        client.verif = Image.open("Data/verif.png","r").convert("RGBA")
        client.verif.thumbnail((30, 30), Image.ANTIALIAS)
        
        client.glowing = Image.open("Data/skin_assets/glowing.png","r").convert("RGBA")
        client.animated = Image.open("Data/skin_assets/animated.png","r").convert("RGBA")
        client.limited = Image.open("Data/skin_assets/limited.png","r").convert("RGBA")
        client.skin_mask = Image.open("Data/skin_assets/skin_mask.png","r").convert("L")
        client.inv_mask = Image.open("Data/skin_assets/inv_mask.png","r").convert("L")
        client.skin_rainbow = Image.open("Data/skin_assets/skin_rainbow.png","r").convert("RGBA")
        client.inv_rainbow = Image.open("Data/skin_assets/inv_rainbow.png","r").convert("RGBA")
        client.tag_background = Image.open("Data/skin_assets/tag_background.png","r").convert("RGBA")
        client.tag_rainbow = Image.open("Data/skin_assets/tag_rainbow.png","r").convert("RGBA")
        client.seasons = {
            0: Image.open("Data/skin_assets/s0.png","r").convert("RGBA"),
            1: Image.open("Data/skin_assets/s1.png","r").convert("RGBA"),
            2: Image.open("Data/skin_assets/s2.png","r").convert("RGBA"),
            3: Image.open("Data/skin_assets/s3.png","r").convert("RGBA"),
            4: Image.open("Data/skin_assets/s4.png","r").convert("RGBA"),
        }
        
        client.verif2 = Image.open("Data/verif.png","r").convert("RGBA")
        client.verif2.thumbnail((25, 25), Image.ANTIALIAS)
        client.kr = Image.open("Data/kr.png","r").convert("RGBA").resize((23, 23))
        client.twitch = Image.open("Data/twitch.png","r").convert("RGBA")
        client.speech = Image.open("Data/speech.png","r").convert("RGBA")
        client.discord = Image.open("Data/discord.png","r").convert("RGBA")
        client.unknown = Image.open("Data/unknown.png").convert("RGBA")
        client.unknown = client.unknown.resize((int(21*(client.unknown.width/client.unknown.height)),21)).convert("RGBA")
        client.overlay = Image.open("Data/stat_background.png","r").convert("RGBA")
        client.prem = Image.open("Data/prem.png","r").convert("RGBA")
        client.prem.thumbnail((30, 30), Image.ANTIALIAS)
        client.inf = Image.open("Data/infect.png","r").convert("RGBA")
        client.inf.thumbnail((30, 30), Image.ANTIALIAS)
        client.staff_ = Image.open("Data/staff.png", "r").convert("RGBA")
        client.staff_.thumbnail((30, 30), Image.ANTIALIAS)
        change_color(gb_all_colors[0][0], gb_all_colors[0][1], gb_all_colors[0][2], client.staff_)
        client.patron = Image.open("Data/patreon.png", "r").convert("RGBA")
        client.patron.thumbnail((30, 30), Image.ANTIALIAS)
        client.boost = Image.open("Data/boost.png", "r").convert("RGBA")
        client.boost.thumbnail((30, 30), Image.ANTIALIAS)
        client.sboost = Image.open("Data/single_boost.png", "r").convert("RGBA")
        client.sboost.thumbnail((30, 30), Image.ANTIALIAS)
        client.kdev = Image.open("Data/dev.png", "r").convert("RGBA")
        client.kdev.thumbnail((30, 30), Image.ANTIALIAS)
        client.gb = Image.open("Data/logo.png","r")
        client.loadn = Image.open("Data/loading.png","r")
        client.defloadn = Image.open("Data/loading2.png","r")
        client.dropshadow = Image.open("Data/shadow2.png","r").convert("RGBA")
        client.default_bg = [Image.open("Data/backgrounds/dtemp1.png"), Image.open("Data/backgrounds/dtemp2.png")]
        client.icons = {}
        client.ranks = {}
        client.levels = {}
        client.icon_mask = Image.open("Data/ranks/icon_mask.png").convert('L')
        client.icon_mask2 = Image.open("Data/ranks/icon_mask.png").convert('L').resize((207-4,207-4))
        client.official_maps = ['newtown', 'littletown', 'kanji', 'sandstorm', 'subzero', 'oasis', 'burg', 'freight', 'lostworld', 'citadel', 'undergrowth', 'shipyard', 'industry', "evacuation", "soul sanctum", "site"]
        for ind in range(17):
            if not os.path.exists("Data/ranks/icon_{}.png".format(ind)):
                response = requests.get("https://assets.krunker.io/textures/classes/icon_{}.png".format(ind))
                try:
                    thumb = Image.open(BytesIO(response.content)).convert("RGBA")
                except:break
                profile_icon = thumb.resize((107,107), resample=Image.BOX)
                profile_icon.save("Data/ranks/icon_{}.png".format(ind))
            client.icons[ind] = Image.open("Data/ranks/icon_{}.png".format(ind)).convert("RGBA")
        for ind in range(10):
            if not os.path.exists("Data/ranks/rank_{}.png".format(ind)):
                response = requests.get("https://krunker.io/img/ranks/icon_{}.png".format(ind))
                try:thumb = Image.open(BytesIO(response.content)).convert("RGBA")
                except:break
                thumb.thumbnail((40, 40), Image.ANTIALIAS)
                thumb.save("Data/ranks/rank_{}.png".format(ind))
            client.ranks[ind] = Image.open("Data/ranks/rank_{}.png".format(ind)).convert("RGBA")
        for ind in range(1, 102, 2):
            if not os.path.exists("Data/levels/{}.png".format(ind)):
                continue
                try:
                    response = requests.get("https://krunker.io/img/levels/{}.png" .format(ind))
                except:
                    print("404", ind);continue
                try:thumb = Image.open(BytesIO(response.content)).convert("RGBA")
                except:continue
                thumb.thumbnail((40, 40), Image.ANTIALIAS)
                thumb.save("Data/levels/{}.png".format(ind))
            client.levels[ind] = Image.open("Data/levels/{}.png".format(ind)).convert("RGBA")
        

        client.compiled_chls = compile_channels()
        client.compiled_cmds = compile_cmds()
        await compile_bgs()
        print("Resources loaded")
        #await connect_to_websocket()
        #print("Connected to websocket")
with open("token.bt", "r") as file:
    client.run(file.read())
