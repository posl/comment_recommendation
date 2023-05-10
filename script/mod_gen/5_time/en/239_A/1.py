def horizon(H):
    return (H*(12800000+H))**(1/2)
print(horizon(int(input())))

if __name__ == '__main__':
    horizon()