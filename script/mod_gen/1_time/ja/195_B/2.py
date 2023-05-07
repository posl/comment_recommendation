def main():
    A, B, W = map(int, input().split())
    W *= 1000
    if W % B == 0:
        min = W // B
    else:
        min = W // B + 1
    max = W // A
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()