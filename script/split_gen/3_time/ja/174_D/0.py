def main():
    N = int(input())
    c = input()
    ans = 0
    for i in range(N-1):
        if c[i] == 'R' and c[i+1] == 'W':
            ans += 1
    print(ans)
