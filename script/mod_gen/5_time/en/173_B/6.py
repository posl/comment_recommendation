def main():
    n = int(input())
    verdicts = []
    for i in range(n):
        verdicts.append(input())
    print('AC x ' + str(verdicts.count('AC')))
    print('WA x ' + str(verdicts.count('WA')))
    print('TLE x ' + str(verdicts.count('TLE')))
    print('RE x ' + str(verdicts.count('RE')))

if __name__ == '__main__':
    main()