def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_a_index = A.index(max_a)
    max_b = max(B)
    max_b_index = B.index(max_b)
    if max_a_index == max_b_index:
        if max_a >= max_b:
            print(1)
        else:
            print(0)
    else:
        if max_a >= max_b:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()