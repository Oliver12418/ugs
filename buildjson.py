import os
list = os.listdir("./games/")
json = open("./games.json", "w")
json.write('')
json.write(
    str(list)
    .replace('[', '[\n ')
    .replace(']', '\n]')
    .replace(',', ',\n')
    .replace('\'', '\"')
    .replace(' ', '    ')
    .replace('.html', '')
)