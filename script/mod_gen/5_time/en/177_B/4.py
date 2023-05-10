def solve():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        c = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                c += 1
        if c < min:
            min = c
    print(min)
solve()

if __name__ == '__main__':
    solve()