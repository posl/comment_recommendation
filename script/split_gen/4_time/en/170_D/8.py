def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_a = a[-1]
    count = 0
    for i in range(1, max_a + 1):
        flag = True
        for j in range(n):
            if a[j] % i == 0:
                if a[j] // i == i:
                    continue
                else:
                    flag = False
                    break
        if flag:
            count += 1
    print(count)
