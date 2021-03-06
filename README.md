# spoofybadge

A simple python script that uses the Spotify API to generate a bitmap from "currently-playing" data.

The idea is that you can customize the ImageMagick parameters, and create an electronic badge, say on a [eink Display Hat](https://www.adafruit.com/product/3934)

---

![Example Badge](badge.png)

## Usage
Firstly, you need to download or clone this repository
```
git clone https://github.com/reckoncrafter/spoofybadge.git
```

You'll want to login to your spotify at [developer.spotify.com](developer.spotify.com), then get your OAuth key from [here](https://developer.spotify.com/console/get-users-currently-playing-track/)

Copy that key, and paste it into a file called OAUTH, e.g
```
echo "0aUtH-k3y-G0e5-hE4e" > OAUTH
```

Run the script from your command line
```
python3 main.py
```
## Dependencies

This script relies on Wand, an ImageMagick wrapper for python (v 0.6.7+)
```
python3 -m pip install wand
```
:warning: Warning! If on Debian/Ubuntu, do not install wand from `apt`, the apt repository version is wildly out of date and will not work!

## Changing Parameters

I plan on implementing command line options, but if you want to change the font, add the absolute path to
```
draw.font = ""
```
at line `57`

line `55` onwards has all the ImageMagick commands, so feel free to adjust those.
