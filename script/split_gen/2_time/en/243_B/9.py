def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(zip(A, B))
    A_set = set(A)
    B_set = set(B)
    print(len(A_set & B_set))
    print(len(C) - len(A_set | B_set))
