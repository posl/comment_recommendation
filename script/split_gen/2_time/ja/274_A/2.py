def main():
    A, B = map(int, input().split())
    C = B / A
    D = round(C, 3)
    print('{:.3f}'.format(D))
