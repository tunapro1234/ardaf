import ardaf.res.glob as glob
import base64
import json

def encrypt(obj):
    return {key: base64.b64encode(value.encode()).decode() for key, value in obj.items()}

def decrypt(obj):
    return {key: base64.b64decode(value.encode()).decode() for key, value in obj.items()}

def create_file():
    try:
        with open(glob.json_path, "w+"):
            pass    
    except:
        raise Exception("Dosya oluşturulamıyor")
    return True

def get_settings():
    try:
        with open(glob.json_path, "r") as file:
            read = json.load(file)

    except FileNotFoundError:
        return reset_settings()
    
    return decrypt(read)

def save_settings(settings):
    try:
        with open(glob.json_path, "w+") as file:
            json.dump(encrypt(settings), file)
    except:
        raise Exception("Yazma hatası.")
    return True

def reset_settings():
    create_file()

