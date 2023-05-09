def generations_away(n, p):
    generations = 0
    for i in range(n):
        generations += 1
        if p[i] == 1:
            break
    return generations

if __name__ == '__main__':
    generations_away()