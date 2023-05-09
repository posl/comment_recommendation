def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    count_same = 0
    count_diff = 0
    # 1. same position
    for i in range(N):
        if A[i] == B[i]:
            count_same += 1
    # 2. different position
    for i in range(N):
        for j in range(N):
            if i != j and A[i] == B[j]:
                count_diff += 1
    print(count_same)
    print(count_diff)

if __name__ == '__main__':
    main()