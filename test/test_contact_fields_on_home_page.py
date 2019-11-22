from model.contact import Contact


def test_contact_fields_on_home_page(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    # получить сортированные списки из ui и db
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    # проверить на соответствие длины списков контактов в ui и db
    assert len(contacts_from_home_page) == len(contacts_from_db)
    # использовать PEP 279 для индексации списка
    for index, contact in enumerate(contacts_from_db):
        # склеить номера телефонов и email-ы для контактов из db
        contacts_from_db[index].all_phones = app.contact.merge_phones_like_on_home_page(contact)
        contacts_from_db[index].all_emails = app.contact.merge_emails_like_on_home_page(contact)
        # сравнить контакт из db с контактом из ui для соответствующего индекса
        assert contacts_from_db[index] == contacts_from_home_page[index]
