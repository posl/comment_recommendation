def main():
    N, A, B = map(int, input().split())
    if A == 0 or B == 0:
        print(0)
        return
    if A + B > N:
        print(0)
        return
    if A + B == N:
        print(1)
        return
    if A + B < N:
        print((N - (A + B)) // (A + B) + 1)
        return
