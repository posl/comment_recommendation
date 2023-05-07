def main():
    #write your code here
    a,b = map(int,input().split())
    print((b-a)*(b-a+1)//2-b)
