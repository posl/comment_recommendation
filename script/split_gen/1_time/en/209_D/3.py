def main():
    n, q = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n-1)]
    c = [list(map(int, input().split())) for _ in range(q)]
    b = [[] for _ in range(n+1)]
    for i in range(n-1):
        b[a[i][0]].append(a[i][1])
        b[a[i][1]].append(a[i][0])
    d = [0]*(n+1)
    e = [0]*(n+1)
    def dfs(x, y):
        for i in b[x]:
            if i != y:
                d[i] = d[x] + 1
                dfs(i, x)
    def dfs2(x, y):
        for i in b[x]:
            if i != y:
                e[i] = e[x] + 1
                dfs2(i, x)
    dfs(1, 0)
    dfs2(n, 0)
    for i in range(q):
        if (d[c[i][0]] + d[c[i][1]]) % 2 == 0:
            print("Town")
        else:
            print("Road")
main()
I'm not sure if this is the best way to solve this problem, but I'm happy that I could solve it. I'm still learning Python, so I'm not sure if I'm using the best method for some of the things I used. I'm looking forward to your feedback. Thank you for reading!
I'm not sure if this is the best way to solve this problem, but I'm happy that I could solve it.
I'm still learning Python, so I'm not sure if I'm using the best method for some of the things I used. I'm looking forward to your feedback. Thank you for reading!
This is a good solution, but you can make it even better. I have a few suggestions:
I'm not sure if this is the best way to solve this problem, but I'm happy that I could solve it. I'm still learning Python, so I'm not sure if I'm using the best method for some of the things I used. I'm looking forward to your feedback. Thank you for reading!
This is a good solution, but you can make it even better. I have a few suggestions:
Thank you for your feedback! I'll try to
