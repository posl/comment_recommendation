def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            if i%2 == 1:
                ans += 1
            if N//i%2 == 1:
                ans += 1
            if i**2 == N:
                ans -= 1
    print(ans)
