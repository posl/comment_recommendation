def main():
    N = int(input())
    a = [1, 2 * N + 1]
    for i in range(N):
        print(a[0])
        b = int(input())
        if b == 0:
            return
        if a[0] + 1 == b:
            a[0] += 2
        else:
            a[0] += 1
        print(a[1])
        b = int(input())
        if b == 0:
            return
        if a[1] - 1 == b:
            a[1] -= 2
        else:
            a[1] -= 1
    return
