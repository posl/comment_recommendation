def print_seq(n,m):
    if n == 1:
        for i in range(1,m+1):
            print i
    else:
        for i in range(1,m-n+2):
            for j in print_seq(n-1,m-i):
                print i,j

if __name__ == '__main__':
    print_seq()