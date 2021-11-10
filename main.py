'''
Zaahier Adams
https://github.com/ZaahierAdams
10 November 2021

Acknowledgements:
stackoverflow user:     https://stackoverflow.com/users/5393381/mseifert
original post:          https://stackoverflow.com/a/49723101
'''

import json
from collections.abc import MutableMapping


def inputs():
    source  = input('\nProvide full path of file: ')
    keys    = input('\nProvide keys to remove (separate multiple keys with a comma):')
    keys_list = keys.split(',')
    return source, keys_list


# modified to handle lists with dictionary elements
def delete_keys_from_dict(dictionary, keys):
    keys_set = set(keys)
    modified_dict = {}
    for key, value in dictionary.items():
        if key not in keys_set:

            # if dict
            if isinstance(value, MutableMapping):
                modified_dict[key] = delete_keys_from_dict(value, keys_set)
            
            # if list
            elif isinstance(value, list):
                modified_dict[key] = value  
                fresh_list = []
                for i in value:
                    if isinstance(i, MutableMapping):
                        fresh_list.append(delete_keys_from_dict(value[value.index(i)], keys_set))
                modified_dict[key] = fresh_list

            else:
                modified_dict[key] = value  
    
    return modified_dict


# write to JSON file
def write_json(source, modified_dict, data_file, indent):
    try:
        with open(source, 'w') as data_file:
            json.dump(modified_dict, data_file, indent = indent)
    except Exception as e:
        print('Error in writting to JSON file\n'+str(e))


def handle_json(source, keys):
    indent = 2
    with open(source) as data_file:
        try:
            data = json.load(data_file)
            modified_dict  = delete_keys_from_dict(data, keys)

            # Console Print
            prettyfy = json.dumps(modified_dict, indent = indent, sort_keys=True)
            #print("\n\nResult:")
            #print(prettyfy)

            write_json(source, modified_dict, data_file, indent)
            
        except Exception as e:
            print("Error in loading JSON file\n"+str(e))

def hang():
    close = input("\n...Completed...\nPress any button to close.")
    
def main():
    source, keys = inputs()
    handle_json(source, keys)
    hang()

main()
    
