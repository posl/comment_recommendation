def problem_index(s):
    if len(s) == 1:
        return ord(s) - 64
    else:
        return problem_index(s[0]) * 26 + problem_index(s[1:])
s = input()
print(problem_index(s))

if __name__ == '__main__':
    problem_index()