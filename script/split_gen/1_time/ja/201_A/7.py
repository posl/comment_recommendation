def main():
    A = list(map(int, input().split()))
    if A[0] == A[1] == A[2]:
        print('Yes')
        return
    if A[0] == A[1] or A[1] == A[2] or A[0] == A[2]:
        print('No')
        return
    if A[0] + A[2] == 2 * A[1]:
        print('Yes')
        return
    print('No')
