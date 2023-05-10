def main():
    # N = int(input())
    # S = []
    # for i in range(N):
    #     S.append(input())
    N = 6
    S = ['AC', 'TLE', 'AC', 'AC', 'WA', 'TLE']
    C = [0, 0, 0, 0]
    for i in range(N):
        if S[i] == 'AC':
            C[0] += 1
        elif S[i] == 'WA':
            C[1] += 1
        elif S[i] == 'TLE':
            C[2] += 1
        elif S[i] == 'RE':
            C[3] += 1
    print('AC x {}'.format(C[0]))
    print('WA x {}'.format(C[1]))
    print('TLE x {}'.format(C[2]))
    print('RE x {}'.format(C[3]))

if __name__ == '__main__':
    main()