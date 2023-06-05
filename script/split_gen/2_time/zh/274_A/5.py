def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r_c = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    q_d = [list(input().split()) for _ in range(q)]
    d = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
    r_s, c_s = r_s - 1, c_s - 1
    r_c = [[r - 1, c - 1] for r, c in r_c]
    r_c.sort(key=lambda x: (x[0], x[1]))
    r_c.append([h, w])
    r_c.insert(0, [-1, -1])
    s = 0
    for i in range(1, len(r_c)):
        s += (r_c[i][0] - r_c[i - 1][0] - 1) * (r_c[i][1] - r_c[i - 1][1] - 1)
    print(s)
    for d_i, l_i in q_d:
        d_i = d[d_i]
        l_i = int(l_i)
        r, c = r_s, c_s
        while l_i > 0:
            if d_i[0] == 0:
                if r + d_i[1] == -1 or r + d_i[1] == h:
                    break
                elif [r + d_i[1], c] in r_c:
                    break
                else:
                    r += d_i[1]
            else:
                if c + d_i[0] == -1 or c + d_i[0] == w:
                    break
                elif [r, c + d_i[0]] in r_c:
                    break
                else:
                    c += d_i[0]
            l_i -= 1
        print(r + 1, c + 1)
