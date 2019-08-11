'''Write a sort_contacts function that takes a dictionary of contacts as a 
parameter and returns a sorted list of those contacts, where each contact is a tuple.'''

contacts = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
            "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
            "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}


def sort_contacts(contacts):
    contacts_list = []
    for name, (phone, email) in sorted(contacts.items()):
        tuple_contacts = (name, phone, email)
        contacts_list.append(tuple_contacts)
    return contacts_list


print(sort_contacts(contacts))
