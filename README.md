# GameBot
The best [Krunker.io](https://krunker.io) Discord bot!

## Features
GameBot includes many commands for [Krunker.io](https://krunker.io).
Its prefix is `g.`
Here is a small list including *some* of its commands:
### Profile
```css
g.pf <kr-username
g.link <kr-username>
g.maps <kr-username>
g.mods <kr-username>
g.assets <kr-username>
g.cstats <kr-username>
g.posts <kr-username>
g.stats
```
### Account Linking & Background
```css
g.link <kr-username>
g.unlink <kr-username>
g.incognito
g.alts
g.alts set
g.pbg <user-name>
g.cbg <clan-name>
```
### Maps
```css
g.map <map-name>
g.online [kr-username]
g.favs <kr-username>
g.search <keyword>
g.theme
```
### Servers
```css
g.find [map-name] [-u] [-p] [-mp <val>] [-vs <val>]
g.online
g.gameinfo <game-url>
g.popular
g.featured
```
### Map Editing
```css
g.editor
g.layout
g.editor help
```
### Leaderboards & Skins
```css
g.leaders <key> key: [level][kills][wins][time][kr][clans][1v1][2v2][4v4][challenge][egg][wars]
g.skin <skin-name> [-t]
g.owners <skin-name>
```
### Clans & Others
```css
g.clan <clan-name>
g.wars [clan-name] [region:<re>]
g.leaders wars
g.applications
g.apply <kr-username>
g.mod <mod-name>
g.asset <asset-name>
g.hub <name>
g.class <class-name>
g.update [version]
```
### Graphs & Sweeps
```css
g.reg <kr-username>
g.graph <map-name>
g.sweeper help
```
### Fun Stuff
```css
g.reply <msg>
g.cat
g.dog
g.bird
g.joke
g.meme
g.tinyurl <url>
```
### Server Management
```css
g.set_chl <#channel>
g.list_chl
g.auto_manage help
g.levels
g.auto_updates #<channel>
```
### Utility
```css
g.staff
g.invite
g.patreon
g.ping
g.help
g.help <module>
g.full_help
```
`Syntax: <> required, [] optional`
## How to install and run the bot
1. Make sure you have [python3](https://www.python.org/download/releases/3.0/) installed
2. Make sure you have [git](https://git-scm.com/) installed, or you can download this repository as a zip instead.
### Installation
With Git:
```sh
git clone https://github.com/39x/GameBot.git
```
then enter the directory with `cd GameBot`

Install Dependencies:
```sh
python3 -m pip install -r requirements.txt
``` 
You might have to manually install some dependencies with `python3 -m pip install <dependency>`
### Running the code
To run the code, make sure you [python3](https://www.python.org/download/releases/3.0/) installed like I said before. Then use
```sh
python3 main.py
```
to run the code.

## License
This code is under the [MIT license](https://opensource.org/licenses/MIT)
```
MIT License

Copyright (c) 2021 39x

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```