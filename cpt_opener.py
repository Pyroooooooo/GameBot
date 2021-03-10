#!/usr/bin/python
import threading, os, time
from subprocess import call
#os.environ["PATH"] = "C:/ProgramFiles/nodejs"
def exec_cmd():
    #call('r"C:/Program Files/nodejs/node.exe" "C:/Users/Administrator/Downloads/bot/bot/cpt/index.js"', shell=True)
    #os.system("start cpt/index-win.exe")
    os.system("C:/Users/Administrator/Downloads/bot/bot/cpt/index-win.exe")
    #os.system("cpt_opener.bat")
    #call("node C:/Users/Administrator/Downloads/bot/bot/cpt/index.js", shell=True)
threading.Thread(target = exec_cmd).start()
for _ in range(15):
    if os.path.exists("done.response"):break
    time.sleep(1)
if os.path.exists("done.response"):
    os.remove("done.response")
exit()
