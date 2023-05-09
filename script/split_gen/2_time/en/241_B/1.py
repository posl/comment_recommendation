def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    for b in B:
        if A[-1] < b:
            print("No")
            return
        while A[-1] > b:
            A.pop()
        A.pop()
    print("Yes")
