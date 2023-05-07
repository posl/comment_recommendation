def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    if len(N) == 2:
        print(N[0] * N[1])
    else:
        N.sort(reverse=True)
        print(N[0] * N[1])
