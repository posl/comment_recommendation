def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        ans = 7 % k
        for i in range(1, 10**6):
            if ans == 0:
                print(i)
                exit()
            ans = (ans * 10 + 7) % k
        print(-1)
