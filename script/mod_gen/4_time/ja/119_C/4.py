def get_input():
    n,a,b,c = map(int,input().split())
    l = []
    for i in range(n):
        l.append(int(input()))
    return n,a,b,c,l

if __name__ == '__main__':
    get_input()