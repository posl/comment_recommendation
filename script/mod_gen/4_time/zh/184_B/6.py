def main():
    N, X = map(int, input().split())
    S = input()
    result = X
    for i in range(N):
        if S[i] == 'o':
            result += 1
        else:
            if result > 0:
                result -= 1
    print(result)

if __name__ == '__main__':
    main()