def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if len(set(str(i)) - set(['7', '5', '3'])) == 0:
            ans += 1
    print(ans)
