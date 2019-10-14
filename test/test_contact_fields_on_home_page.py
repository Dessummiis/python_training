from model.group import Group


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = map(app.contact.clean, db.get_contact_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
