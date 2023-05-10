def main():
    L = int(input())
    L = L-12
    if L < 0:
        print(0)
        return
    ans = 1
    for i in range(1, 12+L):
        ans *= i
    for i in range(1, L+1):
        ans //= i
    for i in range(1, 12):
        ans //= i
    print(ans)
