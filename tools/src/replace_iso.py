import os
from shutil import copyfile

def replace_iso():
    # Create duplicate of original .iso for patching.
    print("Copying game iso")
    isoName = "0_iso/Baka_to_Test_to_Shoukanjuu_Portable_JPN.iso"
    copyfile(isoName, "4_build/BakaPatched.iso")

    # Replace sc.cpk with patched version.
    print("Replacing sc.cpk")
    os.system("tools\\UmdReplace\\UMD-replace.exe 4_build/BakaPatched.iso PSP_GAME/USRDIR/DATA/sc.cpk 3_patched/DATA/sc.cpk")
    
    ## Replace union.cpk with patched version.
    print("Replacing union.cpk")
    os.system("tools\\UmdReplace\\UMD-replace.exe 4_build/BakaPatched.iso PSP_GAME/USRDIR/DATA/union.cpk 3_patched/DATA/union.cpk")

    # Replace EBOOT.BIN with patched version.
    print("Replacing EBOOT.BIN")
    os.system("tools\\UmdReplace\\UMD-replace.exe 4_build/BakaPatched.iso PSP_GAME/SYSDIR/EBOOT.BIN 3_patched/SYSDIR/EBOOT.BIN")
        
    # Replace lt.bin with patched version.
    print("Replacing lt.bin")
    os.system("tools\\UmdReplace\\UMD-replace.exe 4_build/BakaPatched.iso PSP_GAME/USRDIR/DATA/lt.bin 3_patched/DATA/lt.bin")
    
    

if __name__ == "__main__":
    replace_iso()
