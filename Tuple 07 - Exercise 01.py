tuple = 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',\
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
while True:
        n = int(input('Enter a number from 0 to 20: '))
        while n not in range(0,21):
                n = int(input('Enter a number from 0 to 20: '))
        print(f'The number you chose in full is: {tuple[n]}')
        c = input('Do you wanna repeat?[y/n] ').upper().strip()
        while c not in 'YN':
                c = input('Do you wanna repeat?[y/n] ').upper().strip()
        if c == 'N':
                break
print('The program has ended.')