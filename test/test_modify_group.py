from model.group import Group

# def test_modify_group(app):
#     app.group.modify_first_group(Group(name="edit_group_name", header="edit_group_header", footer="edit_group_footer"))
#     app.session.logout()

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()