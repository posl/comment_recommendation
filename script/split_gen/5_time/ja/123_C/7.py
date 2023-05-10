def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    ans = N // min(A, B, C, D, E)
    if N % min(A, B, C, D, E) != 0:
        ans += 1
    ans += 4
    print(ans)
