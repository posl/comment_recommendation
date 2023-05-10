def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            j = N // i
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans-1)
