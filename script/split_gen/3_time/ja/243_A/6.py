def main():
    V, A, B, C = map(int, input().split())
    if V % A == 0 or V % B == 0 or V % C == 0:
        print('T')
    else:
        print('F')
