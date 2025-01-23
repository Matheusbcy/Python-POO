class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        for contact in self.contacts:
            print(
                f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}"
            )

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(
                    f"Found: Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}"
                )
                return contact
        print("Contact not found")
        return None

    def remove_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact {name} removed")
        else:
            print(f"Contact {name} not found")