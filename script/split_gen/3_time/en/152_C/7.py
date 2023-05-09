def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = n
    for i in p:
        if i <= min:
            ans += 1
            min = i
    print(ans)
