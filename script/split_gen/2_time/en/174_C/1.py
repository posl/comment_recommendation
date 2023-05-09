def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7 % k
        for i in range(k):
            if x == 0:
                print(i + 1)
                break
            x = (x * 10 + 7) % k
