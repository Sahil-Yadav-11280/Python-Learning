import matplotlib.pyplot as plt

class Circle(object):
    
    # construtor:
    def __init__ (self , radius=0 , color="red"):
        self.radius = radius;
        self.color = color;

    # Method to add radius:
    def add_radius(self , radius):
        self.radius+=radius

    # drawing the circle:
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0) , radius = self.radius , fc = self.color))
        plt.axis("scaled")
        plt.show()



# Here these 2 objects running their drawing methods is an example of synchronous 


# Creating the object:
RedCircle = Circle(10,"red")
# print(dir(RedCircle))   
RedCircle.drawCircle()

# Creating another object:
BlueCircle = Circle(7 , "Blue")
BlueCircle.drawCircle()