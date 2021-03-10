from selenium import webdriver
import pickle
import os, zipfile
#cookies = pickle.load(open("cookies.pkl", "rb"))
#print(cookies)
from selenium.webdriver.chrome.options import Options


ext_dir = r'D:\poll bot\bot\bot\extension.crx'
ext_file = r'D:\poll bot\bot\bot\extension.zip'

'''# Create zipped extension
## Read in your extension files
file_names = os.listdir(ext_dir)
file_dict = {}
for fn in file_names:
    with open(os.path.join(ext_dir, fn), 'r') as infile:
        file_dict[fn] = infile.read()

## Save files to zipped archive
with zipfile.ZipFile((ext_file), 'w') as zf:
    for fn, content in file_dict.iteritems():
        zf.writestr(fn, content)'''

# Add extension
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
#chrome_options.add_extension(ext_dir)
chrome_options.add_argument("--disable-features=RendererCodeIntegrity")



driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://krunker.io/social.html?p=profile&q=BlAcKThNdER")
input("=> Ready?")
#print(driver.get_cookies())
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
print(cookies)
agent = driver.execute_script("return navigator.userAgent")
print(agent)
input("--->")
from time import sleep
sleep(30)

# directly print the value

'''
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://Google.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie({
        'name': cookie["name"], 
        'value': cookie["value"],
        'domain': cookie["domain"]
    })
from time import sleep
def get_map_data(username, type_ = None):
    driver.get("https://krunker.io/social.html?p=profile&q="+username)
    sleep(1)
    
    def get_(xp):
        return driver.find_element_by_xpath(xp)
    try:
        frame = get_("//iframe[contains(@title, 'hCaptcha')]")
        driver.switch_to.frame(frame)
        sleep(2)
        get_("//div[@id='checkbox']").click()
        driver.switch_to.default_content()
        sleep(1.5)
    except Exception as e:print(e)
    if True:
        try:
            clan = get_('//div[@class="profileName"]/a').text
        except:clan = None
        
        try:verified = get_("//i[@class='material-icons' and contains(text(), 'check_circle')]").text
        except:verified = None
        
        try:premium = get_("//i[@class='material-icons' and contains(text(), 'beenhere')]").text
        except:premium = None
        
        try:partner = get_("//div[@class='rainbowText']").text
        except:partner = None
        
        lvl = get_('//div[@class="pSt"]/strong').text
        challenge = get_('(//div[@class="pSt"])[2]/strong').text
        kr = get_('(//div[@class="pSt"])[3]/strong').text
        score = get_('(//div[@class="pSt"])[4]/strong').text
        spk = get_('(//div[@class="pSt"])[5]/strong').text
        kills = get_('(//div[@class="pSt"])[6]/strong').text
        deaths = get_('(//div[@class="pSt"])[7]/strong').text
        kdr = get_('(//div[@class="pSt"])[8]/strong').text
        kpg = get_('(//div[@class="pSt"])[9]/strong').text
        wins = get_('(//div[@class="pSt"])[12]/strong').text
        loses = get_('(//div[@class="pSt"])[13]/strong').text
        nukes = get_('(//div[@class="pSt" and contains(text(), "Nukes")])/strong').text
        melees = get_('(//div[@class="pSt" and contains(text(), "Melee")])/strong').text
        headshots = get_('(//div[@class="pSt" and contains(text(), "Head")])/strong').text
        wallbangs = get_('(//div[@class="pSt" and contains(text(), "Wall")])/strong').text
        accuracy = get_('(//div[@class="pSt" and contains(text(), "Accu")])/strong').text

        #return 
        get_("//div[@id='pTab_maps']").click()
        maps = []
        try:
            get_('(//div[contains(text(), "No published maps")])')
        except:
            for e_map in range(len(driver.find_elements_by_xpath("//div[@id='pTabContent_maps']/div"))):
                maps.append([get_("(//div[@id='pTabContent_maps']/div)[{}]//a".format(e_map+1)).text,
                             get_("(//div[@id='pTabContent_maps']/div)[{}]//div[@class='mapsVotes']".format(e_map+1)).text.replace("thumb_up", "")])

         
        get_("//div[@id='pTab_mods']").click()
        mods = []
        try:
            get_('(//div[contains(text(), "No published mods")])')
        except:
            for e_mod in range(len(driver.find_elements_by_xpath("//div[@id='pTabContent_mods']/div"))):
                mods.append([get_("(//div[@id='pTabContent_mods']/div)[{}]//a".format(e_mod+1)).text,
                             get_("(//div[@id='pTabContent_mods']/div)[{}]/div[2]".format(e_mod+1)).text.replace("thumb_up", "")])
            
        return clan, lvl, challenge, kr, score, spk, kills, deaths, kdr, kpg, wins, loses, maps, mods
    
while True:
    try:print(get_map_data(input("Username? => ")))
    except Exception as e:print(e)
'''
