# Task #9: Left or right

Left, right, left, right... Rot 13 is too mainstream. Solve this

MAF{atbe_max_vtxltk}

## Background

Based on the structure of the encoded characters and the mention of ROT13, a popular Letter Substitution Cipher, it is likely that we will find our flag by manipulating the characters. What kind of Cipher will we use since we cannot use ROT13? The Hint rescues us yet again by specifying that we will use The Caesar Cipher...

## Procedure

**Step #1:** First, we need to understand that The Caesar Cipher works by shifting letters in the alphabet by a fixed number [Left or Right]. For example, shifting "b" to the Left by 1 gives "a", and Right by 1 gives "c"...

**Step #2:** Since the shift is unknown, we need to brute force all possible values. You are right. This is quite cumbersome. There are two ways to go about this. You can write a Bash/Python Script that does this for you, or you can use Trial and Error on an online Caesar Cipher tool like [https://cryptii.com/pipes/caesar-cipher](https://cryptii.com/pipes/caesar-cipher)...

**Step #3:** If you used the online tool, then simply paste the encrypted characters in the "Cyphertext" box and increase the number of shifts until the "Plaintext" matches the format of flags in TryHackMe. The number of shifts at the time of docuemnting this was 19 but yours could be different...

## Conclusion

This task focused on Cryptography, specifically Substitution Ciphers which are The Caesar Cipher and ROT13. The fun fact is that ROT13 is a special case of The Caesar Cipher wheer the number of shifts is exactly 13. It is time for us to crush Task #10...
