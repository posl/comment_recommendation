def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = []
    for s in S:
        if s in ans:
            ans.append(s + '(' + str(ans.count(s)) + ')')
        else:
            ans.append(s)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()