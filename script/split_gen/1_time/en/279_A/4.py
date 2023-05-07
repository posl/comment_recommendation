def main():
    S = input()
    count = 0
    bottom = 0
    for i in S:
        if i == 'v':
            count += 1
            if count == 1:
                bottom += 1
        else:
            count -= 1
    print(bottom)
