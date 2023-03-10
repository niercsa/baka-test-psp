# https://gbatemp.net/threads/baka-test-portable-english-translation-project.370054/post-5071311
# https://gbatemp.net/threads/baka-test-portable-english-translation-project.370054/post-5071857

def print_table():
    print("decimal, sjis-hex, sjis, baka, baka-hex")
    for i in range(33088,40957):
        try:
            print(str(i) + ", " + hex(i)[-4:].upper() + ", " + bytes.fromhex(hex(i)[-4:]).decode('shift-jis') + ", " + hex(i-33088)[2:].zfill(4).upper() + ", " + (hex(i-33088)[2:].zfill(4)).upper()[2:] + (hex(i-33088)[2:].zfill(4)).upper()[:2])
        except UnicodeDecodeError:
            continue

def print_tbl():
    for i in range(33088,40957):
        try:
            # Need to skip 33276
            print((hex(i-33088)[2:].zfill(4)).upper()[2:] + (hex(i-33088)[2:].zfill(4)).upper()[:2] + "=" + bytes.fromhex(hex(i)[-4:]).decode('shift-jis'))
        except UnicodeDecodeError:
            continue
