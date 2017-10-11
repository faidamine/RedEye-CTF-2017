#RedEye CTF 2017 : Stupid Reverse 

* **Category**: Reverse <br>
* **Author**: Faid Mohammed Amine
* **Contact**: hello@faidamine.pw
* **Description**: 

$ gdb -q ./down

gdb-peda$ disas main
![](1.jpg)
gdb-peda$ b*0x0000000000400eb4
gdb-peda$ disas check
![](2.jpg)
gdb-peda$ b*0x0000000000400d9a
gdb-peda$ r
![](3.jpg)
gdb-peda$ s
gdb-peda$ set $rax=1
gdb-peda$ c
![](4.jpg)


and you get the flag 

# Write-up 

(TODO)

# Other write-ups and resources

