def main():
    N,L = map(int,input().split())
    a = [i for i in range(L,L+N)]
    print(sum(a)-min(a,key=abs))

if __name__ == '__main__':
    main()