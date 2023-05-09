def main():
    S = input()
    K = int(input())
    n = 0
    for i in range(len(S)):
        if S[i] != '1':
            n = i
            break
    if n == 0:
        print(S[K-1])
    else:
        if K <= n:
            print('1')
        else:
            print(S[n])

if __name__ == '__main__':
    main()