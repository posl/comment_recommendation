def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    #print(h)
    #print(w)
    ans = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                for l in range(1, 31):
                    for m in range(1, 31):
                        for n in range(1, 31):
                            for o in range(1, 31):
                                for p in range(1, 31):
                                    for q in range(1, 31):
                                        if i + j + k == h[0] and l + m + n == h[1] and o + p + q == h[2] and i + l + o == w[0] and j + m + p == w[1] and k + n + q == w[2]:
                                            ans += 1
    print(ans)
