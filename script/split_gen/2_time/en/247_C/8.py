def main():
    N = int(input())
    if N == 1:
        print("1")
        return
    S = [1]
    for i in range(2,N+1):
        S = S + [i] + S
    print(" ".join(map(str, S)))
