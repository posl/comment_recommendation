def main():
    n = int(input())
    w = [input() for i in range(n)]
    for i in range(1,n):
        if w[i-1][-1] != w[i][0] or w[i] in w[:i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()