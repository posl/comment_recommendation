def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, x = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(x)
x_list.sort()
diff = [x_list[i+1] - x_list[i] for i in range(n)]
gcd_value = diff[0]
for i in range(1, n):
    gcd_value = gcd(gcd_value, diff[i])
print(gcd_value)

if __name__ == '__main__':
    gcd()