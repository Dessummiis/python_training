from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(
        Contact(first_name="edit_fname", middle_name="edit_mname", lastname="edit_lnmame", nickname="edit_nickname",
                title="edit_title", company="edit_company", address="edit_addr1", phone_home="edit_th",
                phone_mobile="edit_tm",
                phone_work="edit_tw", phone_fax="edit_fax", email_1="edit_e1", email_2="edit_e2", email_3="edit_e3",
                homepage="edit_h",
                secondary_address="edit_addr2", secondary_phone="edit_home2", secondary_notes="edit_notes"))
    app.session.logout()
