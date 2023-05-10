def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    min = max(A)
    max = min(B)
    
    if max - min + 1 < 0:
        print(0)
    else:
        print(max - min + 1)
