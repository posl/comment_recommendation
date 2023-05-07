def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
    else:
        ans = 7 % K
        for i in range(1, 10**6):
            if ans == 0:
                print(i)
                break
            else:
                ans = (ans * 10 + 7) % K
        else:
            print(-1)
