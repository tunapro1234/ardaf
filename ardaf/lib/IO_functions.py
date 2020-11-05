import ardaf.res.glob as glob
import base64
import json

def encrypt(obj):
    return {key: (base64.b64encode(value.encode()).decode() if type(value) is str else value) for key, value in obj.items()}

def decrypt(obj):
    return {key: (base64.b64decode(value.encode()).decode() if type(value) is str else value) for key, value in obj.items()}

def create_file(path=glob.json_path):
    try:
        with open(path, "w+"):
            pass    
    except:
        raise Exception("Dosya oluşturulamıyor")
    return True

def get_settings(path=glob.json_path):
    try:
        with open(path, "r") as file:
            read = json.load(file)

    except FileNotFoundError:
        create_file()
        read = interface.get_profile_details()
        return save_settings(read)

    return decrypt(read)

def save_settings(settings, path=glob.json_path):
    try:
        with open(path, "w+") as file:
            json.dump(encrypt(settings), file)
    except:
        raise Exception("Yazma hatası.")
    return True

