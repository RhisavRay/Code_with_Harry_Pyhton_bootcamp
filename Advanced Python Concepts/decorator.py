def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed a function...")
    return wrapper
# A decorator is a function that accepts a function, creates anew function inside its body, and returns
# that new function

# f = decorator(say_hello)
# f()
# Now instead of writing this piece of code, we can make a change to the say_hello function itself

@decorator
def say_hello():
    print("Hello")
# A simple function to print Hello

say_hello()