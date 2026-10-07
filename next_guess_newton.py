x = float(input("What x to find the square root of? "))
g = float(input("What guess to start with? "))

print("Current estimate square:", g ** 2)

# Newton's method formula
next_guess = g - (g**2 - x) / (2 * g)

print("Next guess:", next_guess)