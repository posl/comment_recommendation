def f(x):
    return x*x + 2*x + 3
t = int(input())
print(f(f(f(t)+t)+f(f(t))))
The solution above is correct, but it is not efficient. In fact, it is a brute-force solution. You can find a more efficient solution below.
