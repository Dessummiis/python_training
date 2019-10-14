import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.check_if_contact_is_in_group(Group(id="59"), Contact(id="43"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()