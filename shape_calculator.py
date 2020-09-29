class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.width and self.height) <= 50:
            picture = ''
            for i in range(self.height):
                for j in range(self.width):
                    picture += '*'
                picture += '\n'
            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        horizontalin = self.width // shape.width
        verticalin = self.height // shape.height
        result = horizontalin * verticalin
        return result

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
