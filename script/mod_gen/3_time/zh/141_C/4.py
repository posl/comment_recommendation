def get_input():
    n,k,q = map(int,input().split())
    alist = []
    for i in range(q):
        alist.append(int(input()))
    return n,k,q,alist

if __name__ == '__main__':
    get_input()