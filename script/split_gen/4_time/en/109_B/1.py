def main():
    n = int(input())
    words = []
    for i in range(0,n):
        words.append(input())
    for i in range(0,n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    for i in range(0,n-1):
        if words[i] in words[i+1:]:
            print("No")
            return
    print("Yes")
