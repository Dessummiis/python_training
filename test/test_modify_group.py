from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="edit_group_name", header="edit_group_header", footer="edit_group_footer"))
    app.session.logout()
