t = 'steel', 'ball', 'car', 'passport', 'computer', 'tuple', 'python'
l = ''
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'

for count in range(0, len(t)):
    if a in t[count]:
        l += a
    if e in t[count]:
        l += e
    if i in t[count]:
        l += i
    if o in t[count]:
        l += o
    if u in t[count]:
        l += u
    print(f'The word {t[count]} has {l} vowels.')
    l = ''

