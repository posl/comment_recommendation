def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        A.append(b)
    if X in A:
        print("Yes")
    else:
        print("No")
