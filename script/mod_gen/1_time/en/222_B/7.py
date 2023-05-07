def main():
    # Read input
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Count number of students who failed the exam
    num_failed = 0
    for i in range(n):
        if a[i] < p:
            num_failed += 1
    
    # Print the number of students who failed the exam
    print(num_failed)

if __name__ == '__main__':
    main()