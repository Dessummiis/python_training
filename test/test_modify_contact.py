from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contacts[index]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
