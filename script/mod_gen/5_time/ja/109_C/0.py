def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n, x = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.append(x)
x_list.sort()
diff = [x_list[i + 1] - x_list[i] for i in range(n)]
ans = diff[0]
for i in range(1, n):
    ans = gcd(ans, diff[i])
print(ans)

if __name__ == '__main__':
    gcd()