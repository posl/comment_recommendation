def main():
    n = int(input())
    k = len(str(n))
    if k == 1:
        if n % 3 == 0:
            print(0)
        else:
            print(-1)
        return
    for i in range(1, k):
        for j in range(k - i):
            if int(str(n)[j:i + j]) % 3 == 0:
                print(i)
                return
    print(-1)
    return
