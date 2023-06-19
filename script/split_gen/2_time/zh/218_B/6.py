def main():
    p = list(map(int, input().split()))
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in p:
        ans += alpha[i-1]
    print(ans)
