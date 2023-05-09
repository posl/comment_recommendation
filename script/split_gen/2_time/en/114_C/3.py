def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            ans += 1
    print(ans)
