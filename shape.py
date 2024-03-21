
from math import sqrt
class Point:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def compute_distance(self,point):
        return sqrt((point.x-self.x)**2+(point.y-self.y)**2)
      
class Line:
    def __init__(self,start:Point,end:Point):
        self.start=start
        self.end=end
        self.length=start.compute_distance(end)    

class Shape:
    def __init__(self,lines,points):
        self.lines=lines
        self.points=points
        self.is_regular=self.compute_regular()
    def compute_regular(self):
        for i in range(len(self.lines)-1):
            if self.lines[i].length!=self.lines[i+1].length:
                return False
        return True
    def vertices(self):
        return len(self.points)
    def edges(self):
        return len(self.lines)
    def inner_angles(self):
        raise NotImplementedError("Subclass must implement this method")
    def compute_area(self):
        raise NotImplementedError("Subclass must implement this method")
    def compute_perimeter(self):
        raise NotImplementedError("Subclass must implement this method")
class Triangle(Shape):
    def __init__(self,lines,points):
        super().__init__(lines,points)
        self.isTriangle=self.compute_triangle()
    def compute_triangle(self):
        if self.lines[0].length+self.lines[1].length>self.lines[2].length and self.lines[0].length+self.lines[2].length>self.lines[1].length and self.lines[1].length+self.lines[2].length>self.lines[0].length:
            return True
        return False
    def inner_angles(self):
        return 180
    def compute_area(self):
        return 0.5*abs((self.points[0].x*(self.points[1].y-self.points[2].y)+self.points[1].x*(self.points[2].y-self.points[0].y)+self.points[2].x*(self.points[0].y-self.points[1].y)))
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
class Equilateral(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 60
    def compute_area(self):
        return (sqrt(3)/4)*self.lines[0].length**2
    def compute_perimeter(self):
        return 3*self.lines[0].length
class Isosceles(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return 0.5*self.lines[0].length*sqrt(self.lines[1].length**2-(self.lines[0].length/2)**2)
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length*2
class Scalene(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        s=self.compute_perimeter()/2
        return sqrt(s*(s-self.lines[0].length)*(s-self.lines[1].length)*(s-self.lines[2].length))
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
class TriRectangle(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return 0.5*self.lines[0].length*self.lines[1].length
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
class Rectangle(Shape):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return self.lines[0].length*self.lines[1].length
    def compute_perimeter(self):
        return 2*(self.lines[0].length+self.lines[1].length)
class Square(Rectangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return self.lines[0].length**2
    def compute_perimeter(self):
        return 4*self.lines[0].length
    
print("equilateral triangle")
point1=Point(0,0)
point2=Point(3,0)
point3=Point(1.5,3)
line1=Line(point1,point2)
line2=Line(point2,point3)
line3=Line(point3,point1)
equilateral=Equilateral([line1,line2,line3],[point1,point2,point3])
print("vertices,edges,isTriangle,inner_angles,area,perimeter")
print(equilateral.vertices())
print(equilateral.edges())
print(equilateral.isTriangle)
print(equilateral.inner_angles())
print(equilateral.compute_area())
print(equilateral.compute_perimeter())

print("square")
point1=Point(0,0)
point2=Point(3,0)
point3=Point(3,3)
point4=Point(0,3)
line1=Line(point1,point2)
line2=Line(point2,point3)
line3=Line(point3,point4)
line4=Line(point4,point1)
square=Square([line1,line2,line3,line4],[point1,point2,point3,point4])
print("vertices,edges,inner_angles,area,perimeter")
print(square.vertices())
print(square.edges())
print(square.inner_angles())
print(square.compute_area())
print(square.compute_perimeter())



