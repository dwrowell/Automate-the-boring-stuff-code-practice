def collatz(number):
        while number>1:
            if number%2==0:
                number = number//2
                print(number)
            elif number%2!=0:
                number = (3*number+1)
                print(number)
        print('COLLLLLAAAATZZZ!!!!!!!')
     
print('Please enter a number')
try:
    number = int(input())
    collatz(number)

except ValueError:
    print('Error dummy. Please enter an integer.')
    
