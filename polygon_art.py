import turtle
import random
import math

class ShapeArt:
    def __init__(self):
        pass
    
    def setup(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        turtle.hideturtle()
    
    def get_new_color(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        r = size / (2 * math.sin(math.pi / num_sides))
        
        turtle.penup()
        turtle.goto(location[0], location[1] - r)
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()

        angle = 360 / num_sides
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(angle)
        
        turtle.penup()


    def art1(self):
        for i in range(random.randint(15, 22)):
            num_sides = 3
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            reduction_ratio = 0.618

        for _ in range(1):
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location = list(turtle.pos())
            size *= reduction_ratio
            self.draw_polygon(num_sides, size, orientation, location, self.get_new_color(), border_size)
    
    def art2(self):
        for i in range(random.randint(15, 22)):
            num_sides = 4
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            reduction_ratio = 0.618

        for _ in range(1):
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location = list(turtle.pos())
            size *= reduction_ratio
            self.draw_polygon(num_sides, size, orientation, location, self.get_new_color(), border_size)
 
    def art3(self):
        for i in range(random.randint(15, 22)):
            num_sides = 5
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            reduction_ratio = 0.618

        for _ in range(1):
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location = list(turtle.pos())
            size *= reduction_ratio
            self.draw_polygon(num_sides, size, orientation, location, self.get_new_color(), border_size)
            
    def art4(self):
        for i in range(random.randint(15, 22)):
            num_sides = random.randint(3,5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            reduction_ratio = 0.618

        for _ in range(1):
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location = list(turtle.pos())
            size *= reduction_ratio
            self.draw_polygon(num_sides, size, orientation, location, self.get_new_color(), border_size)
            
    def art5(self):
        for i in range(random.randint(15, 22)):
            num_sides = 3
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            reduction_ratio = random.uniform(0.5, 0.8)
            inner_layers = 2

            for _ in range(inner_layers):
                size *= reduction_ratio
                self.draw_polygon(
                    num_sides,
                    size,
                    orientation,
                    location,
                    self.get_new_color(),
                    border_size
                )

    def art6(self):
        for i in range(random.randint(15, 22)):
            num_sides = 4
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            reduction_ratio = random.uniform(0.5, 0.8)
            inner_layers = 2

            for _ in range(inner_layers):
                size *= reduction_ratio
                self.draw_polygon(
                    num_sides,
                    size,
                    orientation,
                    location,
                    self.get_new_color(),
                    border_size
                )

    def art7(self):
        for i in range(random.randint(15, 22)):
            num_sides = 5
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            reduction_ratio = random.uniform(0.5, 0.8)
            inner_layers = 2

            for _ in range(inner_layers):
                size *= reduction_ratio
                self.draw_polygon(
                    num_sides,
                    size,
                    orientation,
                    location,
                    self.get_new_color(),
                    border_size
                )

    def art8(self):
        for i in range(random.randint(15, 22)):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            reduction_ratio = random.uniform(0.5, 0.8)
            inner_layers = 2

            for _ in range(inner_layers):
                size *= reduction_ratio
                self.draw_polygon(
                    num_sides,
                    size,
                    orientation,
                    location,
                    self.get_new_color(),
                    border_size
                )


    def art9(self):
        for i in range(random.randint(15, 22)):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            reduction_ratio = random.uniform(0.5, 0.8)
            inner_layers = random.randint(1, 2)

            for _ in range(inner_layers):
                size *= reduction_ratio
                self.draw_polygon(
                    num_sides,
                    size,
                    orientation,
                    location,
                    self.get_new_color(),
                    border_size
                )

    
    def show(self):
        turtle.update()
        turtle.done()


class ArtMenu:
    def __init__(self):
        self.art = ShapeArt()
        self.choices = {
            1: self.art.art1,
            2: self.art.art2,
            3: self.art.art3,
            4: self.art.art4,
            5: self.art.art5,
            6: self.art.art6,
            7: self.art.art7,
            8: self.art.art8,
            9: self.art.art9,
        }

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        if choice in self.choices:
            self.art.setup()
            self.choices[choice]()
            self.art.show()
        else:
            print("Invalid choice. Please run again.")

if __name__ == "__main__":
    menu = ArtMenu()
    menu.run()
