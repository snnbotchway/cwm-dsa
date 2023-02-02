class Student:
    def __init__(self, name) -> None:
        self.name = name


solomon = Student("Solomon")
nat = Student("Nathaniel")
pat = Student("Patrick")

solomon_ref = solomon
solomon = pat
solomon.name = "new name"
print(solomon_ref.name)
