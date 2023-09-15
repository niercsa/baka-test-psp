import os
import struct

def update_pointer():
    eboot = open("3_patched\\SYSDIR\\EBOOT.BIN","r+b")
    offset_pointer = 0x145000
    eboot.seek(offset_pointer)
    offset_sc = 0
    for i in range(85):
        size_sc = os.path.getsize("2_translated\\sc\\{0:05d}.bin".format(i))//0x800
        eboot.write(struct.pack("hh",offset_sc,size_sc))
        offset_sc+=size_sc
def sc_pack():
    #pack sc
    print("packing sc.cpk....")
    os.system(
        "tools\\crifilesystem\\cpkmakec.exe tools\\src\\sc\\sc.csv 3_patched\\DATA\\sc.cpk")
    update_pointer()

    


if __name__ == "__main__":
    sc_pack()