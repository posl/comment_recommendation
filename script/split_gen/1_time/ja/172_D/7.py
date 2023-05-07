def get_divisor_list(x):
    divisor_list = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            divisor_list.append(i)
            if i != x // i:
                divisor_list.append(x // i)
        i += 1
    return divisor_list
N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i * len(get_divisor_list(i))
print(ans)
