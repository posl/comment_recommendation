def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        t = t % 3
        k -= 1
        if t == 1:
            s = s[k:] + s[:k]
        elif t == 2:
            s = s[k:] + s[:k]
            s = s.replace('A', 'b').replace('B', 'c').replace('C', 'a')
        print(s[0])

if __name__ == '__main__':
    main()