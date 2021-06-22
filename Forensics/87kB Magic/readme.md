### Forensics/87kB Magic
![Screenshot](plank.png)
Corrupted files are such a headache..

Author: SolvedPack#1949
#### Writeup

Use binwalk, which shows there is only zip footer no header. This means the zip header is corrupted. Correct the magic numbers (Header bytes) then extract using '-e' flag on binwalk. The extracted zip contains a text file with the flag

flag : **csoc{C@n_y0U_wa1K_7H3_B1NArY?}**