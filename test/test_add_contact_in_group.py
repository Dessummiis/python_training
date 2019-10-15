from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, orm):
    # проверки на группы и контакты
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    # Выбрать рандомный контакт и подготовить список всех групп
    contact = random.choice(orm.get_contact_list())
    all_groups = orm.get_group_list()
    # Проверить, в каких группах контакт не состоит
    groups_without_contact = []
    for group in all_groups:
        if not orm.check_if_contact_is_in_group(group, contact):
            groups_without_contact.append(group)
    # Если контакт входит во все группы, то создать новую группу
    if len(groups_without_contact) == 0:
        app.group.create(Group(name="test"))
        app.open_main_page()
        groups_without_contact = orm.get_group_list()
    # Выбрать рандомную группу из списка групп без контакта
    group = random.choice(groups_without_contact)
    # Добавить контакт в выбранную группу
    app.contact.add_contact_to_group(contact.id, group.id)
    # Проверить, что контакт добавлен в группу
    if not orm.check_if_contact_is_in_group(group, contact):
        raise Exception('Contact not found in group')


# Проверить, есть ли контакт для добавления
#   Если нет контакта, то добавить его
# Проверить, есть ли группа для добавления
#   Если нет группы, то добавить ее
# Выбрать рандомный контакт
# Выбрать ВСЕ ГРУППЫ в которых контакт не состоит
# Добавить контакт в рандомную группу
# Проверить, что контакт добавлен в группу