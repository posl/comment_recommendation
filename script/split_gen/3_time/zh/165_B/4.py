def main():
    x=int(input())
    a=100
    count=0
    while a<x:
        a=int(a*1.01)
        count+=1
    print(count)
