def problem145_b():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[0:N//2] == S[N//2:N]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    problem145_b()