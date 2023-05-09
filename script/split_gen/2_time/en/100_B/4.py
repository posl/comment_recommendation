def main():
    D, N = list(map(int, input().split()))
    if D == 0:
        print(N)
    elif D == 1:
        print(N*100)
    else:
        print(N*10000)
