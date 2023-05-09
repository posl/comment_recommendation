def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(m) < 4:
        print('Heisei')
    elif int(d) <= 30:
        print('Heisei')
    else:
        print('TBD')
