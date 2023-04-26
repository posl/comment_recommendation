Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    sum_h = h1 + h2 + h3
    sum_w = w1 + w2 + w3
    if sum_h != sum_w:
        print(0)
        return
    else:
        sum_h = sum_h // 3
        sum_w = sum_w // 3
    if h1 != w1:
        print(0)
        return
    if h1 + h2 != w1 + w2:
        print(0)
        return
    if h1 + h2 + h3 != w1 + w2 + w3:
        print(0)
        return
    if h1 + h3 != w1 + w3:
        print(0)
        return
    if h1 + h2 + h3 != sum_h * 3:
        print(0)
        return
    if h1 + h2 != sum_h * 2:
        print(0)
        return
    if h1 != sum_h:
        print(0)
        return
    if h1 + h3 != sum_h * 2:
        print(0)
        return
    if h1 + h2 + h3 != sum_w * 3:
        print(0)
        return
    if h1 + h2 != sum_w * 2:
        print(0)
        return
    if h1 != sum_w:
        print(0)
        return
    if h1 + h3 != sum_w * 2:
        print(0)
        return
    if h1 + h2 + h3 != sum_w * 3:
        print(0)
        return
    if h1 + h2 != sum_w * 2:
        print(0)
        return
    if h1 != sum_w:
        print(0)
        return
    if h1 + h3 != sum_w * 2:
        print(0)
        return

    if h1 == w1:
        if h1 + h2 == w1 + w2:
            if h1 + h2 + h3 == w1 + w2 + w3:
                if h1 + h3 == w1 + w3:
                    print(1)
                    return

=======
Suggestion 2

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if i + j + k == h1 and i + k + j == h2 and j + k + i == h3 and i + j + k == w1 and i + k + j == w2 and j + k + i == w3:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    count = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if h1 == i + j + k and w1 == i + j + k:
                    for l in range(1, 31):
                        for m in range(1, 31):
                            for n in range(1, 31):
                                if h2 == l + m + n and w2 == l + m + n:
                                    for o in range(1, 31):
                                        for p in range(1, 31):
                                            for q in range(1, 31):
                                                if h3 == o + p + q and w3 == o + p + q:
                                                    if i + l + o == j + m + p == k + n + q:
                                                        count += 1
    print(count)

=======
Suggestion 4

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, 31):
        for b in range(1, 31):
            for c in range(1, 31):
                for d in range(1, 31):
                    for e in range(1, 31):
                        for f in range(1, 31):
                            for g in range(1, 31):
                                for i in range(1, 31):
                                    for j in range(1, 31):
                                        if h1 == a + b + c and h2 == d + e + f and h3 == g + i + j and w1 == a + d + g and w2 == b + e + i and w3 == c + f + j:
                                            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, h1 + 1):
        for j in range(1, h2 + 1):
            for k in range(1, h3 + 1):
                for l in range(1, w1 + 1):
                    for m in range(1, w2 + 1):
                        for n in range(1, w3 + 1):
                            if i + j + k == h1 and i + l + m == w1 and j + m + n == w2 and k + l + n == w3:
                                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for a in range(1, 30):
        for b in range(1, 30):
            for c in range(1, 30):
                for d in range(1, 30):
                    for e in range(1, 30):
                        for f in range(1, 30):
                            for g in range(1, 30):
                                for i in range(1, 30):
                                    for j in range(1, 30):
                                        if a + b + c == h1 and d + e + f == h2 and g + i + j == h3 and a + d + g == w1 and b + e + i == w2 and c + f + j == w3:
                                            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for h4 in range(1, 31):
        for h5 in range(1, 31):
            for h6 in range(1, 31):
                for w4 in range(1, 31):
                    for w5 in range(1, 31):
                        for w6 in range(1, 31):
                            if h1 == h4 + h5 + h6 and h2 == h4 + h5 + h6 and h3 == h4 + h5 + h6:
                                if w1 == w4 + w5 + w6 and w2 == w4 + w5 + w6 and w3 == w4 + w5 + w6:
                                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    print(solve(h1,h2,h3,w1,w2,w3))

=======
Suggestion 9

def check(h, w):
    for i in range(3):
        if sum(h[i]) != h[i][3]:
            return False
    for i in range(3):
        if sum(w[i]) != w[i][3]:
            return False
    return True

=======
Suggestion 10

def get_num_list():
    return list(map(int, input().split()))
