def main():
    a,b,c,d,e,k = [int(input()) for i in range(6)]
    print(":(" if e-a > k else "Yay!")

if __name__ == '__main__':
    main()