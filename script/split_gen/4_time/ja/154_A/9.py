def main():
    #input
    s,t = input().split()
    a,b = map(int, input().split())
    u = input()
    #compute
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    #output
    print(a,b)
