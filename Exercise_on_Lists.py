Name_of_Contact = input(" Enter the name of the contact you want to add : ")
Phone_Number_of_Contact = input(" Enter the phone number of the contact you want to add : ")
Removed = input(" Enter the name of the contact you want to remove : ")
Contacts = []
def Contact(x, y, z):
    Contacts.append(x)
    Contacts.append(y)
    if z in Contacts:
        Contacts.remove(Removed)
    else:
        print(f"{z} does not exist in your contacts.")
    return(Contacts)
print(Contact(Name_of_Contact, Phone_Number_of_Contact, Removed))
