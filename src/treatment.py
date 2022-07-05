import pandas as pd
import json
import os
from function.funticions import value_by_dict
from apis.google import main
from screens.index import save

main()
path_file_save = save()
path_file = "src/files/notas_filmes.xlsx"
list = []
dict_json = {}
execel_files = pd.read_excel(path_file)

for x in execel_files:
    if x == 0:
        continue
    value_by_dict(list, execel_files.get(f'{x}'),f'{x}')


cont = 1
for x in list:
    dict_json[f'f{cont}'] = x
    cont += 1 

with open(path_file_save, 'w', encoding="UTF-8") as file_json:
    file_json.write(json.dumps(dict_json))

os.remove(path_file)
print(f"local do arquivo salvo: {path_file_save}")
print('------------------------FIM------------------------')