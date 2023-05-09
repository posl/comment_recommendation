def main():
    #S, T = map(int, input().split())
    S = 30
    T = 100
    count = 0
    for a in range(0, S+1):
        for b in range(0, S+1):
            for c in range(0, S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1
    print(count)
