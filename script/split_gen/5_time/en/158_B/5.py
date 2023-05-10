def main():
    N,A,B = map(int,input().split())
    if A+B == 0:
        print(0)
    else:
        print((N//(A+B))*A+min(N%(A+B),A))
