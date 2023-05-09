def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for b in B:
        if len(A) == 0:
            print("No")
            return
        if A[-1] < b:
            print("No")
            return
        while A[-1] > b:
            A.pop()
        A.pop()
    print("Yes")
