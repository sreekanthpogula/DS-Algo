class Myclass:
    def __init__(self, value, value1):
        self.value = value
        self.value1 = value1

    def __str__(self):
        return f"Myclass instance with the value: {self.value}"

    def __repr__(self):
        return f"Myclass {self.value}"

    def __len__(self):
        return len(str(self.value))

    def __add__(self, other):
        if isinstance(other, Myclass):
            return Myclass(self.value + other.value)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Myclass):
            return self.value == other.value
        else:
            return False

    def __getitem__(self, index):
        return str(self.value)[index]

    def __iter__(self):
        self.index = 0
        return self

    def __contains__(self, item):
        return str(item) in str(self.value)

    def __enter__(self):
        print("Entering into the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting the content")

    def __call__(self, *args, **kwargs):
        print(f"calling with args:{args}, kwargs: {kwargs}")


obj1 = Myclass(23, 23)
print(str(obj1))
print(repr(obj1))
print(len(obj1))

obj2 = Myclass(48)
obj3 = obj1 + obj2
print(obj3)
print(obj3 == obj2)
print(obj1[1])


print('\n' in obj1)

with obj1:
    print("Inside the context")

obj1(1, 2, key='value')
