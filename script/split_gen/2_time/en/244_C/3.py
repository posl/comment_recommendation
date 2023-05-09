def main():
    N = int(input())
    arr = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 1):
        print(i)
        arr[i] = 1
        j = int(input())
        if j == 0:
            break
        arr[j] = 1
