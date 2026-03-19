class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

    def contains_point(self, point):
        dx = self.center.x - point.x
        dy = self.center.y - point.y
        return dx*dx + dy*dy <= self.r * self.r


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_corners(self):
        return [
            self.top_left,
            Point(self.bottom_right.x, self.top_left.y),
            self.bottom_right,
            Point(self.top_left.x, self.bottom_right.y)
        ]

    def is_inside_circle(self, circle):
        for corner in self.get_corners():
            if not circle.contains_point(corner):
                return False
        return True

    def overlaps_circle(self, circle):
        cx = circle.center.x
        cy = circle.center.y

        # tìm điểm gần nhất trên hình chữ nhật
        if cx < self.top_left.x:
            closest_x = self.top_left.x
        elif cx > self.bottom_right.x:
            closest_x = self.bottom_right.x
        else:
            closest_x = cx

        if cy > self.top_left.y:
            closest_y = self.top_left.y
        elif cy < self.bottom_right.y:
            closest_y = self.bottom_right.y
        else:
            closest_y = cy

        dx = cx - closest_x
        dy = cy - closest_y

        return dx*dx + dy*dy <= circle.r * circle.r
