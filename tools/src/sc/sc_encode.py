import os
import shutil
def sc_encode():
    #encode sc
    print("encode  sc/*.bin....")
    try:
        shutil.rmtree("2_translated\\sc")
    except FileNotFoundError:
        print("Dir already deleted.")
    os.system("tools\\baka\\Baka.exe 1_extracted\\sc 2_translated\\txt 2_translated\\sc")
    


if __name__ == "__main__":
    sc_encode()