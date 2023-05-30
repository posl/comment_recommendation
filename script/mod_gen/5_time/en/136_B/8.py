def find_odd_digits(N):
    odd_digits = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 != 0:
            odd_digits += 1
    return odd_digits
N = int(input())
print(find_odd_digits(N))
