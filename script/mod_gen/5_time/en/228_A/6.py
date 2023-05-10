def problem():
    s,t,x = map(int,input().split())
    if s < t:
        if s < x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if x > s or x < t:
            print("Yes")
        else:
            print("No")
problem()

if __name__ == '__main__':
    problem()