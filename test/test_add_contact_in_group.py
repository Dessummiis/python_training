from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


def test_add_contact(app, orm):
    # проверки на группы и контакты
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # Выбрать рандомный контакт и подготовить список всех групп
    contact = random.choice(orm.get_contact_list())
    all_groups = orm.get_group_list()
    # Проверить, в каких группах контакт не состоит
    groups_without_contact = []
    for group in all_groups:
        if len(orm.check_if_contact_is_in_group(group, contact)) == 0:
            groups_without_contact.append(group)
    # Выбрать рандомную группу из списка групп без контакта
    group = random.choice(groups_without_contact)
    # Добавить контакт в выбранную группу
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    # Проверить, что контакт добавлен в группу
    # assert



    # contacts_not_in_group = orm.get_contacts_not_in_group(group)
    # contact = random.choice(contacts_not_in_group)

    #
    # assert contact == contacts_in_group...



# Проверить, есть ли контакт для добавления
#   Если нет контакта, то добавить его
# Проверить, есть ли группа для добавления
#   Если нет группы, то добавить ее
# Выбрать рандомный контакт
# Выбрать ВСЕ ГРУППЫ в которых контакт не состоит
# Добавить контакт в рандомную группу
# Проверить, что контакт добавлен в группу