def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum < b_sum:
        print(0)
        return
    else:
        diff = a_sum - b_sum
        count = 0
        for i in range(n-1,-1,-1):
            diff -= (a[i] - b[i])
            count += 1
            if diff < 0:
                break
        print(count)
        return
