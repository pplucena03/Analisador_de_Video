import os 

def remove_file(dictory_path):
    for file_name in os.listdir(dictory_path):
        item_path = os.path.join(dictory_path, file_name)

        os.remove(item_path)