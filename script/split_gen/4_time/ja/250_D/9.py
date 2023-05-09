def main():
    n = int(input())
    res = 0
    for i in range(2, 1000000):
        if n % i == 0:
            j = n // i
            if j % 2 == 0:
                res += 1
    print(res)
