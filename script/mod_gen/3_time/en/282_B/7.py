def get_input():
    n,m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    return n,m,s

if __name__ == '__main__':
    get_input()