# Baka to Test to Shoukanjuu Portable
An attempt to decompile and recompile aseets NPJH-50680 (バカとテストと召喚獣 Portable).  
Join us on [Discord](https://discord.gg/CcZ2M62Gsy)

## File Structure
```
D:.
|   UMD_DATA.BIN
|
\---PSP_GAME
    |   ICON0.PNG
    |   PARAM.SFO
    |   PIC1.PNG
    |
    +---INSDIR
    |       0000.DNS
    |       ICON0.PNG
    |       PIC1.PNG
    |
    +---SYSDIR
    |   |   BOOT.BIN
    |   |   EBOOT.BIN
    |   |   OPNSSMP.BIN
    |   |
    |   \---UPDATE
    |           DATA.BIN
    |           EBOOT.BIN
    |           PARAM.SFO
    |
    \---USRDIR
        \---DATA
                ed.pmf
                ICON0.PNG
                lt.bin
                MOV_PR.pmf
                op.pmf
                PIC1.PNG
                pr.bin
                sc.cpk
                se.acx
                union.cpk
                vo.cpk
```

# Programmer Notes

| PSP_GAME\USRDIR\DATA | Notes |
| -------------------- | ----- |
| ed.pmf | Ending movie |
| ICON0.PNG | Save image |
| lt.bin | Font |
| MOV_PR.pmf | Disclaimer? |
| op.pmf | Opening movie |
| PIC1.PNG | Game Image |
| pr.bin | ? |
| sc.cpk | Script |
| se.acx | Sound effects? |
| union.cpk | Music & Textures |
| vo.cpk | Voices |

# Resources
| Tool | Notes |
| ---- | ----- |
| [Kuriimu2](https://github.com/FanTranslatorsInternational/Kuriimu2) | Unpack / Repack CPK files |
