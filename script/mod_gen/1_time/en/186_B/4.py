def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [a for a in A if sum(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    if len(A[0]) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a in A]
    A = [a for a in A if len(a) > 0]
    if len(A) == 0:
        print(0)
        return
    A = [[a for a in a if a > 0] for a

if __name__ == '__main__':
    main()