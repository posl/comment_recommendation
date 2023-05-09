def is_rururun(n):
    if n < 10:
        return True
    n_str = str(n)
    for i in range(1, len(n_str)):
        if abs(int(n_str[i]) - int(n_str[i-1])) > 1:
            return False
    return True
k = int(input())
cnt = 0
i = 0
while cnt < k:
    i += 1
    if is_rururun(i):
        cnt += 1
print(i)
