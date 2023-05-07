def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] + S[j] == 777:
                result += 1
    print(result)

if __name__ == '__main__':
    main()