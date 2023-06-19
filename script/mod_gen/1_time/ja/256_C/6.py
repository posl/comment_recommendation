def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                if h[0] == i+j+k and h[1] == i+2*j+3*k and h[2] == 4*i+5*j+6*k:
                    if w[0] == i+4*j and w[1] == j+5*k and w[2] == k+6*i:
                        ans += 1
    print(ans)
main()
