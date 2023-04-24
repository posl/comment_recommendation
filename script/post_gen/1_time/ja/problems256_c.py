Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    h = [h1, h2, h3]
    w = [w1, w2, w3]
    ans = 0
    for i in range(1, 30):
        for j in range(1, 30):
            for k in range(1, 30):
                if h[0] == i + j + k and w[0] == i + w[1] + w[2]:
                    if h[1] == i + w[1] + k and w[1] == j + w[2] + k:
                        if h[2] == i + j + w[2] and w[2] == j + w[1] + k:
                            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i in range(1, 31):
        for j in range(1, 31):
            for k in range(1, 31):
                if (i + j + k == h1 and i + k == w1 and j + k == w2 and i + j == w3):
                    ans += 1
    print(ans)

=======
Suggestion 3

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
                                        if h1 == a + b + c:
                                            if h2 == d + e + f:
                                                if h3 == g + i + j:
                                                    if w1 == a + d + g:
                                                        if w2 == b + e + i:
                                                            if w3 == c + f + j:
                                                                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    for i1 in range(1, h1):
        for i2 in range(1, h2):
            for i3 in range(1, h3):
                for j1 in range(1, w1):
                    for j2 in range(1, w2):
                        for j3 in range(1, w3):
                            if i1 + i2 + i3 == h1 and i1 + j1 + j2 + j3 == w1 and i2 + j1 + j2 == w2 and i3 + j1 + j3 == w3 and i1 + i2 + j1 == h2 and i2 + i3 + j2 == h3 and i1 + j1 + j3 == h3 and i3 + j2 + j3 == h3:
                                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1, h[0] + 1):
        for j in range(1, h[1] + 1):
            for k in range(1, h[2] + 1):
                for l in range(1, w[0] + 1):
                    for m in range(1, w[1] + 1):
                        for n in range(1, w[2] + 1):
                            if i + j + k == h[0] and i + l + m == h[1] and i + n + k == h[2] and j + l + n == w[0] and j + m + k == w[1] and n + m + l == w[2]:
                                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    h = list(map(int, input().split()))
    w = list(map(int, input().split()))
    ans = 0
    for i in range(1,31):
        for j in range(1,31):
            for k in range(1,31):
                if h[0] == i+j+k and h[1] == i+2*j+3*k and h[2] == 4*i+5*j+6*k and w[0] == i+4*j and w[1] == j+5*k and w[2] == k+6*i:
                    ans += 1
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, H[0]+1):
        for j in range(1, H[1]+1):
            for k in range(1, H[2]+1):
                if i + j + k == H[0] and i + j + k == H[1] and i + j + k == H[2]:
                    for l in range(1, W[0]+1):
                        for m in range(1, W[1]+1):
                            for n in range(1, W[2]+1):
                                if l + m + n == W[0] and l + m + n == W[1] and l + m + n == W[2]:
                                    if i + l == j + m and j + m == k + n and i + l == k + n:
                                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(h1 + h2 + h3 + w1 + w2 + w3 - 12)

=======
Suggestion 10

def main():
    #input
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    #compute
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
                                        if a+b+c==h1 and d+e+f==h2 and g+i+j==h3 and a+d+g==w1 and b+e+i==w2 and c+f+j==w3:
                                            ans += 1
                                        else:
                                            pass

    #output
    print(ans)
