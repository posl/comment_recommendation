def main():
    N = int(input())
    declared = [0] * (2 * N + 2)
    for i in range(1, 2 * N + 2):
        print(i)
        declared[i] = 1
        j = int(input())
        if j == 0:
            return
        declared[j] = 1
main()
