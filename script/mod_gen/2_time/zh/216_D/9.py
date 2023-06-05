def getMinSteps(n):
    steps = []
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            steps.append('B')
        else:
            n = n - 1
            steps.append('A')
    return steps[::-1]

if __name__ == '__main__':
    getMinSteps()