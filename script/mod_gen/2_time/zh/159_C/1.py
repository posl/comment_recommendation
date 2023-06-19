def max_volume(L):
    return (L/3)**3 if L%3 == 0 else (L//3+1)*(L//3)*(L//3)

if __name__ == '__main__':
    max_volume()