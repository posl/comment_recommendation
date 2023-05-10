def main():
    a,b,x = map(int,input().split())
    max = 0
    for i in range(1,10):
        if x >= a * i + b * len(str(i)):
            max = i
    print(max)
