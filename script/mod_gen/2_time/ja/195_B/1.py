def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_num = W // B
    max_num = W // A
    if W % B != 0:
        min_num += 1
    if W % A != 0:
        max_num -= 1
    if min_num > max_num:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

if __name__ == '__main__':
    main()