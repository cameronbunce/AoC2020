with open("input.txt") as f:
   expenses = list(f)


intexpenses = list()

for a in expenses:
   intexpenses.append(int(a))

i, n = 0, 1

length = len(intexpenses)
done = False
while i < length and not done:
   while n < length and not done:
      if intexpenses[i] + intexpenses[n] == 2020:
         print("Hit! "+str(intexpenses[i])+" "+str(intexpenses[n]))
         print(" - "+ str((intexpenses[i] * intexpenses[n])))
#         input()
         done = True
      else:
#         print(str(i)+" "+str(n))
         n = n+1
   i = i+1
   n = i+1


a, b, c = 1, 2, 3
done = False

while a < length and not done:
   while b < length and not done:
      while c < length and not done:
         if intexpenses[a] + intexpenses[b] + intexpenses[c] == 2020:
            print(str(intexpenses[a])+" "+str(intexpenses[b])+" "+str(intexpenses[c]))
            print(" *= "+str((intexpenses[a] * intexpenses[b] * intexpenses[c])))
            done = True
         else:
            c = c+1
      b = b+1
      c = b+1
   a = a+1
   b = a+1
   c = a+2
