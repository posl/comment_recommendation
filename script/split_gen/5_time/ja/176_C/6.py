def solve(n, a):
    # ここに処理を追加してください
    #print(a)
    max = 0
    sum = 0
    for i in range(n-1):
        if a[i] > max:
            max = a[i]
        if a[i+1] < max:
            sum += max - a[i+1]
    return sum
