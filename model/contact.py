from sys import maxsize


class Contact:

    def __init__(self, id=None, name=None, first_name=None, middle_name=None, last_name=None, nickname=None, title=None,
                 company=None, address=None, phone_home=None, phone_mobile=None, phone_work=None,
                 phone_fax=None, email_1=None, email_2=None, email_3=None, homepage=None,
                 secondary_address=None, secondary_phone=None, secondary_notes=None,
                 all_phones=None, all_emails=None, full_assert=None):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.phone_fax = phone_fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.secondary_address = secondary_address
        self.secondary_phone = secondary_phone
        self.secondary_notes = secondary_notes
        self.all_phones = all_phones
        self.all_emails = all_emails
        self.full_assert = full_assert

    def __repr__(self):
        return "%s:%s:%s%s%s%s" % \
               (self.id, self.first_name, self.last_name, self.address, self.all_emails, self.all_phones)

    def __eq__(self, other):
        # Проверка по имени и фамилии, без учета id
        if self.full_assert or other.full_assert is None:
            return (self.id is None or other.id is None or self.id == other.id) \
                   and self.first_name == other.first_name and self.last_name == other.last_name
        else:
            # Проверка по всем полям со страницы контактов, без учета id
            return (self.id is None or other.id is None or self.id == other.id) \
                   and self.first_name == other.first_name and self.last_name == other.last_name \
                   and self.address == other.address and self.all_phones == other.all_phones \
                   and self.all_emails == other.all_emails

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
