def solve():
    h, w, n = map(int, input().split())
    hlist = [0] * h
    wlist = [0] * w
    for i in range(n):
        a, b = map(int, input().split())
        hlist[a-1] += 1
        wlist[b-1] += 1
    hlist = [i for i in range(h) if hlist[i] == 0]
    wlist = [i for i in range(w) if wlist[i] == 0]
    hlist = [i+1 for i in range(h) if hlist[i] != 0]
    wlist = [i+1 for i in range(w) if wlist[i] != 0]
    for i in range(n):
        print(hlist[i], wlist[i])

if __name__ == '__main__':
    solve()