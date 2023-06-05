def main():
    k = int(input())
    if k%2 == 0:
        print(-1)
        return
    if k%5 == 0:
        print(-1)
        return
    n = 7
    for i in range(1, k+1):
        if n%k == 0:
            print(i)
            return
        n = n*10+7
    print(-1)
    return
