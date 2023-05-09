def main():
    n,k = map(int, input().split())
    ans = n
    while True:
        if ans > abs(ans-k):
            ans = abs(ans-k)
        else:
            print(ans)
            exit()
