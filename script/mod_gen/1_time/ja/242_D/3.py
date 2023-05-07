def solve():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        k -= 1
        for j in range(t):
            if s[k] == 'A':
                k //= 3
            elif s[k] == 'B':
                k = (k+len(s))//3
            else:
                k = (k+2*len(s))//3
        print(s[k])

if __name__ == '__main__':
    solve()