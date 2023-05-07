def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1,1000):
        A = i
        B = i ** 5 - X
        if B ** 5 == A:
            break
    print(A,B)
