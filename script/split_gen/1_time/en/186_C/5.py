def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        else:
            ans += 1
    print(ans)
