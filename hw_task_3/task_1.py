class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
        self.perimeter = 2 * (width + height)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter
