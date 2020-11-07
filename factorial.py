def factorial(n):
    return total
    userstring = input("Number Please:")
    usernum = int(userstring)
    for i in range(0,n):
        total = total * (n - i)
        print("Current i is " + str(i))
        print("Current value of total is " + str(total))
        print(usernum + "! is " + factorial(usernum))
