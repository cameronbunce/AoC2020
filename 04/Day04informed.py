# Passport processor

# I was getting a low number from my first attempt

# referencing
# https://github.com/womogenes/AoC-2020-solutions/blob/main/4/4.1.py
# I saw that he was handling the input in a way that might be cleaner

# this works now using his input method, these top three lines
# the rest is my other solution adapted to this input.

with open("input") as f:
   input = f.read()

passports = input.split("\n\n")

i = 0
while i < len(passports):
   passports[i] = passports[i].replace("\n", " ")
   passports[i] = passports[i].split(' ')
   newdict = {}
   for x in passports[i]:
      a = x.split(':')
#      print(a) Hit EOF, gonna try to catch it the lazy way
      try:
         newdict[a[0]] = a[1]
      except:
         error = IndexError
   passports[i] = newdict
   i = i+1

print(len(passports))

def isvalid(test):
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
