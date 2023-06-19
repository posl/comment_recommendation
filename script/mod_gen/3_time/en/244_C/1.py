def main():
    n = int(input())
    a = [0] * (2 * n + 2)
    for i in range(1, 2 * n + 2):
        print(i)
        a[i] = 1
        j = int(input())
        if j == 0:
            return
        a[j] = 1
main()
