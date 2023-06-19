def s(n):
    return sum([int(i) for i in str(n)])
n = int(input())
print("Yes" if n % s(n) == 0 else "No")
