def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    x = [a,b,c,d,e]
    min = x[0]
    for i in range(1,5):
        if(x[i] < min):
            min = x[i]
    if(n % min == 0):
        print(int(n/min) + 4)
    else:
        print(int(n/min) + 5)
