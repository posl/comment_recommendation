def main():
    x,y = map(int,input().split())
    print(max(0,((y-x-1)//10)+1))
