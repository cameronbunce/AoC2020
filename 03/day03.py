# looking for trees in a big map
# grab out input

with open("input") as f:
   mapraw = list(f)

map = []

for line in mapraw:
   map.append(list(line))

def istree(maybe):
   if maybe == '#':
      return True
   return False

treecount = 0
width = len(map[0])

for i in range(1, len(map)):
   y = (i*3)%width
   if ( map[i][y] == '#' ):
      treecount = treecount+1

print(treecount)


