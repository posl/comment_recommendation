def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == "R":
            count += 1
    print(min(count, N - count))

if __name__ == '__main__':
    main()