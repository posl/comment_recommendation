def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if s[i] == 4 * j * k + 3 * j + 3 * k:
                    break
            else:
                continue
            break
        else:
            count += 1
    print(count)
