class Contact:
    def init(self, contact_id, name, phone_number):
        self.id = contact_id
        self.name = name
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return phone_number.isdigit() and len(phone_number) == 10
class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id += 1
            new_contact = Contact
            cls.all_contacts.append(new_contact)
            print(f"Контакт {name} успешно добавлен.")
        else:
            raise ValueError(f"Ошибка: Номер {phone_number} некорректен (должно быть 10 цифр).")

    @classmethod
    def remove_contact(cls, contact_id):
        cls.all_contacts = [c for c in cls.all_contacts if c.id != contact_id]
        print(f"Контакт с ID {contact_id} удален (если он существовал).")
try:
    ContactList.add_contact("Вася Пупкин", "0700100200")
    ContactList.add_contact("Виктор Цой", "0500123456"),
    print(f"Последний ID: {ContactList.last_id}")
    ContactList.remove_contact(1)
    for contact in ContactList.all_contacts:
        print(f"Имя: {contact.name}, Тел: {contact.phone}, ID: {contact.id}")
    ContactList.add_contact("Джон Джонс", "5551234")
except ValueError as e:
    print(e)