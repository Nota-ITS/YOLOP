import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

im = Image.new('RGBA', (1280, 720), (0, 0, 0, 0)) 
draw = ImageDraw.Draw(im)

points = ((723.399765,405.873939), (1001.97007,649.997378), (1280.52479, 691.932694), (1280.52479, 455.297703), (1121.785255, 444.813875),(1030.426177, 446.311564), (919.59713, 407.371629),(723.399765,405.873939))
draw.polygon(points, fill=(1,1,1))

# points = [(415.657897, 552.505266), (702.142109, 560.17895), (988.626321, 571.689477)]
# draw.polygon(points)

im.save('outdrivable.png')