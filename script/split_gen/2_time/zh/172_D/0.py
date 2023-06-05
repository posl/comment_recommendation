def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum + b_sum <= k:
        print(n+m)
        return
    time = k
    count = 0
    i = 0
    j = 0
    while time >= 0 and i < n and j < m:
        if a[i] <= b[j]:
            time -= a[i]
            count += 1
            i += 1
        else:
            time -= b[j]
            count += 1
            j += 1
    while time >= 0 and i < n:
        time -= a[i]
        count += 1
        i += 1
    while time >= 0 and j < m:
        time -= b[j]
        count += 1
        j += 1
    print(count-1)
