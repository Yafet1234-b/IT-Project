Input_1 = int(input(" Enter the length for conversion :  "))
Input_2 = input(" Enter the unit to be converted :  ")
Input_3 = input(" Enter the unit to be converted to : ")
def Meter_Feet_Converter(x):
    x = ((x)*(3.28084))
    return(x)
def Feet_Meter_Converter(x):
    x = ((x)/(3.28084))
    return(x)
def Length_Conversion(x):
    if Input_2 == "Meter" and Input_3 == "Feet":
        return(str(Meter_Feet_Converter(x)) + " feet ")
    elif Input_2 == "Feet" and Input_3 == "Meter":
        return(str(Feet_Meter_Converter(x)) + " meter ")
    else:
        return(" None ")
print(Length_Conversion(Input_1))