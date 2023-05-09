def main():
    a,b,c,d,e = map(int, input().split())
    list = [a,b,c,d,e]
    print(len(set(list)))
