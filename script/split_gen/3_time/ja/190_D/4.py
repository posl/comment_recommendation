def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0 and (N//i-i) % 2 == 1:
            ans += 1
    print(ans*2)
