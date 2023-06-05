def main():
    #input
    n, m, x, t, d = map(int, input().split())
    #n, m, x, t, d = 38, 20, 17, 168, 3
    #n, m, x, t, d = 1, 0, 1, 3, 2
    #n, m, x, t, d = 100, 10, 100, 180, 1
    #init
    h = t
    for i in range(x+1, m):
        h += d
    for i in range(m+1, n+1):
        h += d
    #print
    print(h)
