def main():
    n = int(input())
    k = 0
    res = 1
    while True:
        if res > n:
            break
        res *= 2
        k += 1
    print(k-1)
