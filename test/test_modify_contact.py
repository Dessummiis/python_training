from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    contact = Contact(first_name="edit_fname", middle_name="edit_mname", last_name="edit_lnmame", nickname="edit_nickname",
                title="edit_title", company="edit_company", address="edit_addr1",
                phone_home="edit_th", phone_mobile="edit_tm", phone_work="edit_tw", phone_fax="edit_fax",
                email_1="edit_e1", email_2="edit_e2", email_3="edit_e3",
                homepage="edit_h", secondary_address="edit_addr2", secondary_phone="edit_home2",
                secondary_notes="edit_notes")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_fist_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="test"))
#     app.contact.modify_first_contact(
#         Contact(first_name="fname_new"))
