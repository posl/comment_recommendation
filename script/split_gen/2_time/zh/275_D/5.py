def function_f(n):
    if n == 0:
        return 1
    else:
        return function_f(int(n/2)) + function_f(int(n/3))
n = int(input())
print(function_f(n))
