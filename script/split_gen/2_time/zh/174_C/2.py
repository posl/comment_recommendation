def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    count = 0
    for i in range(1, k):
        count = count * 10 + 7
        count %= k
        if count == 0:
            print(i)
            return
    print(-1)
