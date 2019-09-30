# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_contact_fields(Contact(first_name="fname", middle_name="mname", lastname="lnmame", nickname="nickname", title="title", company="company", address="addr1", phone_home="th", phone_mobile="tm",
                             phone_work="tw", phone_fax="fax", email_1="e1", email_2="e2", email_3="e3", homepage="h",
                             secondary_address="addr2", secondary_phone="home2", secondary_notes="notes"))
    app.logout()

