def main():
    k = int(input())
    n = 7
    for i in range(1, k+1):
        if n % k == 0:
            print(i)
            return
        n = (n * 10 + 7) % k
    print(-1)
