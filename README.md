# forza-painter
![](/imgs/ayylmao.png)
```
Discord: A-Dawg#0001 (AE)
Supports: Forza Horizon 5
Offically (OTHER v1.405.2.0, MS STORE v3.414.967.0, STEAM v1.414.967.0)
Unofficially (most versions should work)
License: MIT
```

# NEW
We now include `forza-painter-geometrize`. This is a modified `geometrize-lib` that will support transparent images.

### KNOWN ISSUES (None right now!):
Please ask for help on the discord (https://discord.gg/BJNFCxPKhu) or contact me directly if I'm available `A-Dawg#0001`

### What is this for?:
Image → Geometrize → Forza Horizon 5 (Vinyl Group)

### Does this work for the Steam version or the Microsoft Store version?
It now supports both! And it should work for older and future releases too thanks to pattern scanning.

### How does it work?:
Geometrize breaks the images down into shapes and can export a `.json` data file.

`forza-painter` deserializes this `.json` data file and uses some math, reverse engineering and the Windows API to push these shapes into FH5 automagically.

# READ EVERYTHING BELOW BEFORE ASKING FOR HELP

## Requirements
- Geometrize (https://www.geometrize.co.uk/)
- python 3.9 64-bit (recommend downloading from the **Microsoft Store** as it automatically adds to PATH)
- The below python packages (just install from the command line):
```
pip install psutil
pip install pywin32
pip install opencv-python
```

# FAQ:
- **Will this get me banned!?**
```
To preface this:
I take no responsibility for your use of this software.

You may be reported by players if you share the vinyls as they are extremely
detailed. Some players feel that making vinyl groups in this way is unfair as
they have had to suffer through learning the tool and were not able to use an
easy starting point.

This is a completely valid opinion, and with enough time, practice and talent
you CAN recreate extremely complex images. I just don't share the opinion that
you should have to.

As for FH5 detecting this; It is not a "cheat", it is not giving any player
an unfair advantage, it is not modifying game files or game code, and it is
not taking advantage of any exploits.

Interpret that as you feel. I believe this is a missing necessary feature
from the vinyl group designer.
```
- **My version is older/newer or it isn't working following the steps!**
```
For unsupported versions, forza-painter will scan for a known pattern.
If it fails to find this pattern, it will notify you.
Most versions should work fine, but others may need tweaking.
```
- **Will you update this to support newer versions?**
```
It should automatically support newer versions providing the memory structures remain similar.
In the event of it failing on a new version I will revise the code.
```
- **I have an error that I don't understand...**
```
Check the requirements above.
Ensure you have python 3.9 or later installed (make sure it is 64-bit) by running
`python` from the command prompt and that you have installed the python packages.
If you can't manage this, I probably can't help you.
If you are still having problems, contact me on Discord if you wish.
```
- **Can you make a version that just uses inputs to create the shapes?**
```
I can, but I won't. I've open sourced this for a reason.
Feel free to take it and make changes as you wish as permitted by the MIT licence.
Just throw me [A-Dawg#0001 (AE)] a little credit.
```
- **My issue is not listed**
```
Feel free to create an issue or contact me on Discord A-Dawg#0001
```
- **It just says: "Press any key to continue"**
```
Did an image pop up?
    Yes - Is it still up?
            Yes - Click it then press a key
            No - Make sure you are in the Vinyl Group Editor, not the Livery Editor for example
    No - You likely don't have python installed properly, INSTALL IT FROM THE MICROSOFT STORE
```

# Basic usage guide:

## Making your template Vinyl Groups (reuse these)
- Open Forza Horizon 5 and create a new Vinyl Group.
- Just make one sphere and duplicate it for as many layers as you need. Color, size, scale, etc. **DO NOT MATTER**.
- Save this as a template as something identifiable e.g. `forza-painter 3000 shapes`.

Note: When you load these templates the shapes will be **grouped**, make sure you select them and **UNGROUP** before using.

## Using `forza-painter` to recreate the `.json` file (from Geometrize) in Forza Horizon 5:
- First generate the `.json` file in Geometrize (see below steps).
- Open a template with the number of shapes (all spheres) that you desire to represent your geometry (see above steps) then **UNGROUP** it.
    - e.g. if you load 500 spheres and ungroup, it will only use those 500 spheres
- Finally, just drag the `.json` geometry onto the `drag_geometry_file_here.bat` batch script, python will do the rest.

## Using `forza-painter-geometrize`(NEW) to generate your `.json` geometry (For images with transparency):
- Just drag an image onto `forza-painter-geometrize.exe` and it will start
- It will generate a `.json` file with the same name and the same folder as the image you dragged in.
- It will save every 10 shapes, allowing you to drag your `.json` file onto `drag_geometry_file_here.bat` to preview it. (the game does not need to be running)
- Once you are happy with the amount of shapes (or the quality of the preview) just close the window (as it has saved every 10 shapes already).

## Using Geometrize to generate your `.json` geometry (For images without transparency):
- First **Disable Image Downscaling** in `File → Global Preferences → Performance`
    - Alternatively, if the process is too slow, you can enable it, but set the `Max Width/Height`. You will be sacrificing quality for speed though.

![](/imgs/001-global-settings.png)
- Then after loading any image, use the below settings:

![](/imgs/002-image-settings.png)
- Wait for the number of shapes you want to target (1000, 3000 or something smaller if you wish).
- Finally click the `Exporters` tab at the bottom of the panel and select `Save Geometry Data`

![](/imgs/003-exporter-settings.png)

# Acknowledgements
geometrize-lib - Sam Twidale (https://samcodes.co.uk/)
Primitive library - Michael Fogleman (https://github.com/fogleman/primitive)
