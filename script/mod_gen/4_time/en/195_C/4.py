def main():
    N = int(input())
    if N < 1000:
        print(0)
        return
    if N < 10**6:
        print(N-999)
        return
    if N < 10**9:
        print(2*(N-10**6+1)+10**3-999)
        return
    if N < 10**12:
        print(3*(N-10**9+1)+2*(10**6-10**3+1)+10**3-999)
        return
    if N < 10**15:
        print(4*(N-10**12+1)+3*(10**9-10**6+1)+2*(10**6-10**3+1)+10**3-999)
        return

if __name__ == '__main__':
    main()