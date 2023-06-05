def main():
    k = int(input())
    count = 0
    i = 1
    while True:
        if i % sum([int(j) for j in str(i)]) == 0:
            count += 1
            if count == k:
                print(i)
                break
        i += 1
