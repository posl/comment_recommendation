def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('AC x ' + str(s.count('AC')))
    print('WA x ' + str(s.count('WA')))
    print('TLE x ' + str(s.count('TLE')))
    print('RE x ' + str(s.count('RE')))

if __name__ == '__main__':
    main()