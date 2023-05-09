def main():
    n = int(input())
    n = bin(n)[2:]
    n = n[::-1]
    ans = []
    for i in range(len(n)):
        if n[i] == '1':
            ans.append(str(2**i))
    print('\n'.join(ans))

if __name__ == '__main__':
    main()