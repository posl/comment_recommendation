def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rcs = []
    for i in range(N):
        rcs.append(list(map(int, input().split())))
    Q = int(input())
    dls = []
    for i in range(Q):
        dls.append(list(input().split())))
    for i in range(Q):
        d = dls[i][0]
        l = int(dls[i][1])
        if d == "L":
            for j in range(l):
                if cs - 1 in [rcs[k][1] for k in range(N)]:
                    break
                cs -= 1
        elif d == "R":
            for j in range(l):
                if cs + 1 in [rcs[k][1] for k in range(N)]:
                    break
                cs += 1
        elif d == "U":
            for j in range(l):
                if rs - 1 in [rcs[k][0] for k in range(N)]:
                    break
                rs -= 1
        elif d == "D":
            for j in range(l):
                if rs + 1 in [rcs[k][0] for k in range(N)]:
                    break
                rs += 1
        else:
            print("error")
        print(rs, cs)
    return
