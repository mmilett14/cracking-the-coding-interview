def factorial(i):
    if i == 0:
        return 1
    elif i >= 1:
        return i * factorial(i - 1)
    else:
        print('enter number greater or equal to 1')
