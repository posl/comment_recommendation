def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    wall = set()
    for i in range(N):
        r, c = map(int, input().split())
        wall.add((r, c))
    Q = int(input())
    d = []
    l = []
    for i in range(Q):
        d_i, l_i = input().split()
        d.append(d_i)
        l.append(int(l_i))
    for i in range(Q):
        if d[i] == "L":
            while True:
                if (r_s, c_s - 1) in wall:
                    break
                else:
                    c_s -= 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "R":
            while True:
                if (r_s, c_s + 1) in wall:
                    break
                else:
                    c_s += 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "U":
            while True:
                if (r_s - 1, c_s) in wall:
                    break
                else:
                    r_s -= 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        if d[i] == "D":
            while True:
                if (r_s + 1, c_s) in wall:
                    break
                else:
                    r_s += 1
                    l[i] -= 1
                    if l[i] == 0:
                        break
        print(r_s, c_s)
