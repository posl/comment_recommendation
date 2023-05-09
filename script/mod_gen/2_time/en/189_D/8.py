def main():
    N=int(input())
    S=input()
    if S=="OR":
        print(2**N)
    else:
        print(2**(N-1))

if __name__ == '__main__':
    main()