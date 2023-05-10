def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_max = max(a)
    b_min = min(b)
    
    if a_max > b_min:
        print(0)
    else:
        print(b_min - a_max + 1)
