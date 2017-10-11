#RedEye CTF 2017 : Handler

* **Category**: Network <br>
* **Author**: Faid Mohammed Amine
* **Contact**: hello@faidamine.pw
* **Description**: 

1 - Open handler.pcap with wireshark, use "http.request or http.response" as display filter.  Save kotehok.html and the 3 javascripts files it needs: gibberish-aes.js, pbkdf2.js and sha1.js locally.  Select either line-based text data (for html) or media type (for js files).  You may want to save kotehok.html as index.html to save some efforts later" 

2 - Serve the files locally using a web server, then point your web browser to the html page.  You should see a password input to enter the key and a textarea to enter plain text to be encrypted.

3 - Using a javascript debugger, like firebug, inspect the javascript code embedded in the html page.

4 - Fix the javascript in doIt() function, does not work for me, change following lines:

x = document.Crypto.key1.value;
if (x.length > 300) {
msg = document.Crypto.plaintext.value;

From then on, you should be able to encrypt text and see ciphertext in firebug's console.  xmlhttp.open() may fail but it is not necessary to solve this challenge

5 - Place breakpoints in function doIt() in such a way that you will get the value of x, y and CT variable.  Run doIt() several times with different keys & plaintext.

6 - You should notice than y, which is the result of expandkey(x) is never longer than 4 caracters, no matter the lenght of the key you submitted. In fact, it look like a base64 encoded string of a single caracter.  Have a look at expandkey()


7 - Prepare decryption function using doIt() function as template, named mine usetheforcebrute().

function usetheforcebrute() {
  x = document.Crypto.key1.value;
  y = expandkey(x);
  pbkdf2 = new PBKDF2(y, "NaCl", 1000, 16)
  msg = document.Crypto.plaintext.value;
  CT = GibberishAES.dec(msg,pbkdf2);
  alert(CT);
}

Add a button to call it:
<input type='button' value='droptheflag' onclick='usetheforcebrute()' />


8 - Get ciphertext from pcap2.pcap (the post request), paste in text area, enter any key, click drop the flag.

9 - We got the flag


# Write-up 

(TODO)

# Other write-ups and resources

