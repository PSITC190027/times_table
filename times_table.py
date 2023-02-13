def times_table(num):
    for i in range(1, 13):
        print(num , " * " ,i , " = " , num*i)

number =int(input("Enter a number and get the multiples of it: "))
times_table(number)
