def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    if k % 5 == 0:
        print(-1)
        return
    if k == 1:
        print(1)
        return
    if k == 7:
        print(1)
        return
    for i in range(1,k):
        if (pow(10,i) - 1) % k == 0:
            print(i+1)
            return
    print(-1)
    return
