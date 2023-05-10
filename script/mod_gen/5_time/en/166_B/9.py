def main():
    input = raw_input().split()
    N = int(input[0])
    K = int(input[1])
    A = []
    for i in range(0, K):
        input2 = raw_input().split()
        A.append(input2[1:])
    A = [int(i) for j in A for i in j]
    print N - len(set(A))

if __name__ == '__main__':
    main()