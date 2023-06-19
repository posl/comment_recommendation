def check(n):
    if n<10:
        return True
    else:
        n_str = str(n)
        n_len = len(n_str)
        if n_len % 2 == 0:
            n_len_half = int(n_len/2)
            n_str_half_1 = n_str[0:n_len_half]
            n_str_half_2 = n_str[n_len_half:n_len]
            if n_str_half_1 == n_str_half_2:
                return True
            else:
                return False
        else:
            return False
N = int(input())
count = 0
for i in range(1,N+1):
    if check(i):
        count += 1
print(count)
