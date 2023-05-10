def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        exit()
    else:
        x = 1
        for i in range(1, k+1):
            x = x * 10 % k
            if x == 0:
                print(i)
                exit()
