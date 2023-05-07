def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    C = A + B
    if len(str(C)) == len(str(A)) and len(str(C)) == len(str(B)):
        print('Easy')
    else:
        print('Hard')
