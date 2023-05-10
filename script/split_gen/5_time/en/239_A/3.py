def horizon(h):
    return (h*(12800000+h))**(1/2)
print(horizon(int(input())))
