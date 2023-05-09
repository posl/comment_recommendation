def main():
    K, X = [int(i) for i in input().split()]
    if 500*K >= X:
        print("Yes")
    else:
        print("No")
