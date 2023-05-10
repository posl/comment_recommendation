def main():
    A,B,C = map(int,input().split())
    print(100*(A/(A+B+C)+B/(A+B+C)+C/(A+B+C)-1))
