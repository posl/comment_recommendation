def get_input():
    n,k = map(int, input().split())
    h = [int(input()) for i in range(n)]
    return n,k,h

if __name__ == '__main__':
    get_input()