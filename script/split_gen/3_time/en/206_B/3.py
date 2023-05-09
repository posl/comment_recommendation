def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        i = 1
        while True:
            if n <= (i*(i+1)/2):
                print(i)
                break
            else:
                i += 1
