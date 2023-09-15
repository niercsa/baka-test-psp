### patching eboot
import tools.src.eboot.patch_eboot
tools.src.eboot.patch_eboot.patch_eboot()

## patching lt
import tools.src.lt.patch_lt
tools.src.lt.patch_lt.patch_lt()

## adjust width font in lt
import tools.src.lt.adjust_width_font
tools.src.lt.adjust_width_font.adjust_width_font()

### encode sc/*.bin
import tools.src.sc.sc_encode
tools.src.sc.sc_encode.sc_encode()

### pack sc.cpk
import tools.src.sc.sc_pack
tools.src.sc.sc_pack.sc_pack()

### insert cgs
import tools.src.union.union_cgs_insert
tools.src.union.union_cgs_insert.cgs_insert()

### pack union
import tools.src.union.union_pack
tools.src.union.union_pack.union_pack()

### replace iso
import tools.src.replace_iso
tools.src.replace_iso.replace_iso()




