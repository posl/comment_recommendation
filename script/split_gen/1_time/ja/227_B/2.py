def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = (S[i] - 3) // 3
        b = (S[i] - 3) // 3
        if 4 * a * b + 3 * a + 3 * b != S[i]:
            count += 1
    print(count)
