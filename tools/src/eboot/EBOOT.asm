.PSP

.open "1_extracted\\EBOOT.BIN","3_patched\\SYSDIR\\EBOOT.BIN",0x8804000 -0xc0

//speaker name limit
.org 0x08807808
	addiu	a0,a1,0x10
	li	a1,0x29

//.org 0x0088867A4//
//	li	a2,20     //original li a2,6,the game break, if we enlarge the value

//textbox line limit char
.org 0x08804dc0
	li	a0,0x29
	
//log textbox line limit char
.org 0x08811ce0
	li	a2,0x29
	
	
//letter spacing
.org 0x08808D1C
	addiu	a0,a0,0x10

//checksum always true
.org 0x0882b284
		li	v0,0x1
		
//jump to vwf
.org 0x08886640
	jal	vwf_speaker
	

.org 0x08886644
	nop	
.org 0x0888664c
	nop	
	
	
.org 0x08886bfc 
	nop	
.org 0x08886c04 
	nop	
.org 0x08886c18 
	addu	a2,a0,a1


.org 0x08886c34 
	jal	vwf_text
	
	
	

.org 0x0893ccc0

.func vwf_speaker
	li	v0,0x5C
	mult	a0,v0
	mflo	a0
	addu	v0,a0,a1
	lbu	v0,0x5B(v0)//load width from lt.bin
	addi v0,v0,1
	beq	s3,zero,Lab2
	move	a0,v0
	lhu	a0,0x30(s5)
	addu	a2,a2,a0
	addu	a0,a0,v0
Lab2: 
	sh	a0,0x30(s5)
	jr	ra
	lhu	a0,0x0(s0)
.endfunction	



.func vwf_text
	li	v0,0x5C
	mult	s6,v0
	mflo	a0
	addu	v0,a0,a1
	lbu	v0,0x5B(v0)//load width from lt.bin
	lbu	a0,0x0(s1)
	beq	a0,zero,Lab1
	move	a0,v0
	lhu	a0,0x20(s1)
	addu	a2,a2,a0
	addu	a0,a0,v0
Lab1:   
	sh	a0,0x20(s1)
	jr	ra
	move	a0,s6
.endfunction	

.close

