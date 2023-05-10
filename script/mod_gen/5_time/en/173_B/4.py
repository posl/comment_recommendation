def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print('AC x ' + str(S.count('AC')))
    print('WA x ' + str(S.count('WA')))
    print('TLE x ' + str(S.count('TLE')))
    print('RE x ' + str(S.count('RE')))

if __name__ == '__main__':
    main()