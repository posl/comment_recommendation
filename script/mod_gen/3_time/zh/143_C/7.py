def main():
    N = int(input())
    S = input()
    num = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            num += 1
    print(num)

if __name__ == '__main__':
    main()