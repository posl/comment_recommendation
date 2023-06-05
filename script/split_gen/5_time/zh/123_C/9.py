def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = A
    if min > B:
        min = B
    if min > C:
        min = C
    if min > D:
        min = D
    if min > E:
        min = E
    print(int(4 + (N + min - 1) / min))
