def main():
    H,A = map(int,input().split())
    count = 0
    while True:
        count += 1
        H -= A
        if H <= 0:
            break
    print(count)
