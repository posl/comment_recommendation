def problems250_b():
    n,a,b = map(int,input().split())
    for i in range(n * a):
        for j in range(n * b):
            if (i // a + j // b) % 2 == 0:
                print(".",end="")
            else:
                print("#",end="")
        print()

if __name__ == '__main__':
    problems250_b()