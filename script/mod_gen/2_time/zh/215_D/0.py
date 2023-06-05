def permutation(string):
    if len(string) <= 1:
        return [string]
    else:
        result = []
        for i in range(len(string)):
            for j in permutation(string[:i] + string[i+1:]):
                result.append(string[i] + j)
    return result

if __name__ == '__main__':
    permutation()