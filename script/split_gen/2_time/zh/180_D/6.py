def main():
    n = int(input())
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            print(i)
            if i != n//i:
                print(n//i)
    return
