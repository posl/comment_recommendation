def main():
    a,b = map(int,input().split())
    print(max(sum(list(map(int,list(str(a))))),sum(list(map(int,list(str(b)))))))
