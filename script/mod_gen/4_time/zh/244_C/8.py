def main():
    n = int(input())
    used = [False] * (2 * n + 2)
    for i in range(n):
        a = int(input())
        used[a] = True
        b = int(input())
        if b == 0:
            break
        used[b] = True
        for j in range(1, 2 * n + 2):
            if not used[j]:
                print(j)
                used[j] = True
                break
    return

if __name__ == '__main__':
    main()