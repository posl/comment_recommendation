def main():
    k,x = map(int,input().split())
    for i in range(k):
        print(x-k+i+1,end=" ")
        print(x+i+1,end=" ")
    print()
