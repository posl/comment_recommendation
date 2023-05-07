def main():
    A,B = map(int,input().split())
    g = 1
    t = 0
    while True:
        if A/((g)**(1/2)) <= t:
            break
        g += 1
        t += B
    print(t)
