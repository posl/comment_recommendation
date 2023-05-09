def search(n, a, b, c, l, mp):
    if n == len(l):
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return 1000000000
    mp1 = search(n + 1, a, b, c, l, mp)
    mp2 = search(n + 1, a + l[n], b, c, l, mp + 10)
    mp3 = search(n + 1, a, b + l[n], c, l, mp + 10)
    mp4 = search(n + 1, a, b, c + l[n], l, mp + 10)
    return min(mp1, mp2, mp3, mp4)
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(search(0, 0, 0, 0, L, 0))
8 1000 800 100
300
333
400
444
500
555
600
666
243

if __name__ == '__main__':
    search()