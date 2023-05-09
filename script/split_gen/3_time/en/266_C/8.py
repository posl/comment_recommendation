def is_convex(A, B, C, D):
    """
    A, B, C, D are points
    """
    def is_convex_point(A, B, C):
        """
        A, B, C are points
        """
        return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) < 0
    return is_convex_point(A, B, C) and is_convex_point(B, C, D) and is_convex_point(C, D, A) and is_convex_point(D, A, B)
