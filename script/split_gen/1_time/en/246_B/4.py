def main():
    A,B = map(int,input().split())
    #print(A,B)
    d = (A**2 + B**2)**0.5
    print(A/d,B/d)
