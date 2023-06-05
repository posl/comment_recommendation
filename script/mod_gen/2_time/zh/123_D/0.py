def main():
    N=int(input())
    A=int(input())
    B=int(input())
    C=int(input())
    D=int(input())
    E=int(input())
    ans=(N-1)//min(A,B,C,D,E)+5
    print(ans)
main()
