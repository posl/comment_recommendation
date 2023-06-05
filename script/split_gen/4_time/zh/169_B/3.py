def solve(input):
    result = 1
    for i in input:
        if i == 0:
            return 0
        else:
            result *= i
            if result > 10 ** 18:
                return -1
    return result
