def solve(a,b):
    for i in range(1, 100):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    solve()