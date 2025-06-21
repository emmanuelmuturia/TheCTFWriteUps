# Task #19: Uncrackable!

Can you solve the following? By the way, I lost the key. Sorry >.<

MYKAHODTQ{RVG_YVGGK_FAL_WXF}

Flag format: TRYHACKME{FLAG IN ALL CAP}

## Background

Task #9 had a similar pattern, right? The Hint tells us that this is part of The Viegenere Cipher. How do we find the key, though?

## Procedure

**Step #1:** Give each letter a number using the alphabet: `A = 0, B = 1, C = 2, ..., Z = 25`...

**Step #2:** Take the Cipher Letter and subtract the Plain Letter [what it should be...]...

**Step #3:** If the result is negative, just add 26 to keep it in the A–Z range...

**Step #4:** Convert the final number back to a letter. That is one letter of the key...

**Step #5:** In our case we take the first letter of the Ciphertext [M -> 12], subtract the first letter of the Plaintext [T -> 19], get -7, add 26 to get 19, map 19 to the letter 'T' which is now the first letter of our key, and repeat for all of the respective letters...

**Step #6:** We will get the repeating pattern of "THMTHMTHM..." which means that "THM" is our key and it gives us the flag. You can use an online Vigenere Cipher tool for this part...

## Conclusion

This task was based on Cryptography, specifically Polyalphabetic Substitution Ciphers. The Vigenere Cipher uses multiple shifts [based on a key] to avoid Frequency Analysis Attacks that break simple Caesar Ciphers and was considered "unbreakable" until Frequency Patterns and Key Length Guesses were developed to crack it. Are you ready for Task #20?
