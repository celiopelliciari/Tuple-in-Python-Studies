from random import randint

r = tuple(randint(1, 50) for i in range(5))
print(f'The tuple is {r}')

smallest = min(r)
higher = max(r)

print(f'The smallest number is {smallest} and the higher is {higher}')
