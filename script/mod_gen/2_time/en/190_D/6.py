def solve(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    if n == 1:
        return 2
    else:
        sum = 0
        i = 1
        while sum < n:
            sum += i
            i += 1
        if sum == n:
            return i - 1
        else:
            return i - 2

if __name__ == '__main__':
    solve()