def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    print(int(''.join(N[0:len(N)//2])) * int(''.join(N[len(N)//2:])))
