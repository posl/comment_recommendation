def main():
    N = int(input())
    ans = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
        i += 1
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()