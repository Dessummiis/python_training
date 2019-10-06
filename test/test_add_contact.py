# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="fname", middle_name="mname", last_name="lnmame", nickname="nickname", title="title",
                      company="company", address="addr1", phone_home="th", phone_mobile="tm",
                      phone_work="tw", phone_fax="fax", email_1="e1", email_2="e2", email_3="e3", homepage="h",
                      secondary_address="addr2", secondary_phone="home2", secondary_notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)