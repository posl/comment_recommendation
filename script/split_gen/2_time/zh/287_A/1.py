def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    if a.count("For") > a.count("Against"):
        print("Yes")
    else:
        print("No")
        
main()
