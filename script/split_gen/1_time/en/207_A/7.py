def main():
    #input
    A,B,C = map(int,input().split())
    #output
    print(max(A+B,A+C,B+C))
