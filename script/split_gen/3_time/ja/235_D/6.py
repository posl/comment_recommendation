def count(a, n, count):
    if n == 1:
        return count
    elif n % a == 0:
        return count(a, n / a, count + 1)
    elif n % 10 != 0:
        return count(a, int(str(n % 10) + str(n // 10)), count + 1)
    else:
        return -1
a, n = map(int, input().split())
print(count(a, n, 0))
