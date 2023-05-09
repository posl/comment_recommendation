def main():
    N = input()
    N = [int(i) for i in N]
    N.sort(reverse=True)
    print(N[0]*N[1])

if __name__ == '__main__':
    main()