# Hidden in plainsight

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image [here](https://challenge-files.picoctf.net/c_amiable_citadel/618fe22499d6c52fd1de495424be4ee540886e1d066fad4b2474d695757a50da/img.jpg).

## Background

This Challenge had a downloadable Image File along with one Hint:

1] Download the jpg image and read its metadata

It was classified under "Forensics", and therefore it meant that it required you to apply some Forensic Analysis to retrieve The Flag...

## Procedure

**Step #1:** This was relatively straightforward, especially with the Hint, so either use the `exiftool` through this Command: `exiftool <Name of Image File>.jpg`. If not, then use an online version of Exiftool...

**Step #2:** Next, look through the Attributes and notice how in the "Comment" we have what looks like a Base64 Value. Copy and decode it. You will find a Steghide Password in the format: `steghide: [Password]`...

**Step #3:** Copy the Password and go to an online version of Steghide and upload the Image File and use the Password to get The Flag...


## Conclusion

This Challenge tested your Forensics Skills, specifically how to use limited Clues to find more Information...
