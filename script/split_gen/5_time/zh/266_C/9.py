def is_convex_quad(ax,ay,bx,by,cx,cy,dx,dy):
    # 计算向量的叉积
    def cross_product(x1,y1,x2,y2):
        return x1*y2-x2*y1
    # 计算向量ab和向量ac的叉积
    def cross_product_ab_ac(ax,ay,bx,by,cx,cy):
        x1 = bx-ax
        y1 = by-ay
        x2 = cx-ax
        y2 = cy-ay
        return cross_product(x1,y1,x2,y2)
    # 计算向量ab和向量ad的叉积
    def cross_product_ab_ad(ax,ay,bx,by,dx,dy):
        x1 = bx-ax
        y1 = by-ay
        x2 = dx-ax
        y2 = dy-ay
        return cross_product(x1,y1,x2,y2)
    # 计算向量cd和向量ca的叉积
    def cross_product_cd_ca(cx,cy,dx,dy,ax,ay):
        x1 = dx-cx
        y1 = dy-cy
        x2 = ax-cx
        y2 = ay-cy
        return cross_product(x1,y1,x2,y2)
    # 计算向量cd和向量cb的叉积
    def cross_product_cd_cb(cx,cy,dx,dy,bx,by):
        x1 = dx-cx
        y1 = dy-cy
        x2 = bx-cx
        y2 = by-cy
        return cross_product(x1,y1,x2,y2)
    # 计算向量ab和向量ad的叉积
    def cross_product_ab_ad(ax,ay,bx,by,dx,dy):
        x1 = bx-ax
        y1 = by-ay
        x2 = dx-ax
        y2 = dy-ay
        return cross_product(x1,y1,x2,y2)
    # 计算向量ab和向量ad的叉积
    def cross_product_ab_ad(ax,ay,bx,by,dx,dy):
        x
