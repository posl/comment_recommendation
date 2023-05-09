def main():
    H1, W1 = map(int, input().split())
    A = [[int(i) for i in input().split()] for j in range(H1)]
    H2, W2 = map(int, input().split())
    B = [[int(i) for i in input().split()] for j in range(H2)]
    print("Yes" if A.count(B) > 0 else "No")
