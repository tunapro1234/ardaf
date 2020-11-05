import ardaf.res.glob as glob

def get_profile_details():
    profile = {}
    try:
    #yapf: disable
        for key in [key for key, value in glob.default_profile.items() if type(value) is str]:
            print(f"Profile {key} >> ", end="")
            profile[key] = input()
    #yapf: enable
    except KeyboardInterrupt:
        return get_profile_details()
    return profile

def get_post():
    final = ""
    try:
        print(f"Post content >> ", end="")
        final = input()
    except KeyboardInterrupt:
        print("")
        return get_post()
    return final