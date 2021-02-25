def my_decorator(func):

    def wrapper():
        print('before')
        func()
        print('After')

    return wrapper
        

@my_decorator
def hi():
    print('hi')


hi()

