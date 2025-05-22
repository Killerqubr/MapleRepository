# - Colours - #
CRe = "\033[0m"    # Reset
C31 = "\033[31m"   # Red
C32 = "\033[32m"   # Green
C33 = "\033[33m"   # DarkGreen
C34 = "\033[34m"   # Blue
C35 = "\033[35m"   # Purple
C36 = "\033[36m"   # LightBlue
C37 = "\033[37m"   # Gray

def read():
    try:
        with open("Setting/Settings.txt","r",encoding="utf-8") as File:
            Settings = File.readlines()
    except FileNotFoundError:
        print("\033[31m[Error05] 'Setting.txt' is Missing!")
        exit()
    Result = []
    for string in Settings:
        Result.append(string.strip("\n"))
        continue
    return Result
def write(l,v):
    with open(f"Setting/Settings.txt","r",encoding="utf-8") as File:
        List = File.readlines()
        List.pop(l)
        List.insert(l,f"{v}\n")
    with open(f"Setting/Settings.txt","w",encoding="utf-8") as File:
        Line = [str(i) for i in List]
        File.writelines(Line)
def change(v,L12,L14,L17,L18):
    Setting = read()
    i = input(f"{C37}[*]{CRe}{C36}{L12}?{CRe}{C37}(y/n){CRe}")
    if i == "y":
        if Setting[v] == L17:
            return L18
        elif Setting[v] == L18:
            return L17
    else:
        print(f"{C31}[Error06]{CRe}{L14}!")