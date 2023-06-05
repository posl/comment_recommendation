def problem119_a():
    s = input()
    s1 = s.split('/')
    if int(s1[1]) < 5:
        print('Heisei')
    else:
        print('TBD')

if __name__ == '__main__':
    problem119_a()