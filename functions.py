def greet():
    print("hello how aare you")

print("function started")
greet()
print("function ended")


# parameterized function
def greet(name):
    print(f"hello {name}")

print("function started")
greet(input("Enter your name: "))
print("function ended")
