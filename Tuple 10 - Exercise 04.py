print('Enter four numbers from one to ten.')
x = int(input('First: '))
while x not in range(1, 11):
    x = int(input('Choose a number from one to ten: '))
y = int(input('Second: '))
while y not in range(1, 11):
    y = int(input('Choose a number from one to ten: '))
z = int(input('Third: '))
while z not in range(1, 11):
    z = int(input('Choose a number from one to ten: '))
b = int(input('Fourth: '))
while b not in range(1, 11):
    b = int(input('Choose a number from one to ten: '))

t = (x, y, z, b)
print(f'The following tuple was formed: {t}')

print(f'The number nine appear {t.count(9)} times.')

if 3 in t:
    print(f'The position of first three is {t.index(3)}')
elif 3 not in t:
    print('There is no number three.')

even = 0
t2 = []
for cont in range(0, 4):
    if (t[cont] % 2) == 0:
        even += 1
        t2.append(t[cont])
print(f'There are {even} even numbers and they are: {t2}')
