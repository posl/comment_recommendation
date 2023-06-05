def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_max = max(a)
    a_min = min(a)
    b_max = max(b)
    b_min = min(b)
    
    if a_max - a_min > k or b_max - b_min > k:
        print("No")
    else:
        print("Yes")
