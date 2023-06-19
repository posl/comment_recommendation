def problem147_a():
    a = input()
    a = a.split()
    sum = 0
    for i in a:
        sum += int(i)
    if sum >= 22:
        print('bust')
    else:
        print('win')
