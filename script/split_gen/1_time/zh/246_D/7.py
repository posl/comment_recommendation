def judge(n):
    for a in range(100):
        for b in range(100):
            if n == a**3+a**2*b+a*b**2+b**3:
                return True
    return False
n = int(input())
while True:
    if judge(n):
        print(n)
        break
    else:
        n += 1
