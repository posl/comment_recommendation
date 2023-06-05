def get_max_volume(L):
    return (L/3)**3 if L%3 == 0 else (L/3)**3 + 1
