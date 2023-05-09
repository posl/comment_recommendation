def main():
    #S = input()
    #T = input()
    #A, B = [int(x) for x in input().split()]
    #U = input()
    S = "red"
    T = "blue"
    A = 3
    B = 4
    U = "red"
    if S == U:
        A -= 1
    elif T == U:
        B -= 1
    print(A, B)
