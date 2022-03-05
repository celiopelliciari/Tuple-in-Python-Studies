teams = 'City', 'Liverpool', 'Chelsea', 'Manchester', 'West Ham', 'Arsenal', 'Tottenham', 'Wolves', 'Brighton',\
        'Leicester City', 'Aston Villa', 'Southampton', 'Crystal Palace', 'Brentford', 'Leeds', 'Everton', 'Norwich', \
        'Newcastle', 'Watford', 'Burnley'
while True:
    u = str(input('Choice one:'
                  '[A] Show the first five teams.'
                  '[B] Show the last four teams.'
                  '[C] Show a list in alphabetical order.'
                  '[D] What position is the determined team in.'
                  '[E] Exit.')).upper()
    while u not in 'ABCDE':
        u = str(input('Choice one:'
                      '[A] Show the first five teams.'
                      '[B] Show the last four teams.'
                      '[C] Show a list in alphabetical order.'
                      '[D] What position is the determined team in.'
                      '[E] Exit.')).upper()
    if u == 'A':
        for cont in range(0, 5):
             print(f'The {teams[cont]} team is in {cont+1}º position.')
    elif u == 'B':
        for cont in range(16, 20):
             print(f'The {teams[cont]} team is in {cont+1}º position.')
    elif u == 'C':
        print(sorted(teams))
    elif u == 'D':
        c = str(input('Choose a team to know your position: '))
        while c not in teams:
            c = str(input('Choose a team to know your position: '))
        print(f'The {c} is in {teams.index(c)+1}º position.')
    elif u == 'E':
        break
    f = str(input('Do you wanna repeat?[y/n] ')).upper().strip()
    while f not in 'Y''N':
        f = str(input('Do you wanna repeat?[y/n] ')).upper().strip()
    if f == 'N':
        break
print('The program has ended.')