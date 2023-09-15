import os
from shutil import copyfile, rmtree


def union_pack():
    csv = open("tools/src/union/union.csv","w")
    union_dir = "1_extracted/union/"
    patched = os.listdir("2_translated/union/")
    id = 0
    for filename in os.listdir(union_dir):
        if filename in patched:
            csv.write("2_translated\\union\\{0},,{1},Uncompress\n".format(filename,id))
        else:
            csv.write("1_extracted\\union\\{0},,{1},Uncompress\n".format(filename,id))
        id+=1
    csv.flush()
    csv.close()
    os.system("tools\\crifilesystem\\cpkmakec.exe tools/src/union/union.csv -mode=ID -mask 3_patched/DATA/union.cpk")
if __name__ == "__main__":
    union_pack()
