def main():
    N = int(input())
    A = list(map(int, input().split()))
    gcd = [0] * 1001
    for a in A:
        for i in range(2, a + 1):
            if a % i == 0:
                gcd[i] += 1
    print(gcd.index(max(gcd)))
