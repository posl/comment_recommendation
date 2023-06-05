def main():
    a = input()
    A = a.split()
    for i in range(len(A)):
        A[i] = int(A[i])
    A.sort()
    if A[0] + A[1] + A[2] + A[3] >= 500:
        print(4)
    else:
        print(3)

if __name__ == '__main__':
    main()