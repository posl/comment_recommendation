def main():
    n = int(input())
    if n % 3 == 0:
        print(0)
        return
    k = len(str(n))
    for i in range(1, k):
        for j in range(k):
            if i & (1 << j):
                n1 = n
                n1 = n1 // (10 ** j)
                n1 = n1 % (10 ** (k - 1))
                if n1 % 3 == 0:
                    print(i)
                    return
    print(-1)
