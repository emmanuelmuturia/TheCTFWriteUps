# Flag in Flame

The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: [Logs Data](https://challenge-files.picoctf.net/c_amiable_citadel/eb3bef3ff1c8111665bbec934c3208346c59d291f2417a91dd70305589c16ceb/logs.txt). Be prepared—the file is large, and examining it thoroughly is crucial .

## Background

This Challenge had a downloadable Log File along with one Hint:

1] Use base64 to decode the data and generate the image file.

It was classified under "Forensics", and therefore it meant that it required you to apply some Forensic Analysis to retrieve The Flag...

## Procedure

**Step #1:** This was relatively straightforward, especially with the Hint, so the first step would be to simply copy the Base64 content of the File and paste it into any online Tool that converts Base64 to an Image...

**Step #2:** Next, you will get the Image of a Hacker on his Laptop along with a long string of Text below. Find an online Tool to extract Text from an Image to get that Text...

**Step #3:** Copy that Text and then find an online Tool to convert it from Hexadecimal to Text. There is your Flag...


## Conclusion

This Challenge tested your Forensics Skills, specifically how to use limited Clues to find more Information...
