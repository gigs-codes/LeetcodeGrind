# x = "Python"
# y = "is "
# z = "awesome"
# print(x + y + z)


# ----------------------------------- GLOBAL VARIABLES -----------------------------------
# name='GARIMA'

# def myname():
#     name='SHRISTY'
#     print(name)

# print(name)
# myname()

# def myname():
#     global name
#     global memory
#     memory = 'hey'
#     name = 'GARIMA'

# myname()
# print(memory)
# print(name)


# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# y="She "

# def my():
#   global x 
#   x = "is mine"
  
# my()
# print( y + x)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------LISTS--------------------------------------------------
# x = ['apple','banana','jackfruit']
# x.append("strawberry") #add one item
# x.extend(["grapes","lemon"]) #add multiple items
# x.insert(1,"garima") #insert at index at 1 
# x[0] = "ankit" #modify he element
# x.remove("jackfruit") #remove value
# x.pop() #remove the last Selement
# print(x)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------TUPLE--------------------------------------------------
# t=(1,2,3,4)
#no append allowed
# t=t+(5,)
# print(t)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------RANGE--------------------------------------------------
# r=range(1,5)
# l=list(r)
# l.append(5)
# print(l)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------DICTIONARY--------------------------------------------------
# d = {"a":1}
# print(d)
# d["b"] = 2 #add a new key
# print(d)
# d["a"] = 4 #modify value
# print(d)
# d.update({"c":3}) #add multiple
# print(d)
# d.pop("a") #remove key
# print(d)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------SET--------------------------------------------------
# s={1,2}
# s.add(3) #add new element
# print(s)

# s.update([4,5]) #add multiple elements
# print(s)

# s.remove(2) #error if not found
# print(s)

# s.discard(10) #remove(error if not found)
# print(s)


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------FROZEN SET--------------------------------------------------
# fs=frozenset([1,2,3,4])
# cannot add or remove any value


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------BOOL--------------------------------------------------
# b=True #cannot modify


# --------------------------------------------------SETTING THE DATA TYPES------------------------------------------------------
# --------------------------------------------------BYTES --------------------------------------------------
# b=b"hello"
# b=b+b"world"
# print(b)
# Cannot append directly.

# BYtEARRAY
# ba = bytearray(b"hello")
# ba.append(33)
# ba.extend(b"world")
# ba[0] = 72
# print(ba)

# # memoryview - view of bytes, array, without copying
# ba=bytearray(b"hello")
# mv = memoryview(ba)
# mv[0] = 72
# print(mv)

# txt = "hey world garima this side"
# # print("hey" not in txt)

# if "heyya" not in txt:
#     print("NO Hey is not in txt")

# prive=450.9033
# txt = f"the price of this pot is {prive:.2f}"
# print(txt)

# txt="we are so called \"vikings\" from north"
# print(txt)

# class MyClass:
#     x=5

# p1 = MyClass()
# print(p1.x)

# del p1

# class Person:
#     name = ""
#     age = 0 
#     def __init__(self, name, age): # type: ignore
#         self.name=name
#         self.age=age

#     def greet(self):
#         print("Hello, my name is ",self.name)

# p1 = Person(name="John", age=36)
# p1.greet()


# class Family:
#     def __init__(self, name:str, age:int) -> None:
#         self.name=name
#         self.age=age
    
#     def greet(self)->None:
#         print("my name is ", self.name)

# p1 = Family("Garima", 22)
# p1.greet()
        
# class Person:
#     lastname = "Jackson"   # Class variable

#     def __init__(self, name):
#         self.name = name   # Instance variable

# p1 = Person("Emil")
# p2 = Person("Tobias")

# Person.lastname = "Hansen"

# print(p1.lastname)

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def bark(self):
#         print(self.name, " says woof!!")

# d1 = Dog("Buddy",3)
# d1.bark()

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def show(self):
#         print(self.brand)

#     # def display_info(self):
#     #     print(f"{self.year} {self.brand} {self.model}")

# # car1 = Car("Toyata","12ert","2003")
# # car1.display_info()

# c1 = Car(brand="Ford")
# c1.show()

# class Car:
#     def __init__(self,brand):
#         self.brand=brand
        
#     def show(self):
#         print(self.brand)

# c1 = Car("Ford")
# c1.show()

# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade

# s1 = Student("Anna","A")
# print(s1.grade)

# s1.grade = "B"
# print(s1.grade)



# class Playlist:
#     def __init__(self,name) -> None:
#         self.name=name
#         self.songs=[]

#     def add_song(self,song):
#             self.songs.append(song)
#             print(f"added song is : {song}")
        
#     def remove_song(self,song):
#             if song in self.songs:
#                 self.song.remove(song)
#                 print(f"Removed: {song}")

#     def show_songs(self):
#             print(f"playlist is '{self.name}'")
#             for song in self.songs:
#                 print(f"-{song}")
# del Playlist.remove_song #it will cause an error 

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian rap")
# my_playlist.add_song("heyyo rap")
# my_playlist.add_song("kaha rap")
# my_playlist.add_song("behyaa rap")
# my_playlist.remove_song("stairway to heaven")
# my_playlist.show_songs()


# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def area(self):
#         print(f"the area is '{self.width*self.height}'") 
    
# r1 = Rectangle(2,3)
# r1.area()

