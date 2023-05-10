def main():
    a,b,c,d,e = map(int, input().split())
    l = [a,b,c,d,e]
    print(len(set(l)))
