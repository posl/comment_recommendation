def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    #print(p)
    p[-1] = p[-1] / 2
    #print(p)
    print(int(sum(p)))
