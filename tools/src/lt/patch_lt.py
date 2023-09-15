import os


def patch_lt():
    
    
    #decrypt eboot
    print("patch lt.bin....")
    os.makedirs("3_patched\\DATA\\", exist_ok=True)
    os.system(
        "tools\\Xdelta3\\xdelta3.exe -d -f -s 0_original\\DATA\\lt.bin tools\\src\\lt\\lt.xdelta 3_patched\\DATA\\lt.bin")

    


if __name__ == "__main__":
    patch_lt()
