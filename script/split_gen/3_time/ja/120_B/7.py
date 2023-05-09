def main():
    a, b, k = map(int, input().split())
    i = 1
    ans = 0
    while True:
        if a % i == 0 and b % i == 0:
            ans += 1
            if ans == k:
                print(i)
                exit()
        i += 1
