import os
import struct
import json
import gzip
import io
import glob
import sys
import shutil

group1_ptr_offset =0x12D798
group1_sizes  ={
1000:0x20,
1001:0x20,
1002:0x20,
1003:0x20,
1004:0x23,
1005:0x25,
1006:0x25,
1007:0x25,
1008:0x23,
1009:0x23,
1010:0x24,
1011:0x26,
1012:0x25,
1013:0x23,
1014:0x23,
1015:0x23,
1016:0x25,
1017:0x27,
1018:0x27,
1019:0x22,
1020:0x21,
1021:0x22,
1022:0x21,
1023:0x24,
1024:0x22,
1025:0x20,
1026:0x20,
1027:0x20,
1028:0x20,
1029:0x20,
1030:0x1f,
1031:0x20,
1032:0x20,
1033:0x20,
1034:0x20,
1035:0x21,
1036:0x21,
1037:0x22,
1038:0x21,
1039:0x21,
1040:0x21,
1041:0x21,
1042:0x21,
1043:0x25,
1044:0x23,
1045:0x23,
1046:0x24,
1047:0x24,
1048:0x26,
1049:0x25,
1050:0x28,
1051:0x2d,
1052:0x28,
1053:0x25,
1054:0x21,
1055:0x22,
1056:0x29,
1057:0x28,
1058:0x29,
1059:0x26,
1060:0x25,
1061:0x23,
1062:0x29,
1063:0x2e,
1064:0x2e,
1065:0x22,
1066:0x22,
1067:0x22,
1068:0x2a,
1069:0x2a,
1070:0x28,
1071:0x23,
1072:0x10,
1073:0x07,
1074:0x2e,
1075:0x09,
1076:0x05,
1077:0x06,
1078:0x06,
1079:0x19,
1080:0x21,
1081:0x23,
1082:0x34,
1083:0x25,
1084:0x20,
1085:0x19,
1086:0x2d,
1087:0x29,
1088:0x28,
1089:0x2f,
1090:0x28,
1091:0x2e,
1092:0x22,
1093:0x2a,
1094:0x27,
1095:0x27,
1096:0x04,
1097:0x04,
1098:0x06,
1099:0x07,
1100:0x05,
1101:0x07,
1102:0x06,
1103:0x05,
1104:0x08,
}
group2_ptr_offset =0x12D93C
group2_sizes = {
1105:0x1b,
1106:0x26,
1107:0x1f,
1108:0x15,
1109:0x1e,
1110:0x1e,
1111:0x16,
1112:0x16,
1113:0x26,
1114:0x1d,
1115:0x1d,
1116:0x21,
1117:0x17,
1118:0x16,
1119:0x0f,
1120:0x13,
1121:0x10,
1122:0x0f,
1123:0x10,
1124:0x10,
1125:0x0d,
1126:0x0c,
1127:0x12,
1128:0x0f,
1129:0x0f,
1130:0x10,
1131:0x0e,
1132:0x0f,
1133:0x10,
1134:0x16,
1135:0x13,
1136:0x0d,
1137:0x13,
1138:0x13,
1139:0x11,
1140:0x10,
1141:0x12,
1142:0x10,
1143:0x10,
1144:0x10,
1145:0x10,
1146:0x11,


}
group3_ptr_offset =0x144570
group3_sizes = {
1147:0x00cc,
1148:0x0001,
1149:0x0028,
1150:0x0057,
1151:0x005b,
1152:0x00ab,
1153:0x001e,
1154:0x005b,
1155:0x001d,
1156:0x0001,
1157:0x0075,
1158:0x002d,
1159:0x0033,
1160:0x0078,
1161:0x018c,
1162:0x0125,
1163:0x0080,
1164:0x0206,
1165:0x01c5,
1166:0x0280,
1167:0x01b7,
1168:0x015e,
1169:0x021b,
1170:0x0197,
1171:0x0161,
1172:0x0028,
}
def calc_checksum(f):
    s = f.tell()
    f.seek(0)
    p1 = 0x11111111
    p2 = 0x11111111
    p3 = 0x11111111
    p4 = 0x11111111
    m = 0xffffffff
    s -= 16
    while s > 0:
        a1 = int.from_bytes(f.read(4), byteorder='little')
        a2 = int.from_bytes(f.read(4), byteorder='little')
        a3 = int.from_bytes(f.read(4), byteorder='little')
        a4 = int.from_bytes(f.read(4), byteorder='little')
        p1 += a1
        p1 = p1 & m
        if p1 < a1:
            p2 += 1 + a2
        else:
            p2 += 0 + a2
        p2 = p2 & m
        p3 += a3
        p3 = p3 & m
        if p3 < a3:
            p4 += 1 + a4
        else:
            p4 += 0 + a4
        p4 = p4 & m
        s -= 16
    # print("%x %x %x %x" % (p1, p2, p3, p4))
    return struct.pack("<IIII", p1, p2, p3, p4)

