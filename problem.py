#!/usr/bin/env python3

n = input().split()

x = int(n[0])
y = int(n[1])

yx = [[]]

i = 0
while i < x + 1:
   yx[0].append("a1")
   i = i + 1

i = 1
while i < y + 1:
   s = input()
   yx.append(["a1"])
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


i = 0
while i < len(yx):
   print(yx[i])
   i = i + 1
#This is just printing out our map, does not contribute to problem.


"""
[a1,b2,c1,c4] on top  == [a1,b2,c2,c3] on bottom  |negative top |
[b1,c2,c3,d1] on top  == [b1,c1,c4,d1] on bottom  |positive top |

[a1,b1,c3,c4] on left == [a1,b1,c2,c4] on right   |negative left|
[b2,c1,c2,d1] on left == [b2,c3,c4,d1] on right   |positive left|

Notice that if we take an intersection of either one of the 2 sets for the top and left values,
there is only a max of one possible rotation for any ABCD cell.

Consider the following:
[positive top] ∩ [negative left] = [b2,c3]

Therefore, if we have a tile B beneath a positive top, say, c1, and to the right of a negative
left, say, c2, then the only possible rotation of B is b2. However, if the B was instead a D,


The only problem now is that on the far right or far bottom borders, we can not have a positive
left or positive top respectively. This can be solved with an if statement though.
"""

#negative top input etc.
nti = ["a1","b2","c1","c4"]
pti = ["b1","c2","c3","d1"]
nli = ["a1","b1","c3","c4"]
pli = ["b2","c1","c2","d1"]

#negative top output etc.
nto = ["a1","b2","c2","c3"]
pto = ["b1","c1","c4","d1"]
nlo = ["a1","b1","c2","c4"]
plo = ["b2","c3","c4","d1"]

outp = {}
i = 0
while i < 4:
   outp[("t", nti[i])] = nto
   outp[("t", pti[i])] = pto
   outp[("l", nli[i])] = nlo
   outp[("l", pli[i])] = plo
   i = i + 1

#We use ("t", "a1") to keep a1's corresponding tiles separate in dictionary based on if it's on top or on left


print(outp)
rot = {}
rot["A"] = ["a1"]
rot["B"] = ["b1", "b2"]
rot["C"] = ["c1","c2","c3","c4"]
rot["D"] = ["d1"]
#all possible rotations of each pipe type that we can check for intersection with output lists we made above




"""
We must make a list that will take in a top and left value (already written in a1 form), and check their intersecting pipe types.
We can do this by iterating through one dictionary definition list , and then using an if x in y statement
Then we must see if any element of rotation list is in that intersection

Steps:
def inter(t,l,c)
make intersection list between outp[("t",t)] and outp[("l",l)]
iterate through rot[c] and see if any element is in intersection list
if so, then change value at coordinate of c to that rotation, otherwise the pipe system is impossible 
"""

#def inter(t, l, c):
#   z = 0
#   intersection = []
#   while z < 0:
#      if outp[("t", t)]][z] in outp[("l", l):
#      lint.append(outp[("t", t)])
#      z = z + 1
#^^^^^Unfinished function ^^^^^^^^

"""
Then we must iterate through our matrix starting at yx[1][1] and run the function for each coordinate

We must then also make the test to make sure that all items across bottom and right of map are no positive top or positive left.
Otherwise instead of running test we could also make it so that instead of As just running across top  and bottom of grid, 
we make a frame of As.
"""


"""
Finitooooo
"""


