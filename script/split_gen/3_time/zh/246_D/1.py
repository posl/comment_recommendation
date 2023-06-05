def main():
    n = int(input())
    a = 0
    b = 0
    x = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            x = i**3 + i**2*j + i*j**2 + j**3
            if x >= n:
                if a == 0 and b == 0:
                    a = i
                    b = j
                elif x < a**3 + a**2*b + a*b**2 + b**3:
                    a = i
                    b = j
    print(a**3 + a**2*b + a*b**2 + b**3)
