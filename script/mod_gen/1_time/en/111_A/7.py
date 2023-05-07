def swap(n):
    return n.replace('1', 'x').replace('9', '1').replace('x', '9')
n = input()
print(swap(n))

if __name__ == '__main__':
    swap()