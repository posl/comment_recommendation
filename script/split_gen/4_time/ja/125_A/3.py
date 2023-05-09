def main():
    a,b,t = map(int,input().split())
    i = 1
    j = 0
    while i <= t + 0.5:
        if i % a == 0:
            j += b
        i += 1
    print(j)
