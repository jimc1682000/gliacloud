#Please try to add 1~3 line of code to finish the integration
def anonymous(x):
    print("x",x)
    return x**2 + 1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        baseY = anonymous(0)
        nowY = anonymous(intercept)
        area += step*(nowY-baseY)
    return area
print(integrate(anonymous, 0, 10))
