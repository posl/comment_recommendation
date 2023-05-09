def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    maxA = max(A)
    maxA_index = A.index(maxA)
    for i in range(N):
        if i == maxA_index:
            A.remove(maxA)
            print(max(A))
            A.insert(maxA_index, maxA)
        else:
            print(maxA)

if __name__ == '__main__':
    main()