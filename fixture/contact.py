from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_main_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_main_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.open_main_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.open_main_page()

    def fill_contact_fields(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.phone_fax)
        self.change_field_value("email", contact.email_1)
        self.change_field_value("email2", contact.email_2)
        self.change_field_value("email3", contact.email_3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.secondary_address)
        self.change_field_value("phone2", contact.secondary_phone)
        self.change_field_value("notes", contact.secondary_notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_main_page()
        contacts = []
        for element in wd.find_elements_by_name("selected[]"):
            text = element.get_attribute("title")
            id = element.get_attribute("value")
            contacts.append(Contact(name=text, id=id))
        return contacts

