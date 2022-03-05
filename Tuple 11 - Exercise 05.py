products = ('Book', 10, 'Scissors', 1, 'Pencil', 0.5, 'Paper', 5, 'Eraser', 0.25, 'Backpack', 20)

print('-'*40, '\n', f'{"LIST OF PRODUCTS":^40}', '\n', '-'*40)

for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end='')
    else:
        print(f' $ {products[pos]:>5.2f}')

print('-'*40)


