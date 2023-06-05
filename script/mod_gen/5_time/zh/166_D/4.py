def problem_166(x):
    for b in range(-1000,1000):
        for a in range(-1000,1000):
            if a**5 - b**5 == x:
                return (a,b)

if __name__ == '__main__':
    problem_166()