def main():
    A, B = map(int, input().split())
    K = (A + B) // 2
    if A == B:
        print(K)
    else:
        print("IMPOSSIBLE")
