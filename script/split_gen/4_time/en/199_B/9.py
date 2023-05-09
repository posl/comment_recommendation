def main():
    #get input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #find min and max of the ranges
    min_a = max(a)
    max_b = min(b)
    #check if there is any x in the range
    if min_a > max_b:
        print(0)
    else:
        print(max_b - min_a + 1)
