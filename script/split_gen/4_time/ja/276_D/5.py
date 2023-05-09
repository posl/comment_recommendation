def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        b = [i for i in a if i % 2 == 0]
        if len(b) == len(a):
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    while True:
        c = [i for i in a if i % 3 == 0]
        if len(c) == len(a):
            a = [i // 3 for i in a]
            ans += 1
        else:
            break
    if len(set(a)) == 1:
        print(ans)
    else:
        print(-1)
