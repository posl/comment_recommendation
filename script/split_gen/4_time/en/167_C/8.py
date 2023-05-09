def main():
    n,m,x = map(int,input().split())
    book = []
    for i in range(n):
        book.append(list(map(int,input().split())))
    ans = min([sum([book[i][0] for i in range(n) if j & (1 << i)]) for j in range(2**n) if sum([book[i][j+1] for i in range(n)]) >= x])
    print(ans if ans < 10**5 else -1)
