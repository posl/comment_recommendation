def main():
    n = int(input())
    k = len(str(n))
    if n % 3 == 0:
        print(0)
        return
    for i in range(1, k):
        for j in range(0, k):
            if i + j > k:
                break
            if int(str(n)[j:j + i]) % 3 == 0:
                print(i)
                return
    print(-1)
