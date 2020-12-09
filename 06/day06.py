with open("input") as f:
   fin = f.read()

groups = fin.split('\n\n')

total = 0
def dedupe(alist):
   return list(dict.fromkeys(alist))

for group in groups:
   group = dedupe(list(group))
   try:
      group.remove('\n')
   except:
      error = ValueError
   total = total + len(group)


print(total)


