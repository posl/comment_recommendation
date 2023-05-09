def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(n-1):
        if s[i] == "A" and s[i+1] == "C":
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i]
    for i in range(q):
        li, ri = map(int, input().split())
        print(l[ri-1] - l[li-1])

if __name__ == '__main__':
    main()