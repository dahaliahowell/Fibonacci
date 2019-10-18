#Name:  Dahalia Howell

#My First Ever Github Project :)

#This function checks an inputted list to determine whether or not it is a fibonacci sequence.
#It returns True if it is and False if it is not.
def fib_check(lst):
    target = lst[0]
    counter = 0
    while target > fib(counter):
        counter+=1
    if counter != target:
        return False
    return lst == genFib(counter, counter + len(lst))

#This function returns the fibonacci number of its input.
def fib(x):
    if x == 0:
        return 0
    elif x < 3:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#This function accepts the starting number and one plus the ending number of a range as input.
#It the finds the fibonacci number of each number within the range and adds them to a list after each iteration.
#The function returns a list containing the fibonacci sequence of the range.
def genFib(start, end):
    lst = []
    for i in range(start, end):
        lst += [fib(i)]
    return lst

# print(genFib(0,6))
print(fib_check([0,1,1,2,3,5]))
    

