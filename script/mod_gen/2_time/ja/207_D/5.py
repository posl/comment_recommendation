def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        for o in range(4):
                            for p in range(4):
                                for q in range(4):
                                    for r in range(4):
                                        for a in range(4):
                                            for b in range(4):
                                                for c in range(4):
                                                    for d in range(4):
                                                        s2 = [[s[j][0],s[j][1]] for j in range(n)]
                                                        t2 = [[t[j][0],t[j][1]] for j in range(n)]
                                                        for j in range(n):
                                                            s2[j][0] += i
                                                            s2[j][1] += j
                                                        for j in range(n):
                                                            s2[j][0] += k
                                                            s2[j][1] += l
                                                        for j in range(n):
                                                            s2[j][0] += m
                                                            s2[j][1] += o
                                                        for j in range(n):
                                                            s2[j][0] += p
                                                            s2[j][1] += q
                                                        for j in range(n):
                                                            s2[j][0] += r
                                                            s2[j][1] += a
                                                        for j in range(n):
                                                            s2[j][0] += b
                                                            s2[j][1] += c
                                                        for j in range(n):
                                                            s2[j][0] += d
                                                        s2.sort()
                                                        t2.sort()
                                                        if s2 == t2:
                                                            print("Yes")
                                                            return
    print("No")

if __name__ == '__main__':
    main()