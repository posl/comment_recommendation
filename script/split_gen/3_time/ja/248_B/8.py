def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(k):
        if a >= b:
            break
        elif a % 2 == 0:
            a = a // 2
            b = b - a
            count += 1
        else:
            a = a // 2 + 1
            b = b - a
            count += 1
    print(count)
