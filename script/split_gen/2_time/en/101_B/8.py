def sum_digits(n):
    return sum(int(i) for i in str(n))
n = int(input())
print("Yes" if n % sum_digits(n) == 0 else "No")
This is a very short solution, but it is not very efficient. It is O(n) in time and O(1) in space.
