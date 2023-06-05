def main():
    L, Q = map(int, input().split())
    mark = [0 for i in range(L+1)]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = L
            for j in range(x, -1, -1):
                if mark[j] == 1:
                    left = j
                    break
            for j in range(x, L+1):
                if mark[j] == 1:
                    right = j
                    break
            print(right-left)
