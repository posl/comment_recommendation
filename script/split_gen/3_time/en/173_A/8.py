def main():
    #Read input
    N = int(input())
    #Calculate change
    change = N % 1000
    #Output result
    if change == 0:
        print(0)
    else:
        print(1000 - change)
