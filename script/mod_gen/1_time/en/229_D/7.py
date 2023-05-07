def main():
    s = input()
    k = int(input())
    x = s.split('.')
    y = [len(i) for i in x]
    y.sort(reverse=True)
    print(y[0]-k if y[0]-k>0 else 0)

if __name__ == '__main__':
    main()