# forza-painter
![](/imgs/ayylmao.png)
```
Discord: A-Dawg#0001 (AE)
Supports: Forza Horizon 5
Offically: MS Store/XBOX PC App (latest version), Steam (latest version).
Unofficially: Every version that isn't running on a console of via cloud gaming should work.
License: MIT
```

# NEW
### `Geometrize` is no longer needed, see updated guides below!
### Want to support the tool with money? Donate to charity instead (https://www.charitywatch.org/top-rated-charities)

# Info
### KNOWN ISSUES (None right now!):
Please ask for help on the discord
- https://discord.gg/BJNFCxPKhu


If you would like, you can contact me directly if I'm available on Discord
- `A-Dawg#0001`

### What is this for?:
Any image → Forza Horizon 5 (Vinyl Group)

### Does this work for the Steam version or the Microsoft Store version?
It supports both! And it should work for older and future releases too thanks to pattern scanning.

### How does it work?:
When you drag an image onto `drag_image_file_here.bat`; It will break the image down into shapes and store them in `.json` data files.
Then you drag those `.json` data files onto `drage_geometry_json_here.bat`; It deserializes this `.json` and uses some math, reverse engineering and the Windows API to push these shapes into FH5 automagically.

# READ EVERYTHING BELOW BEFORE ASKING FOR HELP

## Requirements
- python 3.8 or 3.9 (or later**\***) 64-bit (Make sure to tick `Add to PATH` during installation. Microsoft Store installation does this automatically.)
- The below python packages (just install from the command line):
**\****If you are using python 3.10 or later you have to install `psutil` from https://pypi.org/project/psutil-wheels/*
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
Ensure you have python 3.8 or later installed (make sure it is 64-bit) by running
`python` from the command prompt. Check that you have installed the python packages (pip commands at top of readme)
If you are still having problems, join the discord (top of readme) and ask for help in #support
```
- **Can you make a version that just uses inputs to create the shapes?**
```
I can, but I won't. I've open sourced this for a reason.
Feel free to take it and make changes as you wish as permitted by the MIT license.
Just throw me [A-Dawg#0001 (AE)] a little credit.
```
- **My issue is not listed**
```
Join the discord (at top of readme) and ask for help in #support, failing that, contact me on Discord. A-Dawg#0001
```
- **It just says: "Press any key to continue"**
```
Did an image pop up?
    Yes - Is it still up?
            Yes - Click it then press a key
            No - Make sure you are in the Vinyl Group Editor, not the Livery Editor for example
    No - You likely don't have python installed properly (Make sure to tick `Add to PATH` or just install from Microsoft Store)
```

# Basic usage guide:

## Making your template Vinyl Groups (reuse these)
- Open Forza Horizon 5 and create a new Vinyl Group.
- Just make one sphere and duplicate it for as many layers as you need. Color, size, scale, etc. **DO NOT MATTER**.
    - Tip (Optional): You can make, say, 100 then select an existing shape, select highlight all, copy and insert these 100 over and over.
    - Tip (Optional): Another trick is to save one vinyl group with 6 groups of 500 spheres. Simply load it and delete the ones you don't want (e.g. to reduce it down to 2000 shapes, delete 2 of them), then ungroup.
- Save this as a template, as something identifiable, e.g. `forza-painter 3000 shapes`.

Note: When you load these templates the shapes will be **grouped**, make sure you select them and **UNGROUP** before using (If you miss one it will tell you).

## Using `forza-painter-geometrize` to generate your `.json` geometry (NEW):
- Just drag an image onto `drag_image_file_here.bat` and it will start
- It will generate a `.json` file with the same name and the same folder as the image you dragged in. (most profiles will also save one every 500 shapes separately)
- You can close the window at any time when you are happy or if the shapes are complete.
- **Advanced Users:** Consider tweaking the profiles in the `settings` folder and share them with other users.

# Acknowledgements
- geometrize-lib - Sam Twidale (https://samcodes.co.uk/)
- Primitive library - Michael Fogleman (https://github.com/fogleman/primitive)
