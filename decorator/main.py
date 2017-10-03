def decorator(func):
    def wrapper():
        wrapper.count += 1
        return func()
    return wrapper

@decorator
def foo():
    pass

if __name__ == "__main__":
    for test in range(1000):
        #
        foo.count = 0
        for i in range(test):
            foo()
        if test != foo.count:
            print("Error", str(test), "->", str(foo.count))
    print("END")
