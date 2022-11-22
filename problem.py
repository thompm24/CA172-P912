#!/usr/bin/env python3

n = input().split()

x = int(n[0])
y = int(n[1])

yx = [[]]

i = 0
while i < x + 1:
   yx[0].append("A")
   i = i + 1

i = 1
while i < y + 1:
   s = input()
   yx.append(["A"])
   j = 0
   while j < x:
      yx[i].append(s[j])
      j= j + 1
   i = i + 1

"""
Now we have a 2d map we can iterate through using y and x coordinates respectively like yx[y][x]
This map is comprised of a border of A values across the top and down the left. This makes it so
that we don't need to treat corners of map provided by user specially, and they will obey same
rules as every other tile
"""


d = {}
i = 0
while i < len(yx):
   j = 0
   while j < len(yx[0]):
      d[(0, j)] = "a1"
      j = j + 1
   d[(i, 0)] = "a1"
   i = i + 1

"""
All of the A values we put in at border are now defined in dictionary as a1, as {(0,0):"a1"}
"""

i = 0
while i < len(yx):
   print(yx[i])
   i = i + 1
#This is just printing out our map, does not contribute to problem.


"""
List of possible relations which will not work:
Negative:
No connection from right:
a1, b1, c3, c4
Try connect to their left:
B2, c3, c4, d1

No connection downwards:
A1, b2, c1, c4
Try connect upwards:
B1, c1, c4, d1

Positive:
Try connect right:
B2, c1, c2, d1
Wont connect left:
A1, b1,  c1, c2

Try  connect down:
B1, c2, c3, d1
Wont connect up:
A1, b2, c2, c3
"""
