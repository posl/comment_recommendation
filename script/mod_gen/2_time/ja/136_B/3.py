def main():
    N = int(input())
    even = 0
    odd = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(odd)

if __name__ == '__main__':
    main()