def main():
    K = int(input())
    ans = []
    n = 1
    while len(ans) < K:
        if n % sum(map(int, str(n))) == 0:
            ans.append(n)
        n += 1
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()