def main():
    N = int(input())
    num = N
    count = 0
    while num != 0:
        count += 1
        num = int(num/10)
    ans = 0
    for i in range(1, 2 ** count):
        a = 0
        b = 0
        for j in range(count):
            if i & (1 << j) != 0:
                a = a * 10 + N // (10 ** j) % 10
            else:
                b = b * 10 + N // (10 ** j) % 10
        ans = max(ans, a * b)
    print(ans)
