def main():
    a,b = map(int,input().split())
    print(b-a-(b-a)*(b-a+1)//2)