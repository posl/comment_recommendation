def main():
    n, q = map(int, input().split())
    s = input()
    ac = [0] * n
    for i in range(n-1):
        ac[i+1] = ac[i]
        if s[i] == 'A' and s[i+1] == 'C':
            ac[i+1] += 1
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r-1] - ac[l-1])

if __name__ == '__main__':
    main()