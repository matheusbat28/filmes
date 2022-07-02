import pandas as pd
import json
from funticions import value_by_dict

list = []
dict_json = {}
execel_files = pd.read_excel("notas_filmes.xlsx")

value_by_dict(list, execel_files.get('Filmes'),'Filmes')
value_by_dict(list, execel_files.get('Marcos'),'Marcos')
value_by_dict(list, execel_files.get('Lucas'),'Lucas')
value_by_dict(list, execel_files.get('Matheus'),'Matheus')
value_by_dict(list, execel_files.get('Igor'),'Igor')
value_by_dict(list, execel_files.get('Vitor'),'Vitor')
value_by_dict(list, execel_files.get('Bia'),'Bia')
value_by_dict(list, execel_files.get('Gui'),'Gui')
value_by_dict(list, execel_files.get('Status'),'Status')

cont = 1
for x in list:
    dict_json[f'f{cont}'] = x
    cont += 1 

with open('filmes.json', 'w', encoding='utf-8') as file_json:
    file_json.write(json.dumps(dict_json))