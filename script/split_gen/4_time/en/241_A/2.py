def main():
    a = list(map(int, input().split()))
    b = []
    b.append(0)
    b.append(a[0])
    b.append(a[a[0]])
    b.append(a[a[a[0]]])
    b.append(a[a[a[a[0]]]])
    b.append(a[a[a[a[a[0]]]]])
    b.append(a[a[a[a[a[a[0]]]]]])
    b.append(a[a[a[a[a[a[a[0]]]]]]])
    b.append(a[a[a[a[a[a[a[a[0]]]]]]]])
    b.append(a[a[a[a[a[a[a[a[a[0]]]]]]]]])
    print(b[3])
