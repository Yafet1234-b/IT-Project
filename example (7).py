X = int(input(" Enter the numerical value of the temperature ---> "))
Y = input(" Enter the unit of the temperature --->")
Z = input("Enter the unit you want to convert to -->")

def Celsius_Fahrenheit_Converter(x):
    x = ((((9)/(5)) * (x)) + ( 32 ))
    return(x)
def Fahrenheit_Celsius_Converter(x):
    x = (((x)-(32)) * ((5)/(9)))
    return(x)
def Temperature_Unit_Converter(x):
    if Y == "Fahrenheit" and Z == "Celsius":
        return Fahrenheit_Celsius_Converter(x)
    elif Y == "Celsius" and Z == "Fahrenheit":
        return (Celsius_Fahrenheit_Converter(x) )
    else:
        return ( " Error " )
print(Temperature_Unit_Converter(X))