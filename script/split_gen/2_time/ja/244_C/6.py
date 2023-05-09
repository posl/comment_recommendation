def main():
    N = int(input())
    a = [i for i in range(1, 2 * N + 2)]
    for i in range(1, 2 * N + 2):
        print(a[i])
        b = int(input())
        a.remove(b)
        if b == 0:
            break
