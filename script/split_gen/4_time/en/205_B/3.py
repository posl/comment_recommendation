def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == [i for i in range(1, N+1)]:
        print("Yes")
    else:
        print("No")
