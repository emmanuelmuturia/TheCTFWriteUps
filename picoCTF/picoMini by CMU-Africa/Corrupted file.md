# Corrupted file

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file [here](https://challenge-files.picoctf.net/c_amiable_citadel/bdd976098377529fe779dbd31b424f69e51327b5ba68fd247dfcc074f0684141/file).

## Background

This Challenge had a downloadable Binary File along with three Hints:

1] Try checking the file’s header.
2] JPEG
3] Tools like xxd or hexdump can help you inspect and edit file bytes.

It was classified under "Forensics", and therefore it meant that it required you to apply some Forensic Analysis concepts to retrieve The Flag...

## Procedure

**Step #1:** The first step would be to view the File's Headers to confirm what File Type it truly has. This can be done with `xxd corrupted.jpg | head`. Since the first Bytes are not `FF D8 FF E0`, then this is a corrupted Image File as the Header is broken...

**Step #2:** Fix it by adding the ".jpg" Extension to the File's name if you have not. Replace the Bytes using this Linux Command: `printf "\xFF\xD8\xFF\xE0" | dd of=<Name of File>.jpg bs=1 seek=0 conv=notrunc`.

**Step #3:** Open the Image and you will see The Flag...


## Conclusion

This Challenge tested your understanding of Digital Forensics and Hex when dealing with different File Types...
