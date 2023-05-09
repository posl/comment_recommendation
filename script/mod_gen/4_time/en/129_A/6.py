def problems129_a():
    P,Q,R = map(int,input().split())
    print(min(P+Q,Q+R,R+P))

if __name__ == '__main__':
    problems129_a()