#!/usr/bin/env python3
                         # Parses 2 integer input into list of two elements
n = input().split()
                        

""" 
Proceeding code-block for producing X*Y matrix given the two inputs x and y
"""
                        



x = int(n[0])            # X = number of rows
y = int(n[1])            # Y = number of cells in row

yx = [[]]                # Currently empty list of lists (list 1: list of rows, list 2: list of cells within each row)

i = 0

while i < x + 1:         # Creates top layer of border values (border value = nothing tile, uniteractable)
   yx[0].append("a1")    # Entire first row in coordinate-mapping list is border values, row extends 1 more than the relevant coordinate-map 
   i = i + 1              

i = 1                    # i = 1 as the border row = 0, which doesn't accept inputs (tile coordinates), so index skips to first row in map

while i < y + 1:         # y + 1 as one extra iteration needed to add initial border cell to each row
   s = input()           # s accepts entire input line given (entire composition of row, i.e. what pattern is in which tile in the row)
   yx.append(["a1"])     # Border value is first cell of any row
   j = 0                 # Re-initializes j, so that function starts at first cell of any row 
   while j < x:
      yx[i].append(s[j])  # Appends the pattern which is contained in the current cell to current row
      j = j + 1           # Index j to access and append the next input/cell pattern to the current row
   i = i + 1              # Index i to move to appending the next row

i = 1

while i < len(yx):       # Iterates for as many rows as exist in map
   yx[i].append("A")     # Adds nothing tile to end of each row
   i = i + 1

yx.append(["a1"])        # Adds
i = 1
while i < len(yx[0]):
   yx[-1].append("A")
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
If so, then return that element.
"""

def inter(t, l, c):
   z = 0
   intersection = []
   while z < len(outp[("t", t)]):
      if outp[("t", t)][z] in outp[("l", l)]:
         intersection.append(outp[("t", t)][z])
      z = z + 1
   z = 0
   while z < len(rot[c]):
      if rot[c][z] in intersection:
         return rot[c][z]
      z = z + 1

print(inter(yx[0][1], yx[1][0], yx[1][1]))

"""
Then we must iterate through our matrix starting at yx[1][1] and run the function for each coordinate.
"""

#i = 1
#while i < len(yx):
#   j = 1
#   while j < len(yx[0]):
#      print(yx[i][j], (i,j))
#      yx[i][j] = inter(yx[i - 1][j], yx[i][j - 1], yx[i][j])
#      print(yx[i][j], (i,j))
#      j = j + 1
#   i = i + 1
"""
Finitooooo
"""
