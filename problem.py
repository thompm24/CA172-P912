#!/usr/bin/env python3

n = input().split()

x = int(n[0])
y = int(n[1])

xy = []

i = 0
while i < y:
   s = input()
   xy.append([])
   j = 0
   while j < x:
      xy[i].append(s[j])
      j= j + 1
   i = i + 1

print(xy)

print(xy[0][0])


#a
#b1 b2
#c1 c2 c3 c4
#d

if xy[0][0] == 
