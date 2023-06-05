def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t = t % sum(a)
    for i in range(n):
        if t >= a[i]:
            t -= a[i]
        else:
            print(i+1, t)
            break
