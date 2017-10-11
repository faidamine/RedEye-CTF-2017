#RedEye CTF 2017 : Leaks

* **Category**: Network <br>
* **Author**: Faid Mohammed Amine
* **Contact**: hello@faidamine.pw
* **Description**: 

$ tshark  -r  leak.pcap  -T fields -e data | xxd -r -p

output :

...
...
FLAG-:x:115:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false
icmp:x:106:110::/var/run/dbus:/bin/false
parici:x:33:33:www-data:/var/www:/usr/sbin/nologin
imcp:x:33:33:www-data:/var/www:/usr/sbin/nologin
parla:x:116:124:PulseAudio daemon,,,:/var/run/pulse:/bin/false
....

FLAG is icmppariciicmpparla




# Write-up 

(TODO)

# Other write-ups and resources

