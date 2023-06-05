def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while 4 * a * b + 3 * a + 3 * b < S[i]:
            a += 1
            if 4 * a * b + 3 * a + 3 * b >= S[i]:
                break
            b += 1
            if 4 * a * b + 3 * a + 3 * b >= S[i]:
                break
        if 4 * a * b + 3 * a + 3 * b != S[i]:
            count += 1
    print(count)
