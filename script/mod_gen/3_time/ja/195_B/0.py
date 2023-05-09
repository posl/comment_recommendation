def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if W % B != 0:
        min += 1
    if W % A != 0:
        max -= 1
    if min <= max:
        print(min, max)
    else:
        print("UNSATISFIABLE")

if __name__ == '__main__':
    main()