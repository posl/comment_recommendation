def main():
    N = int(input())
    for i in range(N, 10**18+1):
        for a in range(1, 10**9+1):
            for b in range(1, 10**9+1):
                if i == a**3 + a**2*b + a*b**2 + b**3:
                    print(i)
                    return
