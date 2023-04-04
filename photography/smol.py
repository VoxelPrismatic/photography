import os
import ffmpeg #ffmpeg-python
import argparse

# Get target folder
parser = argparse.ArgumentParser()
parser.add_argument("target", nargs = "+")
parser.add_argument("-n", default = False, action = "store_true")
args = parser.parse_args()

# Start converting
ls = []
for t in args.target:
    for f in os.listdir(t):
        if f.endswith("-smol.webp") or f.endswith("-med.webp"):
            continue
        ls.append(t + "/" + f)
m = 0
l = len(ls)
print()
if args.n:
    y = "n"
else:
    y = "y"

for f in ls:
    m += 1
    print(f"\x1b[1A\x1b[K{f} [{m}/{l} {(m*3)/(l*3)*100:.2f}%] .")
    p = ffmpeg.probe(f)
    h = p["streams"][0]["height"]
    w = p["streams"][0]["width"]
    n = 8
    o = 2
    while h/n > 480 or w/n > 480:
        n += 1
    while h/o > 2048 or w/o > 2048:
        o += 1
    print(f"\x1b[1A\x1b[K{f} [{m}/{l} {(m*3+1)/(l*3)*100:.2f}%] :")
    os.system(f"ffmpeg -i \"{f}\" -vf scale={w/n:.0f}:{h/n:.0f} \"{f}-smol.webp\" -{y} 2> /dev/null")
    print(f"\x1b[1A\x1b[K{f} [{m}/{l} {(m*3+2)/(l*3)*100:.2f}%] |")
    os.system(f"ffmpeg -i \"{f}\" -vf scale={w/o:.0f}:{h/o:.0f} \"{f}-med.webp\" -{y} 2> /dev/null")
