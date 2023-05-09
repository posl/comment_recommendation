def main():
    N = input()
    N = list(N)
    N = list(map(int, N))
    N.sort(reverse=True)
    a = N.pop(0)
    b = 0
    for i in range(len(N)):
        b = b * 10 + N[i]
    print(a * b)
main()
