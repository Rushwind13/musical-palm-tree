import simplegui

class Circle:
    def __init__(self):
        self.radius = 100
        self.center_point = (200,200)

    def xshift(self, x_shift):
        x = (self.center_point[0] + x_shift) % 200
        y = self.center_point[1]
        self.center_point = (x,y)
        self.collide()
       
    def collide(self):
        if self.center_point[0] > 400-self.radius:
            x = 200
            y = 200
            self.center_point = (x,y)
 

class ShapeAttribute:
    def __init__(self):
        self.line_width = 20
        self.line_color = "Purple"
        self.fill_color = "Yellow"

class Cliq:
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttribute()
       
    def drawme(self, canvas, x_shift):
        self.circle_shape.xshift(x_shift)
        canvas.draw_circle(self.circle_shape.center_point, 
                           self.circle_shape.radius, 
                           self.shape_attributes.line_width, 
                           self.shape_attributes.line_color,
                           self.shape_attributes.fill_color)
    
cliq = Cliq()

def draw(canvas):
    cliq.drawme(canvas, x_shift=1)
    canvas.draw_line(
        (400, 0),
        (400, 400), 
        ShapeAttribute().line_width, 
        ShapeAttribute().line_color
    )

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
