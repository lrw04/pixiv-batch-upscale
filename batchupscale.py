from pathlib import Path
from subprocess import run
from sys import argv
from config import WAIFU2X
import util
import shutil

def doubleimg(img: Path):
    tmpname = 'tmp' + img.suffix
    run([WAIFU2X, '-s', '2', '-i', str(img), '-o', tmpname])
    shutil.copy(tmpname, img)

img = Path(argv[1])
lst = Path(argv[2])
out = Path(argv[3])
minsize = int(argv[4])

images = dict()

for dir in img.iterdir():
    if not dir.is_dir():
        continue
    for f in dir.iterdir():
        if not f.is_file():
            continue
        images[util.get_pid(f.parts[-1])] = str(f)

for k in sorted(images.keys()):
    print(k[0], k[1], images[k])

with open(lst, 'r') as f:
    for l in f.readlines():
        ind = tuple(l.strip().split(','))
        p = Path(images[ind])
        if not (out / p.parts[-1]).exists():
            shutil.copy(p, out)

for f in out.iterdir():
    tries = 0
    while f.stat().st_size < minsize * 1024 * 1024 and tries < 5:
        doubleimg(f)
