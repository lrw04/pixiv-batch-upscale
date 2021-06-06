from pathlib import Path
from sys import argv
import util

dir = Path(argv[1])

for f in dir.iterdir():
    if not f.is_file():
        continue
    fn = f.parts[-1]
    pid = util.get_pid(fn)
    print(f"{pid[0]},{pid[1]}")
