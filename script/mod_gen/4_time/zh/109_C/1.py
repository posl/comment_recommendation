def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, x = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(x)
x_list.sort()
diff_list = [x_list[i] - x_list[i-1] for i in range(1, n+1)]
diff_list.sort()
gcd_num = diff_list[0]
for i in range(1, n):
    gcd_num = gcd(gcd_num, diff_list[i])
print(gcd_num)
