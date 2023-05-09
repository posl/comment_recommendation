def solve(input_string):
    input_int = int(input_string)
    return 1000 - input_int % 1000 if input_int % 1000 != 0 else 0

if __name__ == '__main__':
    solve()