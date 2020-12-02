with open("input") as f:
   passdb = list(f)

def isvalid(parsed):
   count = 0 
   low, high, key, passwd = parsed
   for a in passwd:
      if a == key:
         count = count + 1
   if low <= count <= high:
      return True
   else:
      return False

def rule2(parsed):
   low, high, key, passwd = parsed
   if (passwd[low-1] == key) ^ (passwd[high-1] == key):
      return True
   return False

def passparser(line):
   rule, key, passwd = line.split(' ')
   passwd = passwd[0:-1]
   key = key[0]
   low, high = rule.split('-')
   low = int(low)
   high = int(high)

   return low, high, key, passwd


valid = 0
valid2 = 0
for line in passdb:
   parsed = passparser(line)
   if isvalid(parsed):
      valid = valid + 1
   if rule2(parsed):
      valid2 = valid2 + 1
print(str(valid))
print(str(valid2))
