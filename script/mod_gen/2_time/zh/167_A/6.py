def solve(x):
    for a in range(-118,119):
        for b in range(-119,118):
            if a**5-b**5==x:
                return a,b
x=int(input())
a,b=solve(x)
print(a,b)

if __name__ == '__main__':
    solve()