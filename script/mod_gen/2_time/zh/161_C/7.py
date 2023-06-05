def get_input():
    n,m = input().split()
    n = int(n)
    m = int(m)
    A = input().split()
    A = [int(i) for i in A]
    return n,m,A

if __name__ == '__main__':
    get_input()