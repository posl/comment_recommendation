def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_num = min(A, B, C, D, E)
    print((N + min_num - 1) // min_num + 4)
