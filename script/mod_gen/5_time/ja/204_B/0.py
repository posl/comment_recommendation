def harvest():
    N = int(input())
    A = list(map(int, input().split()))
    harvest = 0
    for a in A:
        if a > 10:
            harvest += a - 10
    return harvest
print(harvest())

if __name__ == '__main__':
    harvest()