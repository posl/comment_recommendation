def main():
    N = int(input())
    declared = [False] * (2 * N + 2)
    for i in range(1, 2 * N + 2):
        print(i)
        declared[i] = True
        aoki = int(input())
        if aoki == 0:
            break
        declared[aoki] = True
