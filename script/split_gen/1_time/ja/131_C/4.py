def main():
    A,B,C,D = map(int,input().split())
    print(B-A+1-(B//C-(A-1)//C)-(B//D-(A-1)//D)+((B//C)*(B//D)-(A-1)//C*(A-1)//D))
main()
