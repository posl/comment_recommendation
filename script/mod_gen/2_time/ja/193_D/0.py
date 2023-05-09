def main():
    K = int(input())
    S = input()
    T = input()
    s = [0]*10
    t = [0]*10
    for i in range(4):
        s[int(S[i])] += 1
        t[int(T[i])] += 1
    s[0] = t[0] = K
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            s[i] -= 1
            t[j] -= 1
            if s[i] < 0 or t[j] < 0:
                s[i] += 1
                t[j] += 1
                continue
            win = 0
            for k in range(1, 10):
                s[k] += 1
                t[k] += 1
                a = 0
                b = 0
                for l in range(1, 10):
                    a += l*10**s[l]
                    b += l*10**t[l]
                if a > b:
                    win += 1
                s[k] -= 1
                t[k] -= 1
            s[i] += 1
            t[j] += 1
            ans += win/((s[i]+1)*(t[j]+1))
    print(ans)

if __name__ == '__main__':
    main()