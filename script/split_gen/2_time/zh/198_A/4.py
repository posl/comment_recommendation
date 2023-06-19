def share_candy(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count
n = int(input())
print(share_candy(n))
