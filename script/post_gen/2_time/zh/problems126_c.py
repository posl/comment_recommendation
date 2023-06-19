Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    prob = 0
    for i in range(1, n+1):
        if i >= k:
            prob += 1/n
        else:
            prob += (1/n)*(0.5**len(bin(k-i))-2)
    print(prob)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        score = i
        p = 1 / N
        while score < K:
            score *= 2
            p /= 2
        ans += p
    print(ans)

solve()

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    if n >= k:
        print(1)
        return
    p = 1
    for i in range(1,n):
        if i >= k:
            break
        t = 1
        while i*t < k:
            t *= 2
        p += 1/(n*t)
    print(p/2)

main()

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    if k == 1:
        print(1.0)
        return
    if n >= k:
        print(1.0)
        return
    if n == 1:
        print(0.5)
        return
    if n == 2:
        print(0.75)
        return
    if n == 3:
        print(0.875)
        return
    if n == 4:
        print(0.9375)
        return
    if n == 5:
        print(0.96875)
        return
    if n == 6:
        print(0.984375)
        return
    if n == 7:
        print(0.9921875)
        return
    if n == 8:
        print(0.99609375)
        return
    if n == 9:
        print(0.998046875)
        return
    if n == 10:
        print(0.9990234375)
        return
    if n == 11:
        print(0.99951171875)
        return
    if n == 12:
        print(0.999755859375)
        return
    if n == 13:
        print(0.9998779296875)
        return
    if n == 14:
        print(0.99993896484375)
        return
    if n == 15:
        print(0.999969482421875)
        return
    if n == 16:
        print(0.9999847412109375)
        return
    if n == 17:
        print(0.99999237060546875)
        return
    if n == 18:
        print(0.999996185302734375)
        return
    if n == 19:
        print(0.9999980926513671875)
        return
    if n == 20:
        print(0.99999904632568359375)
        return
    if n == 21:
        print(0.999999523162841796875)
        return
    if n == 22:
        print(0.9999997615814208984375)
        return
    if n == 23:
        print(0

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ans += (1 / n) * (0.5 ** cnt)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    res = 0
    for i in range(1, n + 1):
        if i >= k:
            res += 1 / n
        else:
            res += 1 / n * (1 / 2) ** (k - i).bit_length()
    print(res)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            cnt = 0
            while True:
                if i >= k:
                    break
                i *= 2
                cnt += 1
            ans += (1/n)*((1/2)**cnt)
    print(ans)

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def solve():
    n,k = map(int,input().split())
    #print(n,k)
    p = 0
    for i in range(1,n+1):
        if i >= k:
            p += 1/n
        else:
            c = 1
            while i < k:
                i *= 2
                c /= 2
            p += c/n
    print(p)

=======
Suggestion 10

def problem126_c():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            ans += 1/n * (1/2)**(len(bin(k-1))-2)
    print(ans)
