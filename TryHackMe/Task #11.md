# Task #11: Can you fix it?

I accidentally messed up with this PNG file. Can you help me fix it? Thanks, ^^

[Please download the task file[s]...]

## Background

We have a photo and The Hint clearly asks us to check the image's header. What does this mean?

## Procedure

**Step #1:** Since the photo has been said to be "spoilt", let us use this Linux command to check if it is still a photo: `file [File Name]`...

**Step #2:** The output [data] means that our photo is actually a Binary File. Since The Hint mentioned the Header, we can use any Metadata-viewing tool to check if the Header bits correspnd to that of a photo. They do not since any tool you use will reveal the first 8 Header Bits as: 23 33 44 5F 0D 0A 1A 0A. The standard 8 Header Bits are usually: 89 50 4E 47 0D 0A 1A 0A...

**Step #3:** To repair the photo, we simply need to replace the weird Header Bits with those of a valid photo. We can achieve using this command: `printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | dd conv=notrunc of=[File Name] bs=1 seek=0`...

**Step #4:** Once the operation has been completed, it means that the photo has been repaired. When you open the photo, you should see the flag...

## Conclusion

This task tested your prowess in File Format Signatures, Hex Editing, and Data Recovery, all which are critical in Digital Forensics. Imagine if you were hacked and your files were corrupted. Where is Task #12?
