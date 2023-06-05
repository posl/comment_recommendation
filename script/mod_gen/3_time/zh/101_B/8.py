def check(n):
    s = 0
    for i in str(n):
        s += int(i)
    return n % s == 0
n = int(input())
print("Yes" if check(n) else "No")
