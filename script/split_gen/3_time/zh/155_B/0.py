def check(n, l):
    for i in range(n):
        if l[i] % 2 == 0:
            if l[i] % 3 != 0 and l[i] % 5 != 0:
                return False
    return True
n = int(input())
l = list(map(int, input().split()))
print("APPROVED" if check(n, l) else "DENIED")
