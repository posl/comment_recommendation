def main():
    #n, m = map(int, input().split())
    #a = [int(input()) for _ in range(n)]
    #b = [int(input()) for _ in range(m)]
    #print(n, m, a, b)
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    print(n, m, a, c)
    #print(n, m, a, b)
    #print(n, m, a, b, c, d)
    #print(n, m, a, b, c, d, sep='\n')
