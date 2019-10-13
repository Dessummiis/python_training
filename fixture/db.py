import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, address, home, mobile, work, phone2,"
                           "email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, middle_name, last_name, address, phone_home, phone_mobile, phone_work, secondary_phone,
                 email_1, email_2, email_3) = row
                list.append(Contact(id=str(id), first_name=first_name, middle_name=middle_name, last_name=last_name,
                                    address=address, phone_home=phone_home, phone_mobile=phone_mobile,
                                    phone_work=phone_work, secondary_phone=secondary_phone,
                                    email_1=email_1, email_2=email_2, email_3=email_3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
