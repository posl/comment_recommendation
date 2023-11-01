def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(m) < 4:
