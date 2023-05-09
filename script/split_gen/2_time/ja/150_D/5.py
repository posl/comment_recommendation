def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i//2 for i in a]
    c = 1
    for i in a:
        while i % 2 == 0:
            i //= 2
            c *= 2
    ans = (m//c + 1)//2
    print(ans)
