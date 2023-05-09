def main():
    N = int(input())
    S = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += S[i]
    if sum % 10 != 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()