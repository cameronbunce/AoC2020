# looking for trees in a big map
# grab out input


with open("input") as f:
   mapraw = list(f)

map = []

for line in mapraw:
   map.append(list(line[0:-1]))

# never used the function
# anywho, now we have to check other slopes

treecount = []
width = len(map[0])
print(width)
#for i in range(1, len(map)):
#   y = (i*3)%width
#   if ( map[i][y] == '#' ):
#      treecount = treecount+1

def check(r, d):
   x, y, count = 0, 0, 0

   while x < len(map):
      print(x, y)
#      input()
      if (map[x][y] == '#'):
         count = count + 1
      x = x+d
      y = (y+r) % width
   return count

treecount.append(check(1,1))
treecount.append(check(3,1))
treecount.append(check(5,1))
treecount.append(check(7,1))
treecount.append(check(1,2))

print(treecount)

out = treecount[0]*treecount[1]*treecount[2]*treecount[3]*treecount[4]
print(out)



