def main():
    K = int(input())
    result = 0
    for i in range(1,K+1):
        if i%2 == 0:
            result += (K//2)
        else:
            result += ((K+1)//2)
    print(result)

if __name__ == '__main__':
    main()