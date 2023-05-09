def main():
    N = int(input())
    i = 1
    while i*(i+1) <= 2*N:
        i += 1
    print(2*N-i*(i-1))
