def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if not '7' in str(i) and not '7' in oct(i)[2:]:
            ans += 1
    print(ans)
