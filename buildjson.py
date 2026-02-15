import os
import json

lst = sorted(
    f for f in os.listdir("./games/")
    if f.endswith(".html") and os.path.isfile(os.path.join("games", f))
)
files = [os.path.splitext(f)[0] for f in lst]

with open("./games.json", "w", encoding="utf-8") as file:
    json.dump(files, file, indent=4, ensure_ascii=False)