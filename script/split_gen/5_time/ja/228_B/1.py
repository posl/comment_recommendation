def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = -1
    count = 1
    for i in range(n):
        if a[i] == -1:
            continue
        else:
            while True:
                if a[i] == -1:
                    break
                else:
                    i = a[i] - 1
                    count += 1
    print(count)
