def main():
    n,m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(0 if i == j else 1)
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(0)
                elif j == 0:
                    print(i+1)
                elif i == 0:
                    print(j+1)
                else:
                    print(min(i+1,j+1))
