def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort(reverse=True)
    print(N[0] * N[1])
