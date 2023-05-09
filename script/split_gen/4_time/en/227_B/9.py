def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for s in S:
        a = 0
        b = 0
        while a * b <= s:
            if 4 * a * b + 3 * a + 3 * b == s:
                count += 1
                break
            b += 1
            if a * b > s:
                a += 1
                b = 0
    print(N - count)
