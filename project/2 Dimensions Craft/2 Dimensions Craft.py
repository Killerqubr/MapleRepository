# 2 Dimensions Craft  - Ropeway Edition #

# - Imported Funtions - #
import glob
import time
from Language import language
from Saves import save
from Setting import settings

# - Colours - #
CRe = "\033[0m"    # Reset
C31 = "\033[31m"   # Red
C32 = "\033[32m"   # Green
C33 = "\033[33m"   # DarkGreen
C34 = "\033[34m"   # Blue
C35 = "\033[35m"   # Purple
C36 = "\033[36m"   # LightBlue
C37 = "\033[37m"   # Gray

# - Load Language File - #
Language = language.read(language.check())

# - Main Interface - #
while True:
    print(f"\n{C35}- {Language[0]} -{CRe}")
    print(f"{C32} 1{CRe}.{Language[1]}")
    print(f"{C32} 2{CRe}.{Language[2]}")
    print(f"{C32} 3{CRe}.{Language[3]}")
    print(f"{C32} 4{CRe}.{Language[19]}")
    print(f"{C32} 5{CRe}.{Language[4]}")
    time.sleep(0.1)
    MI = input(f"{C37}[#]{CRe}{C36}{Language[5]}:{CRe}")
#    print('\n'*20)
    if MI == "1":
        pass
    elif MI == "2":
        print(f"{C31}[Error04]{CRe}{C36}{Language[6]}:){CRe}")
        continue
    elif MI == "3":
        Setting = settings.read()
        while True:
            print(f"\n{C35}= {Language[3]} ={CRe}")
            print(f"{C32} 1{CRe}.{Language[7]}")
            print(f"{C32} 2{CRe}.{Language[8]}")
            print(f"{C32} 3{CRe}.{Language[11]}")
            time.sleep(0.1)
            MSI = input(f"{C37}[#]{CRe}{C36}{Language[5]}:{CRe}")
            if MSI == "1":
                while True:
                    print(f"\n{C35}-= {Language[7]} =-{CRe}")
                    print(f"{C32}1{CRe}.{Language[16]} - {C34}{Setting[1]}{CRe}")
                    print(f"{C32}2{CRe}.{Language[13]}")
                    time.sleep(0.1)
                    MSGI = input(f"{C37}[#]{CRe}{C36}{Language[5]}:{CRe}")
                    if MSGI == "1":
                        Setting[1] = settings.change(1,Language[12],Language[14],Language[17],Language[18])
                        continue
                    elif MSGI == "2":
                        break
                    else:
                        print(f"{C31}[Error06]{CRe}{Language[14]}!")
            elif MSI == "2":
                while True:
                    print(f"\n{C35}-= {Language[8]} =-{CRe}")
                    print(f"{C32}1{CRe}.{Language[9]}({Language[10]}) - {C34}{Setting[0]}{CRe}")
                    print(f"{C32}2{CRe}.{Language[13]}")
                    time.sleep(0.1)
                    MSVI = input(f"{C37}[#]{CRe}{C36}{Language[5]}:{CRe}")
                    if MSVI == "1":
                        Setting[0] = settings.change(0,Language[12],Language[14],Language[17],Language[18])
                        continue
                    elif MSVI == "2":
                        break
                    else:
                        print(f"{C31}[Error06]{CRe}{Language[14]}!")
                        continue
            elif MSI == "3":
                settings.write(0,Setting[0])
                settings.write(1,Setting[1])
                print(f"{C37} [%]{Language[15]}{CRe}")
                break
            else:
                 print(f"{C31}[Error06]{CRe}{Language[14]}!")
                 continue
    elif MI == "4":
        while True:
            LList = glob.glob("Language/*.txt")
            print(f"\n{C35}= {Language[19]} ={CRe}")
            List = []
            for string in LList:
                A = string.strip("Language/")
                B = A.strip(".txt")
                List.append(B)
                continue
            count = 1
            for string in List:
                print(f"{C32} {count}{CRe}.{string}")
                count += 1
                continue
            print(f"{C33} {count}{CRe}.{Language[13]}")
            SLanguage = input(f"{C37}[#]{CRe}{C36}{Language[5]}:{CRe}")
            if SLanguage in List:
                ULanguage = language.check()
                if ULanguage == SLanguage:
                    print(f"{C31}[Error08]{Language[20]}{CRe}")
                    continue
                else:
                    language.change(SLanguage)
            elif SLanguage == Language[13]:
                break
    elif MI == "5":
        exit()
    else:
         print(f"{C31}[Error06]{CRe}{Language[14]}!")
         continue