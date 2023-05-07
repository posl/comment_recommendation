def main():
    A, B = map(int, input().split())
    if A % 2 == 0:
        if B % 2 == 0:
            print((A ^ B) ^ B)
        else:
            print((A ^ B) ^ A)
    else:
        if B % 2 == 0:
            print(A ^ B)
        else:
            print(A ^ B ^ A)
