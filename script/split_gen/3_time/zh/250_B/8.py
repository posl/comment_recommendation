def main():
    n,a,b=map(int,raw_input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0:
                        print '.',
                    else:
                        print '#',
                print
            print
main()
