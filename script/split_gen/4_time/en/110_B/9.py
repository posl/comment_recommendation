def main():
    #Read input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #Check if war will break out
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print("No War")
    else:
        print("War")
    return
