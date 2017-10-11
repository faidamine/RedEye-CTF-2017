#RedEye CTF 2017 : Stupid Reverse 

* **Category**: Reverse <br>
* **Author**: Faid Mohammed Amine
* **Contact**: hello@faidamine.pw
* **Description**: 

$ gdb -q ./down

gdb-peda$ disas main
![](1.JPG)
gdb-peda$ b*0x0000000000400eb4
gdb-peda$ disas check
![](2.JPG)
gdb-peda$ b*0x0000000000400d9a
gdb-peda$ r
![](3.JPG)
gdb-peda$ s
gdb-peda$ set $rax=1
gdb-peda$ c
![](4.JPG)


and you get the flag 

# Write-up 

(TODO)

# Other write-ups and resources

