def main(file_name):

    menu_output()
    selection = int(input("Выберите опцию: "))
    if selection == 1:
        make_contact(file_name)
    elif selection == 2:
        modify_contact(file_name)
    elif selection == 3:
        delete_contact(file_name)
    elif selection == 4:
        show_contact(file_name)
    elif selection == 5:
        copy_contact(file_name)
    elif selection == 0:
        print("Вы вышли из телефонной книги")
        return
    else:
        print("Данной опции не существует!")
        main(file_name)
def menu_output():
    print("Нажмите 1 чтобы создать контакт")
    print("Нажмите 2 чтобы изменить контакт")
    print("Нажмите 3 чтобы удалить контакт")
    print("Нажмите 4 чтобы найти и показать контакт")
    print("Нажмите 5 чтобы скопировать контакт")
    print("Нажмите 0 для выхода из телефонного справочника")

def make_contact(file_name):
    firstname = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    contact = f'{firstname} {lastname} {phone} {comment}'
    with open(file_name, 'a', encoding='UTF-8') as data:
        data.write(contact + '\n')
    main(file_name)

def modify_contact(file_name):
    contact_to_modify = input("Введите данные контакта, который вы хотите изменить: ")
    contacts = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            contacts.append(line.strip())
    matching_contacts = [contact for contact in contacts if contact_to_modify in contact]

    if len(matching_contacts) == 0:
        print("Данного контакта не существует")
    elif len(matching_contacts) == 1:
        contact_index = contacts.index(matching_contacts[0])
        contact_fields = matching_contacts[0].split()

        print("Выберите поле для изменения:")
        print("1. Имя")
        print("2. Фамилия")
        print("3. Номер")
        print("4. Комментарий")

        field_selection = int(input("Введите номер поля: "))

        if field_selection == 1:
            new_value = input("Введите новое имя: ")
            contact_fields[0] = new_value
        elif field_selection == 2:
            new_value = input("Введите новую фамилию: ")
            contact_fields[1] = new_value
        elif field_selection == 3:
            new_value = input("Введите новый номер: ")
            contact_fields[2] = new_value
        elif field_selection == 4:
            new_value = input("Введите новый комментарий: ")
            contact_fields[3] = new_value
        else:
            print("Неверный номер поля")


        updated_contact = ' '.join(contact_fields)
        contacts[contact_index] = updated_contact

        with open(file_name, 'w', encoding='UTF-8') as file:
            for contact in contacts:
                file.write(contact + '\n')

        print("Контакт успешно изменен")

    else:
        print("Уточните, какой контакт вы хотите изменить:")
        for index, contact in enumerate(matching_contacts):
            print(f"{index + 1}. {contact}")

        contact_selection = int(input("Введите номер контакта: "))

        if contact_selection < 1 or contact_selection > len(matching_contacts):
            print("Неверный номер контакта")
            return

        contact_to_modify = matching_contacts[contact_selection - 1]
        contact_index = contacts.index(contact_to_modify)
        contact_fields = contact_to_modify.split()

        print("Выберите поле для изменения:")
        print("1. Имя")
        print("2. Фамилия")
        print("3. Номер")
        print("4. Комментарий")

        field_selection = int(input("Введите номер поля: "))

        if field_selection == 1:
            new_value = input("Введите новое имя: ")
            contact_fields[0] = new_value
        elif field_selection == 2:
            new_value = input("Введите новую фамилию: ")
            contact_fields[1] = new_value
        elif field_selection == 3:
            new_value = input("Введите новый номер: ")
            contact_fields[2] = new_value
        elif field_selection == 4:
            new_value = input("Введите новый комментарий: ")
            contact_fields[3] = new_value
        else:
            print("Неверный номер поля")
            return

        updated_contact = ' '.join(contact_fields)
        contacts[contact_index] = updated_contact

        with open(file_name, 'w', encoding='UTF-8') as file:
            for contact in contacts:
                file.write(contact + '\n')

        print("Контакт успешно изменен")
    main(file_name)
    
def delete_contact(file_name):
    contact_ = input("Введите данные контакта, который вы хотите удалить: ")
    contacts = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            contacts.append(line.strip())

    matching_contacts = [contact for contact in contacts if contact_ in contact]

    if len(matching_contacts) > 0:
        if len(matching_contacts) > 1:
            print(
                f"Найдено несколько контактов с данными '{contact_}'. Введите номер контакта, который вы хотите удалить:")
            for i, contact in enumerate(matching_contacts):
                name, surname, phone, comment = contact.split(' ')
                print(f"{i + 1}. {name} {surname} {phone} {comment}")
            selection = input("Выберите номер контакта: ")
            if not selection.isdigit() or int(selection) < 1 or int(selection) > len(matching_contacts):
                print("Неверный номер контакта")
                main(file_name)
                return
            contact_to_delete = matching_contacts[int(selection) - 1]
        else:
            contact_to_delete = matching_contacts[0]

        with open(file_name, 'r', encoding='UTF-8') as data:
            lines = data.readlines()

        with open(file_name, 'w', encoding='UTF-8') as data:
            for line in lines:
                if line.strip().split(' ') != contact_to_delete.split(' '):
                    data.write(line)
        print(f"Контакт {contact_to_delete.split(' ')[0]} {contact_to_delete.split(' ')[1]} успешно удален.")
    else:
        print(f"Контакт с данными '{contact_}' не найден.")

    main(file_name)

def show_contact(file_name):

    name = input("Введите данные контакта который необходимо найти: ")
    contacts = []
    with open(file_name, 'r', encoding='UTF-8') as data:
        for line in data:
            if name.lower() in line.lower():
                contacts.append(line)

    if len(contacts) > 0:
        print("Список контактов с данными", name, ":")
        for contact in contacts:
            print(contact)
    else:
        print("Контакт с данными", name, "не найден")
    main(file_name)


def copy_contact(file_name):
    contact_name = input("Введите данные контакта, который вы хотите скопировать: ")
    copied_contacts = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            if contact_name in line:
                copied_contacts.append(line)

    if len(copied_contacts) > 1:
        print(
            f"Найдено несколько контактов с данными {contact_name}. Уточните, какой именно контакт вы хотите скопировать:")
        for i, contact in enumerate(copied_contacts):
            print(f"{i + 1}. {contact.strip()}")
        while True:
            selection = int(input("Введите номер контакта: ")) - 1
            if 0 <= selection < len(copied_contacts):
                contact_to_copy = copied_contacts[selection]
                break
            else:
                print("Неверный номер контакта. Попробуйте снова.")

    elif len(copied_contacts) == 1:
        print(f"Найден контакт: {copied_contacts[0].strip()}")
        contact_to_copy = copied_contacts[0]

    else:
        print(f"Контакт с данными {contact_name} не найден.")
        main(file_name)
        return

    with open('new_file.txt', 'a', encoding='UTF-8') as new_file:
        new_file.write(contact_to_copy)

    print("Контакт успешно скопирован в файл new_file.txt.")
    main(file_name)

if __name__ == '__main__':
    file_name = 'phone_book.txt'
    main(file_name)