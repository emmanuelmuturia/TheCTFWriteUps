# Task #15: Binary walk

Please exfiltrate my file :)

[Please download the task file[s]...]

## Background

Since the task file is a photo, you might be wondering why The Hint points us to Binwalk. The answer lies in both the description and The Hint. Let me explain:

## Procedure

**Step #1:** As you might have guessed it, our first step is to use the `file [File Name]` command to see what kind of file we are handling...

**Step #2:** The file is a photo but why does The Hint point us to Binwalk? The answer is simple. The file is not just a photo. There is something else hidden on the inside...

**Step #3:** You can use the `binwalk` tool or visit an online version of it. Once you do, you will be shown that the image has other files embedded inside of it, with one of them being an archived text file name "hello_there.txt"...

**Step #4:** Download and uncompress it. The text file has two lines, with the first one being, "Thank you for extracting me, you are the best!" and the second one is the flag...

## Conclusion

This task once again tested your knowledge of Steganography and Forensics, where stuff is hidden in plain sight. Binwalk is a tool for analyzing, reverse engineering, and extracting Firmware Images and can identify File Signatures, Compressed Data, File Systems, and more within binary files. Do you see Task #16 already?..
