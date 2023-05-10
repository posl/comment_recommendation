def problems119_a():
    s = input()
    y, m, d = map(int, s.split('/'))
    if m <= 4:
        print('Heisei')
    else:
        print('TBD')
