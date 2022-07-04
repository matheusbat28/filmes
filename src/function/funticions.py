
def value_by_dict(list, list_Name, name):
    cont = 0
    if name == 'Filmes':
        for x in list_Name: 
            dict_filmes = {}
            dict_filmes[name] = x.strip().capitalize()
            list.append(dict_filmes)

    elif name == 'Status':
        for x in list_Name: 
            x_str = str(x)
            if x_str == "nan":
                list[cont][name] = ' '  
            else:        
                list[cont][name] = x_str.strip().capitalize()
                cont += 1
    else:
        for x in list_Name: 
            x_str = str(x)
            if x_str == "nan":
                list[cont][name] = '0'  
            else:        
                list[cont][name] = x_str.strip().capitalize()
            cont += 1