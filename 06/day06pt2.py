with open("input") as f:
   fin = f.read()

groups = fin.split('\n\n')

total = 0
def dedupe(alist):
   return list(dict.fromkeys(alist))

for group in groups:
   items = dedupe(list(group))
   people = len(group.split('\n'))
   group = list(group)

   try:
      items.remove('\n')
   except:
      error = ValueError
   for item in items:
      if group.count(item) == people:
         total = total + 1


print(total)


