def main():
    n = int(input())
    s = "1"
    for i in range(1,n):
        s = s + str(i+1) + s
    print(s)
