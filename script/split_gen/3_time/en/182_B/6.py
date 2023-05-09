def main():
    N = int(input())
    A = list(map(int, input().split()))
    gcdness = [0] * 1000
    for a in A:
        for i in range(2, a + 1):
            if a % i == 0:
                gcdness[i - 1] += 1
    print(gcdness.index(max(gcdness)) + 1)
