def main():
    L1, R1, L2, R2 = map(int, input().split())
    if L2 <= R1 and R1 <= R2:
        print(R1 - L2)
    elif L1 <= R2 and R2 <= R1:
        print(R2 - L1)
    else:
        print(0)
