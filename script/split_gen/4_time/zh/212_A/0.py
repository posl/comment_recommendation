def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print("黄金")
    elif A == 0 and 0 < B:
        print("白银")
    else:
        print("合金")
