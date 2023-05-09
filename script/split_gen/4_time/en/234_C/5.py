def main():
    K = int(input())
    ans = 0
    for i in range(1, 1000000):
        if '2' in str(i):
            ans += 1
            if ans == K:
                print(i)
                exit()
