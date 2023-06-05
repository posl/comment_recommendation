def main():
    k,x = map(int,input().split())
    left = x-k+1
    right = x+k
    for i in range(left,right):
        print(i,end=" ")
