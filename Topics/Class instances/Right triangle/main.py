import math

class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = round((1 / 2) * self.a * self.b, 1)

def triangle_is_right(hyp, leg_1, leg_2):
    return math.pow(hyp, 2) == math.pow(leg_1, 2) + math.pow(leg_2, 2)

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
if triangle_is_right(input_c, input_a, input_b):
    right_triangle = RightTriangle(input_c, input_a, input_b)
    print(right_triangle.area)
else:
    print("Not right")
