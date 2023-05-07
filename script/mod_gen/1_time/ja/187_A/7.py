def main():
    A, B = map(int, input().split())
    A = list(str(A))
    B = list(str(B))
    A_sum = 0
    B_sum = 0
    for i in A:
        A_sum += int(i)
    for i in B:
        B_sum += int(i)
    if A_sum > B_sum:
        print(A_sum)
    else:
        print(B_sum)

if __name__ == '__main__':
    main()