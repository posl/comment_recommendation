def f(x):
    return x**2 + 2*x + 3
t = int(input())
print(f(f(f(t)+t)+f(f(t))))
This is a very simple problem, but I had to make sure that I was using the right precedence for the operators. The solution is to use parentheses to make sure that the operations are done in the correct order.

if __name__ == '__main__':
    f()