def main():
    N = int(input())
    for i in range(N, 10**18+1):
        if (i**(1/3)).is_integer():
            print(i)
            exit()
