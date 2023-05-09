def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        temp_a,temp_b = map(int,input().split())
        a.append(temp_a)
        b.append(temp_b)
    #print(n,x)
    #print(a)
    #print(b)
    current_position = 0
    for i in range(n):
        current_position = current_position + a[i]
        if current_position > x:
            print("No")
            return
        current_position = current_position + (b[i] - a[i])
        if current_position > x:
            print("No")
            return
    if current_position == x:
        print("Yes")
    else:
        print("No")
    return
