def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A, B, C, D, E)
    ans = 5 + (N - 1) // min_num
    print(ans)
