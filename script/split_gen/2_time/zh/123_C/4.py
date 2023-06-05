def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(E)
    time = 0
    time += (A % 10) * 10
    time += (B % 10) * 10
    time += (C % 10) * 10
    time += (D % 10) * 10
    time += (E % 10) * 10
    print(time)
