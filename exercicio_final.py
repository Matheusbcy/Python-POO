from contato import Contact
from contato_agenda import ContactBook

contato_agenda = ContactBook()

while True:
    print("\n --- Options ---")
    print("1 - Add contact")
    print("2 - Remove contact")
    print("3 - List contacts")
    print("4 - Search contact")
    print("5 - Exit")
    
    choice = input("Choose an option:\n ")
    
    if choice == "5":
        break
    elif choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print("Contato foi adicionado com sucesso")
    elif choice == "2":
        name = input("Name: ")
        contact = contato_agenda.search_contact(name)
        if contact:
            contato_agenda.remove_contact(name)
            print("Contato removido com sucesso")
    elif choice == "3":
        contato_agenda.list_contacts()
    elif choice == "4":
        name = input("Name: ")
        contact = contato_agenda.search_contact(name)
        if contact:
            print("Contato encontrado")
    else:
        print("Opcao invalida. utilize a opcao de 1 a 5")