# -*- coding : utf-8 -*-

# - Colours - #
CRe = "\033[0m"    # Reset
C31 = "\033[31m"   # Red
C32 = "\033[32m"   # Green
C33 = "\033[33m"   # DarkGreen
C34 = "\033[34m"   # Blue
C35 = "\033[35m"   # Purple
C36 = "\033[36m"   # LightBlue
C37 = "\033[37m"   # Gray

def check():
    try:
        with open(f"Language/_init_.py","r") as File:
            List = File.readlines()
    except FileNotFoundError:
        print(f"{C33}[Error01] File'_init_.txt'is Missing{CRe}")
        exit()
    try:
        Language = List[1]
    except IndexError:
        print(f"{C31}[Error02] File Error!{CRe}")
        print(f"{C33}Something wrong in the line 2 of '_init_.py'{CRe}")
        print(f"{C33}You need overwrite it with your Language File name{CRe}")
        exit()
    try:
        with open(f"Language/{Language}.txt","r",encoding="utf-8") as File:
            pass
    except FileNotFoundError:
        print(f"{C31}[Error03] Language File Not Found!{CRe}")
        print(f"{C33}You need import a Language File into folder'Language'{CRe}")
        exit()
    return Language
def read(Language):
    with open(f"Language/{Language}.txt","r",encoding="utf-8") as File:
        List = File.readlines()
        Result = []
        for string in List:
            Result.append(string.strip("\n"))
            continue
        return Result
def change(SLanguage):
    LLanguage = check()
    print(f"{C37}{CRe}{LLanguage}{C36}->{CRe}{SLanguage}")
    print(f"{C31}\n[!]All Settings Changed have been removed!\n{CRe}")
    with open("Language/_init_.py","r",encoding="utf-8") as File:
        List = File.readlines()
        List[1] = SLanguage
    with open("Language/_init_.py","w",encoding="utf-8") as File:
        File.writelines(List)
    with open(f"Language/{SLanguage}.txt","r",encoding="utf-8") as File:
        List = File.readlines()
        SL17 = List[17]
        SL18 = List[18]
    with open(f"Language/{LLanguage}.txt","r",encoding="utf-8") as File:
        List = File.readlines()
        L17 = List[17]
        L18 = List[18]
    with open("Setting/Settings.txt","r",encoding="utf-8") as File:
        List = File.readlines()
        count = 0
        RList = []
        for string in List:
             i = List[count]
             if i == L17:
                 RList.append(SL17)
             elif i == L18:
                 RList.append(SL18)
             continue
    with open(f"Setting/Settings.txt","w",encoding="utf-8") as File:
        File.writelines(RList)
        exit()