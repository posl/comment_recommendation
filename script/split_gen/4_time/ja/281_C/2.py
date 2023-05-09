def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    t = t % a_sum
    a_sum = 0
    for i in range(n):
        a_sum += a[i]
        if t < a_sum:
            print(i + 1, t)
            break
