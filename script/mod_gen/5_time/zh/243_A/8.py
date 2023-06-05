def problem243_a():
    v,a,b,c = map(int,input().split())
    if v < a:
        print("F")
    elif v < b:
        print("M")
    elif v < c:
        print("T")
    else:
        print("T")

if __name__ == '__main__':
    problem243_a()