class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[1] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5


if __name__ == '__main__':
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    ahmet = point1.distance_from_point(point1)
    ahmet2 = point2.distance_from_point(point2)
    print(ahmet," \n",ahmet2)