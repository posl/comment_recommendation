def main():
    k = int(input())
    #print(k)
    if k%2 == 0:
        print((k//2)**2)
    else:
        print((k//2)*(k//2+1))

if __name__ == '__main__':
    main()