def make_pixel(chunk,ref,dsizes,binary):
    ret = io.BytesIO()
    ret.write(struct.pack("I",chunk))
    binary_compressed = io.BytesIO()
    for size in dsizes:
        ret.write(struct.pack("I",binary_compressed.tell()+ref))
        binary_compressed.write(struct.pack("IIII", size, 0, 0, 0))
        binary_compressed.write(gzip.compress(binary.read(size),compresslevel=9))
        align = (16 - (binary_compressed.tell() % 16))
        if align:
            binary_compressed.write(b"\x00" * align)
    ret.write(struct.pack("I", binary_compressed.tell() + ref))
    align = (16 - (binary_compressed.tell() % 16))
    if align:
        binary_compressed.write(b"\x00" * align)
    ret.seek(ref)
    ret.write(binary_compressed.getbuffer())
    align = (0x800 - (ret.tell() % 0x800))
    if align:
        ret.write(b"\x00" * align )
    checksum = calc_checksum(ret)
    ret.seek(-16, 2)
    ret.write(checksum)
    ret.seek(0)
    return ret.read()

def cgs_insert():
    cwd = os.getcwd()
    try:
        shutil.rmtree("2_translated/union/")
    except FileNotFoundError:
        print("Dir already deleted.")
    os.makedirs(os.path.dirname("2_translated/union/"), exist_ok=True)
    eboot = open("3_patched/SYSDIR/EBOOT.BIN", "r+b")
    for js in glob.glob("2_translated/cgs/*.json"):
        info = json.loads(open(js, "rb").read())
        union_index = int(os.path.basename(js[:-5]))
        pixel_index = 1
        out = open("2_translated/union/{0:05d}.bin".format(union_index), 'w+b')
        update_pointer = False
        update_pallete = []
        update_pixel = []
        for pal, pix in zip(info["content"]["pallete"], info["content"]["pixel"]):
            try:
                os.system(
                    "tools\\GimConv\\GimConv.exe 2_translated/cgs/{0}_{1:02d}.png -o {2}/2_translated/cgs/temp.gim {3}".format(
                        union_index, pixel_index, cwd, pix["format"]))
                gim = open("2_translated/cgs/temp.gim", 'rb')
            except:
                sys.exit()
            gim.seek(0x44)
            gim_format = struct.unpack("H", gim.read(2))[0]
            gim.seek(0x34)
            pixel_size = struct.unpack("I", gim.read(4))[0] - 0x50
            if (gim_format != 4) and (gim_format != 5):
                print("Invalid gim format, make sure the png format are indexed color.")
                sys.exit()
            gim.seek(0x80)
            pixel = make_pixel(pix["chunk"], pix["chunk_offset"][0], pix["gzip_dsizes"],
                               io.BytesIO(gim.read(pixel_size)))
            gim.seek(4, 1)
            palet_size = struct.unpack("I", gim.read(4))[0] - 0x50
            gim.seek(0x48, 1)
            pallete = gim.read(palet_size)
            gim.close()
            os.remove("2_translated/cgs/temp.gim")
            pixel_index+=1
            if info["ptr_offset"] == None:
                out.seek(pal["offset"])
                out.write(pallete)
                out.seek(pix["offset"])
                out.write(pixel)
            else:
                update_pointer = True
                update_pallete.append(pallete)
                update_pixel.append(pixel)
        #if info["content"]["map"]:
        #    map = open("work/isofiles/cgs/{0}.map".format(union_index), "rb").read()
        #    out.seek(info["content"]["map"]["offset"])
        #    out.write(map)
        if update_pointer:
            eboot.seek(info["ptr_offset"])
            for upallete in update_pallete:
                eboot.write(struct.pack("I", out.tell()))
                out.write(upallete)
            for upixel in update_pixel:
                eboot.write(struct.pack("I", out.tell()))
                out.write(upixel)
                out.write(b"\x00" * (0x1000 - (out.tell() % 0x1000)))
            checksum = calc_checksum(out)
            out.seek(-16, 2)
            out.write(checksum)
        out.close()
        
        
        
        if union_index in group1_sizes:
            new_union_size = os.path.getsize("2_translated/union/0{}.bin".format(union_index))
            group1_sizes.update({union_index:new_union_size>>11})
            
        if union_index in group2_sizes:
            new_union_size = os.path.getsize("2_translated/union/0{}.bin".format(union_index))
            group2_sizes.update({union_index:new_union_size>>11})
            
        if union_index in group3_sizes:
            new_union_size = os.path.getsize("2_translated/union/0{}.bin".format(union_index))
            group3_sizes.update({union_index:new_union_size>>11})
    
    
    group1_offset = 0
    eboot.seek(group1_ptr_offset)
    for j in group1_sizes:
        eboot.write(struct.pack("HH",group1_offset,group1_sizes[j]))
        group1_offset+=group1_sizes[j]
        
        
    group2_offset = 0
    eboot.seek(group2_ptr_offset)
    for j in group2_sizes:
        eboot.write(struct.pack("HH",group2_offset,group2_sizes[j]))
        group2_offset += group2_sizes[j]
        
    group3_offset = 0
    eboot.seek(group3_ptr_offset)
    for j in group3_sizes:
        eboot.write(struct.pack("HH",group3_offset,group3_sizes[j]))
        group3_offset += group3_sizes[j]



if __name__ == "__main__":
    cgs_insert()