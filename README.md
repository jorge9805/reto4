# reto4
# Restaurant (getters setters and diccounts)
was added getters and setter to each item on the menu like get volume in beverages or set calories in appetizer etc and most important was added a disccount according to if the menu has some main course or some appetizer if the menu has main course so the disscount is applied to all the beverages and if the menu has an appetizer the diccount is applied to the desserts

```python


class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Beverage(MenuItem):
    def __init__(self,name,price,volume,alcohol_content,lactose_free):
        super().__init__(name,price)
        self.volume=volume
        self.alcohol_content=alcohol_content
        self.lactose_free=lactose_free
    def set_volume(self,volume):
        self.volume=volume
    def set_alcohol_content(self,alcohol_content):
        self.alcohol_content=alcohol_content
    def set_lactose_free(self,lactose_free):
        self.lactose_free=lactose_free
    def get_volume(self):
        return self.volume 
    def get_alcohol_content(self):
        return self.alcohol_content
    def get_lactose_free(self):
        return self.lactose_free
        
class Appetizer(MenuItem):
    def __init__(self,name,price,calories):
        super().__init__(name,price)
        self.calories=calories
    def set_calories(self,calories):
        self.calories=calories
    def get_calories(self):
        return self.calories
    
class MainCourse(MenuItem):
    def __init__(self,name,price,calories,is_vegan):
        super().__init__(name,price)
        self.calories=calories
        self.is_vegan=is_vegan
    def set_calories(self,calories):
        self.calories=calories
    def set_is_vegan(self,is_vegan):
        self.is_vegan=is_vegan
    def get_calories(self):
        return self.calories
    def get_is_vegan(self):
        return self.is_vegan
    
class Dessert(MenuItem):
    def __init__(self,name,price,calories,is_gluten_free):
        super().__init__(name,price)
        self.calories=calories
        self.is_gluten_free=is_gluten_free
    def set_calories(self,calories):
        self.calories=calories
    def set_is_gluten_free(self,is_gluten_free):
        self.is_gluten_free=is_gluten_free
    def get_calories(self):
        return self.calories
    def get_is_gluten_free(self):
        return self.is_gluten_free

class Order:
    def __init__(self,table_number):
        self.table_number=table_number
        self.menu_items=[]
    def add_menu_item(self,menu_item):
        self.menu_items.append(menu_item)
    def is_main_course_included(self):
        for item in self.menu_items:
            if isinstance(item,MainCourse):
                return True
        return False
    
    def is_appetizer_included(self):
        for item in self.menu_items:
            if isinstance(item,Appetizer):
                return True
        return False
    def apply_discount(self):
        #is override according to the order composition
        if self.is_main_course_included():
            return (0.7,"Beverage")
        elif self.is_appetizer_included():
            return (0.8,"Dessert")
    def calculate_total_bill(self,discount):
        total=0
        for item in self.menu_items:
            if isinstance(item,Beverage) and (discount[1]=="Beverage"):
                total+=item.price*discount[0]
            elif isinstance(item,Dessert) and (discount[1]=="Dessert"):
                total+=item.price*discount[0]
            else:
                total+=item.price
        return total
    def get_items(self):
        items=[]
        for item in self.menu_items:
            items.append(item.name)
        return items
#items
roasted_chicken=MainCourse("Roasted Chicken",15,500,False)
chicken_wings=Appetizer("Chicken Wings",10,300)
chocolate_cake=Dessert("Chocolate Cake",5,400,True)
beer=Beverage("Beer",5,0.5,0.05,False)
salmon=MainCourse("Salmon",20,600,False)
fries=Appetizer("Fries",5,200)
ice_cream=Dessert("Ice Cream",4,300,True)
wine=Beverage("Wine",8,0.75,0.12,False)
lemonade=Beverage("Lemonade",3,0.3,0,False)
lentil_soup=Appetizer("Lentil Soup",6,250)
apple_pie=Dessert("Apple Pie",5,350,True)
water_with_ice=Beverage("Water with Ice",0,0.5,0,False)
pork_cheeks=MainCourse("Pork Cheeks",18,550,False)
orange_chiken=MainCourse("Orange Chicken",16,500,False)
vegan_hamburguer=MainCourse(" Vegan Hamburguer",14,450,True)
#orders

print("adding items to orders and calculating")
order1=Order(1)
order1.add_menu_item(roasted_chicken)
order1.add_menu_item(chicken_wings)
order1.add_menu_item(chocolate_cake)
order1.add_menu_item(beer)
print("the items on order 1 are:" ,order1.get_items())
order2=Order(2)
order2.add_menu_item(salmon)
order2.add_menu_item(fries)
order2.add_menu_item(ice_cream)
order2.add_menu_item(wine)
print("the items on order 2 are:" ,order2.get_items())
order3=Order(3)
order3.add_menu_item(lemonade)
order3.add_menu_item(lentil_soup)
order3.add_menu_item(apple_pie)
order3.add_menu_item(water_with_ice)
print("the items on order 3 are:" ,order3.get_items())

print("the total bill for order 1 is:",order1.calculate_total_bill(order1.apply_discount()))
print("the discount for order 1 is:",order1.apply_discount()[0],"the discount is for:",order1.apply_discount()[1] )
print("the total bill for order 2 is:",order2.calculate_total_bill(order2.apply_discount()))
print("the discount for order 2 is:",order2.apply_discount()[0],"the discount is for:",order2.apply_discount()[1] )
print("the total bill for order 3 is:",order3.calculate_total_bill(order3.apply_discount()))
print("the discount for order 3 is:",order3.apply_discount()[0],"the discount is for:",order3.apply_discount()[1] )




#setting things and getting things

print("setting and getting things")
print(wine.get_alcohol_content())
wine.set_alcohol_content(0.1)
print(wine.get_alcohol_content())
print(wine.get_volume())
wine.set_volume(0.8)
print(wine.get_volume())
print(chicken_wings.get_calories())
chicken_wings.set_calories(350)
print(chicken_wings.get_calories())
print(orange_chiken.get_calories())
orange_chiken.set_calories(550)
print(orange_chiken.get_calories())
print(orange_chiken.get_is_vegan())
orange_chiken.set_is_vegan(True)
print(orange_chiken.get_is_vegan())

```

# Shape 

the class and all the subclasses were created foremore the class shape has a lot of fuctions but each functions has to be override by every type of shape so we used the polimorfism a lot
```python
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
```
