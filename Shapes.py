


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def circumference(self):
        return 2*self.radius*3.14






class Square:
    def __init__(self,side):
        self.sides=side
    def area(self):
        return self.sides**2
    def calculate_peri5meter(self):
        return 4*self.sides






class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        X=self.width * self.length
        return X 
    def perimeter(self):
        p= 2*(self.length +self.width) 
        return p 

        


class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        Area=4*3.14* self.radius**2
        return Area
    def calculate_the_volume(self):
        volumes= (4/3)*3.14 *self.radius*self.radius*self.radius
        return volumes   


                
            
    