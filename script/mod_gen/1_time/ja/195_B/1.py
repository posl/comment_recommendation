def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_n = W // B
    max_n = W // A
    if W % B != 0:
        min_n += 1
    if W % A != 0:
        max_n -= 1
    if min_n > max_n:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)
main()

if __name__ == '__main__':
    main()