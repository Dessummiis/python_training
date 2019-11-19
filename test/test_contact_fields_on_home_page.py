from model.group import Group
from model.contact import Contact


def test_contact_fields_on_home_page(app, orm, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    # for i in contacts_from_db:
    #     contacts_from_home_page[i].all_phones = app.contact.merge_phones_like_on_home_page(i)
    #     contacts_from_home_page[i].all_emails = app.contact.merge_emails_like_on_home_page(i)
    smth = 0
    # checklist = []
    # for contact in contacts_from_db:
    #     if contact in contacts_from_home_page:
    #         checklist.append(True)
    #     else:
    #         checklist.append(False)
    # print (checklist)
    # assert sorted(contact_from_home_page, key=Group.id_or_max) == sorted(contact_from_db, key=Group.id_or_max)
