with open("input") as f:
   passdb = list(f)

def isvalid(rule, key, passwd):
   passwd = passwd[0:-1]
   key = key[0]
   low, high = rule.split('-')
   low = int(low)
   high = int(high)

   count = 0 
   for a in passwd:
      if a == key:
         count = count + 1
   if low <= count <= high:
      return True
   else:
      return False

valid = 0

for line in passdb:
   a, b, c = line.split(' ')
   if isvalid(a, b, c):
      valid = valid + 1

print(str(valid))
