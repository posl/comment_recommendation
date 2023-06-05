def main():
    k = int(input())
    mod = 7 % k
    for i in range(1, k + 1):
        if mod == 0:
            print(i)
            return
        mod = (mod * 10 + 7) % k
    print(-1)
