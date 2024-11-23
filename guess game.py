import random
x=random.randint(1,10)
print("I am thinking of a number between 1 and 10.")
i=0
while i<3:
    y = int(input("Take a guess: "))
    if y==x:
      print("yay")
      print("Good job! You guessed my number.")
    else:
      print("Wrong, try again.")
    i+=1

print("The number I was thinking of was",x)