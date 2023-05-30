def main():
    n = int(input())
    used = [False] * (2 * n + 1)
    for i in range(1, 2 * n + 2):
        used[i] = True
        print(i)
        a = int(input())
        if a == 0:
            return
        used[a] = True
main()
