def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print('存在不满足的字符串')
            return
    print('可满足')

if __name__ == '__main__':
    main()