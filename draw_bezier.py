from PIL import Image
from PIL import ImageDraw

def make_bezier(xys):
    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = pascal_row(n-1)
    def bezier(ts):
        # This uses the generalized formula for bezier curves
        # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier

def pascal_row(n, memo={}):
    # This returns the nth row of Pascal's Triangle
    if n in memo:
        return memo[n]
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        # print(numerator,denominator,x)
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
    if n&1 == 0:
        # n is even
        result.extend(reversed(result[:-1]))
    else:
        result.extend(reversed(result))
    memo[n] = result
    return result

if __name__ == '__main__':
    im = Image.new('RGBA', (1280, 720), (0, 0, 0, 0)) 
    draw = ImageDraw.Draw(im)
    ts = [t/100.0 for t in range(101)]

    xys = [(415.657897, 552.505266), (702.142109, 560.17895), (988.626321, 571.689477)]
    bezier = make_bezier(xys)
    points = bezier(ts)
    points.extend((1280.226323,588.315793))

    draw.polygon(points)
    im.save('out.png')