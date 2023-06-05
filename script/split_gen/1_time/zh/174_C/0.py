def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    else:
        x = 7
        for i in range(1, k + 1):
            if x % k == 0:
                print(i)
                return
            else:
                x = 10 * x + 7
        print(-1)
        return
