def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i
        if ans >= N:
            print(i)
            break
