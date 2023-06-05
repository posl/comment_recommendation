def main():
    A,B = input().split()
    A = int(A)
    B = int(B)
    if A % B == 0:
        print(A+B)
    else:
        print(B-A)
