def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = (s[i] - 3) // 3
        b = (s[i] - 4) // 4
        if a < 1 or b < 1:
            continue
        if s[i] == 4 * a * b + 3 * a + 3 * b:
            continue
        else:
            count += 1
    print(count)
