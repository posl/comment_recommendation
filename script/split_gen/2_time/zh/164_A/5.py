def main():
    a = input()
    b = a.split()
    c = int(b[0])
    d = int(b[1])
    if c > d:
        print("安全")
    else:
        print("不安全")
