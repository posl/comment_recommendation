def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    N_bin = list(N_bin)
    N_bin = [int(i) for i in N_bin]
    N_bin = N_bin[::-1]
    ans = []
    for i in range(60):
        if N_bin[i] == 1:
            ans.append(2**i)
    ans.append(2**60)
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()