Inputted_Name = input(" Enter the name of the contact you want to add : ")
Inputted_Contact_Number = input(" Enter the phone number of the contact you want to add : ")
Removed_Contact_Name = input(" Enter the name of the contact you want to remove : ")
Contacts = []
def Contact(x, y, z):
    Contacts.append(x)
    Contacts.append(y)
    if z in Contacts:
        Contacts.remove(Removed_Contact_Name)
    else:
        print(f"{z} does not exist in your contacts.")
    return(Contacts)
print(Contact(Inputted_Name, Inputted_Contact_Number, Removed_Contact_Name))