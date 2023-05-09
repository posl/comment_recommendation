def main():
    K = int(input())
    S = str(input())
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)
