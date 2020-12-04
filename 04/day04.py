# Passport Scanner

# The expected fields are as follows:

#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)


# cid is optional, the rest are mandatory

# passports are separated by blank lines

with open("input") as f:
   input = list(f)

# read input until you get to just a newline
# trim passport of newlines,
# concatenate,
# and then separate on spaces, key:value pairs?

i = 0
passport = []
passports = []

while i < len(input):
   if not ( input[i] == '\n' ):
      passport.append(input[i])
   else:
      passports.append(passport)
      passport = []
   i = i + 1

# clean up the newlines:

i = 0
while i < len(passports):
   pout = []
   for p in passports[i]:
      p = p[0:-1]
      pout.append(p)
   holdinglist = (" ".join(pout)).split(' ')
   newdict = {}
   for x in holdinglist:
      a = x.split(':')
      newdict[a[0]] = a[1]
   passports[i] = newdict
   i = i + 1

# print(passports[0])

def isvalid(test):
#   if len(test) < 7:
#      return False
#   else:
#      pass
#
# Nah, not doing lists, in case I need to work on them more
# I made the passports dictionaries
# so this is gong to be a long one-liner
   return ((((((('byr' in test) and
                 'iyr' in test) and
                 'eyr' in test) and
                 'hgt' in test) and
                 'hcl' in test) and
                 'ecl' in test) and
                 'pid' in test)


goodones = []

for one in passports:
   if isvalid(one):
      goodones.append(one)

print(len(goodones))

