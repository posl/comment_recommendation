def main():
    A, B = input().split()
    A = int(A)
    B = float(B)
    B = int(B * 100 + 0.5)
    print(A * B // 100)
