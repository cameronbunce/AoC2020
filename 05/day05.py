with open("input") as f:
   fin = f.read()

bpasses = fin.split('\n')

highest = 0

seats = []
for i in range(128):
   row = []
   for j in range(8):
      row.append(((i*8)+j))
   seats.append(row)

def fb(bpass, plane):
   # print(bpass)
   # print(plane)
   # input()
   try:
      i = bpass[0]
   except:
      error = IndexError
      return plane

   bpass = bpass[1:]
   if i == 'F':
      # take the front slice
      h = int((len(plane))/2)
      # print(h)
      plane = plane[0:h]
      return fb(bpass, plane)

   elif i == 'B':
      # take the back slice
      plane = plane[int(len(plane)/2):]
      return fb(bpass, plane)

   elif i == 'L':
      plane = plane[0:int(((len(plane))/2))]
      return fb(bpass, plane)

   elif i == 'R':
      print(plane)
      plane = plane[int(len(plane)/2):]
      return fb(bpass, plane)

   elif i == '':
      return plane[0]

print(fb("FBFBBFFRLR", seats))
