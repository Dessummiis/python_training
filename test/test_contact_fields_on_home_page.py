from random import randrange


def test_contact_fields_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_edit_page.all_phones = app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    contact_from_edit_page.all_emails = app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page == contact_from_edit_page
