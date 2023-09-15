import os


def patch_eboot():
    print("patch EBOOT.BIN")
    
    #decrypt eboot
    print("Decrypting eboot...")
    os.system(
        "tools\\DecEboot\\deceboot.exe 0_original\\SYSDIR\\EBOOT.BIN 1_extracted\\EBOOT.BIN")

    #insert vwf function
    print("Inserting vwf function...")
    os.system("tools\\Armips\\armips.exe tools\\src\\eboot\\eboot.asm")


if __name__ == "__main__":
    patch_eboot()
