def main():
    #Read input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    #Calculate the total number of days of assignments
    total = 0
    for a in A:
        total += a
    
    #If the total number of days of assignments is greater than the number of days of vacation, print -1
    if total > N:
        print(-1)
    else:
        #Otherwise, print the number of days of vacation minus the total number of days of assignments
        print(N - total)

if __name__ == '__main__':
    main()