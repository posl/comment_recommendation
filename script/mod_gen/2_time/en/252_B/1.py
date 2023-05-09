def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()
    for i in range(K):
        if A[-1] == B[i]:
            A.pop()
        else:
            break
    if len(A) > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()