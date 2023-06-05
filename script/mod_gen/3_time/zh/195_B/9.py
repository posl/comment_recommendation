def main():
    A,B,W = map(int, input().split())
    W = W * 1000
    min = 0
    max = 0
    if W % A == 0:
        min = W // A
    else:
        min = W // A + 1
    if W % B == 0:
        max = W // B
    else:
        max = W // B
    if min > max:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()