def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(y) == 2019:
        if int(m) < 4:
            print('Heisei')
        elif int(m) == 4:
            if int(d) <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')
