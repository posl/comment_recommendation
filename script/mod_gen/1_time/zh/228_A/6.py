def problems228_a():
    s,t,x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problems228_a()