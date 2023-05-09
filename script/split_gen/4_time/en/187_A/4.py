def main():
    A, B = map(int, input().split())
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))
