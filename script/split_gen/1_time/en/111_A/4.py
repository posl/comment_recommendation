def solution():
    n = input()
    result = n.replace('1', 'x')
    result = result.replace('9', '1')
    result = result.replace('x', '9')
    print(result)
solution()
