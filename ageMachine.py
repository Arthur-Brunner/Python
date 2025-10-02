def ageMachine (age: int): #his function take integer age as Argument and print if you old or will be old
    if age >= 50:
        print("du bist alt geworden")
    else:
        print("Aha, eines Tages du wirst alt auch")

def addTwoNumber(first_number:int , second_number:int)->int: #this function accept two integer as argument and add them return result of summation
    return first_number+second_number #snake_case für variablen nutzen -- klein geschrieben
result = addTwoNumber(5,6) #camel_case 
print("it is result: "+str(result))
ageMachine(51)