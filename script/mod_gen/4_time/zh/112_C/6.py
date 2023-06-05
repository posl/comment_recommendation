def solve():
    #N = int(input())
    #x,y,h = [],[],[]
    #for i in range(N):
    #    x.append(int(input()))
    #    y.append(int(input()))
    #    h.append(int(input()))
    #for cx in range(101):
    #    for cy in range(101):
    #        H = 0
    #        for i in range(N):
    #            if h[i] > 0:
    #                H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
    #                break
    #        flag = True
    #        for i in range(N):
    #            if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy), 0):
    #                flag = False
    #                break
    #        if flag:
    #            print(cx, cy, H)
    #            return
    #N = int(input())
    #x,y,h = [],[],[]
    #for i in range(N):
    #    x.append(int(input()))
    #    y.append(int(input()))
    #    h.append(int(input()))
    #for cx in range(101):
    #    for cy in range(101):
    #        H = -1
    #        for i in range(N):
    #            if h[i] > 0:
    #                H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
    #                break
    #        flag = True
    #        for i in range(N):
    #            if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy), 0):
    #                flag = False
    #                break
    #        if flag:
    #            print(cx, cy, H)
    #            return
    N = int(input())
    x,y,h = [],[],[]
    for i in range(N):
        x.append(int(input()))
        y.append(int(input()))
        h.append(int(input()))
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    break
            flag

if __name__ == '__main__':
    solve()