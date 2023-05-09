def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #最も移動時間が短い交通機関を探す
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    print((N + min - 1) // min + 4)

if __name__ == '__main__':
    main()