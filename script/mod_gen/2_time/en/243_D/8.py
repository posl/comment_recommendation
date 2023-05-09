def findParent(n):
    if n%2 == 0: return n//2
    else: return (n-1)//2

if __name__ == '__main__':
    findParent()