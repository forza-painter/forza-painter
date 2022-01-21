# forza-painter
![](/imgs/ayylmao.png)
```
Discord: A-Dawg#0001 (AE)
Supports: Forza Horizon 4 and 5
Offically: MS Store/XBOX PC App (latest versions), Steam (latest versions).
Unofficially: Every version that isn't running on a console of via cloud gaming should work.
License: MIT
```

# NEW
#### Now supports multiple images being dragged in to queue them up.
#### Final masking shapes are now removed automatically if unnecessary (per side)
### Now supports Forza Horizon 4!
### `Python` and `Geometrize` are both no longer needed, see updated guides below!
### Want to support the tool with money? Donate to charity instead (https://www.charitywatch.org/top-rated-charities)

# Info
### KNOWN ISSUES (None right now!):
Please ask for help on the discord
- https://discord.gg/BJNFCxPKhu


If you **cannot get help** on the Discord server, you can contact me directly (if I'm available)
- `A-Dawg#0001`

### What is this for?:
Any image → Forza Horizon 4 or 5 (Vinyl Group)

### Does this work for the Steam versions or the Microsoft Store versions?
It supports both! And it should work for older and future releases too thanks to pattern scanning.

### How does it work?:
When you drag one or multiple images onto `forza-painter.exe`; It will break the image(s) down into shapes and store them in `.json` data files.
Then you drag those `.json` data files onto `forza-painter.exe`; It deserializes this `.json` and uses some math, reverse engineering and the Windows API to push these shapes into FH5 automagically.

# READ EVERYTHING BELOW BEFORE ASKING FOR HELP

## Requirements
- Microsoft Visual C++ 2015 Redistributable (Download both x86 and x64):
    - https://www.microsoft.com/en-us/download/details.aspx?id=53587

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

# Basic usage guide:

## Making your template Vinyl Groups (reuse these)
- Open Forza Horizon 5 and create a new Vinyl Group.
- Just make one sphere and duplicate it for as many layers as you need. Color, size, scale, etc. **DO NOT MATTER**.
    - Tip (Optional): You can make (cut/insert) ~100 then select an existing shape, select highlight all, copy and insert these 100 over and over.
    - Tip (Optional): Another trick is to save one vinyl group with 6 groups of 500 spheres. Simply load it and delete the ones you don't want (e.g. to reduce it down to 2000 shapes, delete 2 of them), then ungroup.
- Save this as a template, as something identifiable, e.g. `forza-painter 3000 shapes`.

Note: When you load these templates the shapes will be **grouped**, make sure you select them and **UNGROUP** before using (If you miss one it will tell you).

## Using `forza-painter` to generate your `.json` geometry (NEW):
- Just drag one or multiple images onto `forza-painter.exe` and it will start
- It will generate a `.json` file with the same name and the same folder as the image(s) you dragged in. (most profiles will also save one every 500 shapes separately)
- You can close the window at any time when you are happy or if the shapes are complete.
- If more than one image is dragged in, it will queue them, completing them one by one.
- **Advanced Users:** Consider tweaking the profiles in the `settings` folder and share them with other users. See #faq on the Discord for more info.

# Acknowledgements
- geometrize-lib - Sam Twidale (https://samcodes.co.uk/)
- Primitive library - Michael Fogleman (https://github.com/fogleman/primitive)
