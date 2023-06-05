def main():
    n,s = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if i & (1<<j):
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == s:
            print("Yes")
            for j in range(n):
                if i & (1<<j):
                    print("H",end="")
                else:
                    print("T",end="")
            print()
            return
    print("No")
