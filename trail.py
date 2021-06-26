li = ['amit','bisht','zyx','amit']

l = set()
no = []
for i in li:
    print(li.count(i))
    l.add((i,li.count(i)))


print(l)