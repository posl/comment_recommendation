def main():
    AB = input().split()
    A = int(AB[0])
    B = int(AB[1])
    CD = input().split()
    C = int(CD[0])
    D = int(CD[1])
    while True:
        C = C - B
        if C <= 0:
            print("Yes")
            break
        A = A - D
        if A <= 0:
            print("No")
            break
