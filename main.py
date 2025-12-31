class Person:
    def __init__(self, name, interests, location):
        self.name =  name
        self.interests = interests
        self.location = location

    def introduce(self):
        items = ", ".join(self.interests)
        return f"Hello, my name is {self.name}. I enjoy {items}. I am currently based in {self.location}."
    
me = Person(
    name="Abin Mohammad Syafrial",
    interests=["volleyball", "football", "coffee"],
    location="Jember, Indonesia"
)

print(me.introduce())