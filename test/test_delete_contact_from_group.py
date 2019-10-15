from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, orm):
    new_group_or_contact = False
    # проверки на группы и контакты
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        new_group_or_contact = True
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
        new_group_or_contact = True
    # Выбрать рандомный контакт и подготовить список всех групп
    all_groups = orm.get_group_list()
    contact = random.choice(orm.get_contact_list())
    # Добавить контакт в группу если не было групп или контактов
    if new_group_or_contact:
        app.contact.add_contact_to_group(contact.id, all_groups.id)
    # Проверить, есть ли контакты в группах и собрать эти группы
    groups_with_contact = []
    for group in all_groups:
        if len(app.contact.get_contacts_in_group(group)) != 0:
            groups_with_contact.append(group)
    # Если нет, то добавить
    if len(groups_with_contact) == 0:
        group = random.choice(all_groups)
        app.contact.add_contact_to_group(contact.id, group.id)
    # Выбрать группу и соответствующий контакт для удаления
    group = random.choice(groups_with_contact)
    contact = random.choice(app.contact.get_contacts_in_group(group))
    # Удалить контакт из группы
    app.contact.delete_contact_from_group(contact.id, group.id)
    # Проверить, что контакт удален
    if orm.check_if_contact_is_in_group(group, contact):
        raise Exception('Contact was not deleted from group')

    # Добавить контакт в выбранную группу
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    # Проверить, что контакт удален



