def main():
    n = int(input())
    used = [0] * (2 * n + 2)
    for i in range(1, 2 * n + 2):
        print(i)
        used[i] = 1
        if i == 1:
            continue
        a = int(input())
        if a == 0:
            return
        used[a] = 1
        if a == 2 * n + 1:
            print(2 * n + 2)
            return
        if used[a - 1] == 0:
            print(a - 1)
            return
        if used[a + 1] == 0:
            print(a + 1)
            return
main()
