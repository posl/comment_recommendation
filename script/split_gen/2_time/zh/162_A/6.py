def main():
    k = int(input())
    count = 0
    for i in range(1,10**6):
        if is_lucky(i):
            count += 1
        if count == k:
            print(i)
            break
