def main():
    N = input()
    if len(N) == 3:
        print(N)
    elif len(N) == 2:
        print("".join([N[0],N[0],N[0]]))
    elif len(N) == 1:
        print("".join([N, N, N]))
