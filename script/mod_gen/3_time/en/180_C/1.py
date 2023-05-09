def main():
    n = int(input())
    ans = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()