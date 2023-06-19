def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = {A[i]: i for i in range(N)}
    B = {B[i]: i for i in range(N)}
    same = 0
    diff = 0
    for a in A:
        if a in B:
            if A[a] == B[a]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)
main()
