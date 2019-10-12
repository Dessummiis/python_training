from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Contact(first_name="", middle_name="",last_name="", address="", phone_home="", phone_mobile="",
            phone_work="", secondary_phone="", email_1="", email_2="", email_3="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
            last_name=random_string("last_name", 10), address=random_string("address", 10),
            phone_home=random_string("phone_home", 10), phone_mobile=random_string("phone_mobile", 10),
            phone_work=random_string("phone_work", 10), secondary_phone=random_string("secondary_phone", 10),
            email_1=random_string("email_1", 10), email_2=random_string("email_2", 10), email_3=random_string("email_3", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
