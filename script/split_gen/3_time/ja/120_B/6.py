def main():
    a, b, k = map(int, input().split())
    x = 0
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            x += 1
            if x == k:
                print(i)
                break
