def solve():
    v,a,b,c = map(int,input().split())
    if v % a == 0:
        print("T")
    elif v % b == 0:
        print("T")
    elif v % c == 0:
        print("T")
    else:
        print("F")

if __name__ == '__main__':
    solve()