def main():
    #write your code here
    N, D = map(int,input().split())
    if N % (2*D+1) == 0:
        print(N//(2*D+1))
    else:
        print(N//(2*D+1)+1)
