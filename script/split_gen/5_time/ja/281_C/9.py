def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    t = t % a_sum
    for i in range(n):
        if t < a[i]:
            print(i+1, t)
            break
        t -= a[i]
