# CA172-P912




Using lists we can maybe assign a suitable value to each coordinate.

So  say we have the grid:
C C A
B D C
C C C

The way we iterate through the grid for values is as such:
● ○ ○   ● ● ○   ● ● ●   ● ● ●   ● ● ●
○ ○ ○   ● ○ ○   ● ● ○   ● ● ●   ● ● ●
○ ○ ○   ○ ○ ○   ● ○ ○   ● ● ○   ● ● ●


(Refer to problem for variable assignment of each pipe and position:
https://open.kattis.com/problems/piperotation)

C in the corner must be assigned the key c2. Therefore
{(0,0):"c2"}

╭ ○ ○
○ ○ ○   Valid so far
○ ○ ○

Since 0,0 is c2, that means that 0,1 must be b1 and 1,0 must be c3.

{(0,0):"c2", (0,1):"b1", (1,0):"c3"}

╭ ╮ ○
| ○ ○   Valid so far
○ ○ ○

Then when we do the next iteration of, both of the corner values are ok, but we run into a problem at (1,1).

╭ ╮ 
| ┼ ○   Invalid
╰ ○ ○

A coordinate assigned a value of d cannot have a b1 adjacent to it on the X axis, making this invalid.
