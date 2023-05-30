def horizon(H):
    return (H*(12800000+H))**(1/2)
H = int(input())
print(horizon(H))
