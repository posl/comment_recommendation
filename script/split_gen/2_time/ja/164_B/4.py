def main():
    A, B, C, D = map(int, input().split())
    if (C-1) // B >= (A-1) // D:
        print('Yes')
    else:
        print('No')
