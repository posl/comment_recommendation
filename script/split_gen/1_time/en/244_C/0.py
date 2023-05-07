def main():
    N = int(input())
    used = [False] * (2 * N + 2)
    for i in range(1, 2 * N + 2):
        print(i)
        used[i] = True
        j = int(input())
        if j == 0:
            return
        used[j] = True
    return
main()
