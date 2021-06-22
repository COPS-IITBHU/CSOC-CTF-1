from itertools import permutations
import random
with open('flag.txt','r') as f:
    flag=list(f.read())
if len(flag)%2==1:
    flag.append(' ')
x = ['t', 'Y', 'w', 'V', '|', ']', 'u', 'X', '_', '0', 'P', 'k', 'h', 'D', 'A', '4', 'K', '5', 'z',
 'Z', 'G', '7', ';', 'S', ' ', '/', '6', '%', '}', '\\', ',', ':', '>', '#', 'a', '$', '3', '`',
 '+', 'R', 'b', 'H', 'd', 's', '1', 'J', 'L', 'v', '9', '2', 'o', 'M', '<', 'e', '(', 'x', '-',
 'B', 'm', "'", 'y', 'Q', '"', 'W', 'l', '.', 'i', 'O', '^', 'p', '8', 'f', 'F', 'C', '?', 'g',
 '@', 'j', '[', 'r', '!', '=', 'E', '~', '*', 'T', '{', ')', 'U', 'N', 'c', '&', 'n', 'q', 'I']
# print(flag)
for _ in range(20):
    for i in range(len(flag)):
        flag[i]=x[ord(flag[i])-32]
# print(flag)
random.seed(1337)
random.shuffle(flag)
# print(len(flag))
# perms=permutations(flag,5)
# output=[]
# for i,j in enumerate(perms):
#     if i==0:
#         for x in j:
#             output.append(x)
#     elif i<=23:
#         output.append(j[4])
# print(output)
# print(len(output))
output=''.join(output)
print(len(output))
out=open('output.txt','w')
out.write(output)

