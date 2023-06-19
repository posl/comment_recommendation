def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(abs(x) + abs(y))
    if max(A) > max(x, y):
        print("No")
        return
    if x == 0 and y == 0:
        print("Yes")
        return
    if x == 0 or y == 0:
        if 1 in A:
            print("Yes")
        else:
            print("No")
        return
    for i in range(N-1):
        if A[i] == 1 and A[i+1] == 1:
            print("Yes")
            return
    print("No")
    return
main()
