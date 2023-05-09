def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    else:
        if k == 1:
            print(1)
            return
        else:
            for i in range(1, k):
                if (i * (i + 1)) % k == 0:
                    print(i + 1)
                    return
