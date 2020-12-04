# Passport processor

# I was getting a low number from my first attempt

# referencing
# https://github.com/womogenes/AoC-2020-solutions/blob/main/4/4.1.py
# I saw that he was handling the input in a way that might be cleaner

# this works now using his input method, these top three lines
# the rest is my other solution adapted to this input.

# Now for part 2
# We need to verify input, so I'll build out individual
# rule checkers for the different fields

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
#     print(a) Hit EOF, gonna try to catch it the lazy way
      try:
         newdict[a[0]] = a[1]
      except:
         error = IndexError
   passports[i] = newdict
   i = i+1

print(len(passports))

# leaving this alone for now
def isvalid(test):
   if ((((((('byr' in test) and
             'iyr' in test) and
             'eyr' in test) and
             'hgt' in test) and
             'hcl' in test) and
             'ecl' in test) and
             'pid' in test):
      # I like keeping the base level check for the quick escape
      if (((((((check_byr(test['byr'])) and
                check_iyr(test['iyr'])) and
                check_eyr(test['eyr'])) and
                check_hgt(test['hgt'])) and
                check_hcl(test['hcl'])) and
                check_ecl(test['ecl'])) and
                check_pid(test['pid'])):
                   return True
      else:
                   return False
   else:
      return False
# (Birth Year) - four digits; at least 1920 and at most 2002.
def check_byr(byr):
   if len(byr) == 4:
      try:
         n = int(byr)
         if (n > 1919) and (n < 2003):
            return True
         else:
            # out of range
            return False
      except:
         # not a number
         error = ValueError
         return False
   else:
      # wrong length
      return False

# (Issue Year) - four digits; at least 2010 and at most 2020.
def check_iyr(iyr):
   if len(iyr) == 4:
      try:
         n = int(iyr)
         if (n > 2009) and (n < 2021):
            return True
         else:
            # out of range
            return False
      except:
         # not a number
         error = ValueError
         return False
   else:
      # wrong length
      return False



# (Expiration Year) - four digits;
#                     at least 2020 and at most 2030.
def check_eyr(eyr):
   if len(eyr) == 4:
      try:
         n = int(eyr)
         if (n > 2019) and (n < 2031):
            return True
         else:
            # out of range
            return False
      except:
         # not a number
         error = ValueError
         return False
   else:
      # wrong length
      return False



#(Height) - a number followed by either cm or in:
#    If cm, the number must be at least 150 and at most 193.
#    If in, the number must be at least 59 and at most 76.
def check_hgt(hgt):
   units = ('cm', 'in')
   # slice it up
   unit = hgt[-2:]
   base = hgt[:-2]
   if unit in units:
      if unit == 'cm':
         # check for numberability
         try:
            a = int(base)
            # check centimeter range
            if ( a > 149 ) and ( a < 194 ):
               return True
         except:
            error = ValueError
            return False
      else:
         # check range for inches
         try:
            a = int(base)
            if ( a > 58 ) and ( a < 77 ):
               return True
         except:
            error = ValueError
            return False
   else:
      # units didn't work out
      return False

# (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def check_hcl(hcl):
   hexdigits = '0123456789abcdefABCDEF'
   if len(hcl) == 7:
      if hcl[0] == '#':
         hcl = hcl[1:]
         for i in hcl:
            if i in hexdigits:
               pass
            else:
               # got something that wasn't valid hex
               return False
         # if it made it through the for loop, it's good
         return True
      else:
         # doesn't start with #
         return False
   else:
      # wrong number of digits
      return False

# (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def check_ecl(ecl):
   good = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
   return ecl in good

# (Passport ID) - a nine-digit number, including leading zeroes.
def check_pid(pid):
   if len(pid) == 9:
      try:
         n = int(pid)
         return True
      except:
         # doesn't work as a number
         error = ValueError
         return False
   else:
      # wrong length
      return False

goodones = []

for one in passports:
   if isvalid(one):
      goodones.append(one)

print(len(goodones))
