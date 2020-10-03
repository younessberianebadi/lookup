# Lookup algorithm Implementation

This source code simulate a lookup algorithm based on a binary tree which routers use to store the FIBs (Forwarding information base) and search in them.

The project contains 5 script files:

## Fib.py

Contains a function called prefix_gene() which generates random ipv4 prefixes from a class passed to it as a parameter.

The next lines do the following :
- Creates a text file named FIB in write mode.
- Generate 4 more random addresses for the next-hop interfaces.
- Starts writing lines in the FIB.txt file in forrmat of : ip prefix - next-hop - output interfaces.

### Note: 

- There are 4 output interfaces S1, S2, S3 and S4.
- There are: 500 lines of A class ip prefixes, 300 B class ip prefixes, 200 C class ip prefixes and the default input.
- Creates a new files called Destination.txt and write 100 random ip addresses in it.

## tree.py

It includes two functions, the first uses the file FIB.txt to create the tree which is in a 2D list format and the second does the lookup of a particular address and matches it with a prefix entry from the FIB

## 100addresslookup.py

Relises a lookup of the 100 address from the Destination.txt file and writes the result in a new file named « Resultat du lookup.txt » which is french for lookup result.

## draw.py

Uses turtle library to draw the binary tree for the first 20 entries of the FIB.

![Tree drawing](/screenshots/draw.png)

## graphic.py

Create a GUI interface where the user can type an address and it searches for the input of that particular address.

![GUI](/screenshots/graphic.png)

---

This project was a school assignment for my 4th year in the engineering school and the project report is in the link below (Note: it is in french):

[Drive](https://drive.google.com/file/d/1pilfgAojEgyr-n0BN-WPuwqLDlqBsl_O/view?usp=sharing)
