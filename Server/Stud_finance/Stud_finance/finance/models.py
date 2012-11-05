from google.appengine.ext import db

class Visitor(db.Model):
    ip = db.StringProperty()
    added_on = db.DateTimeProperty(auto_now_add=True)


class Person(db.Model):
    name = db.StringProperty()

    def toString(self):
        str = self.name
        return str


class Account(db.Model):
    number = db.StringProperty()
    password = db.StringProperty()

    def toString(self):
        return ' acc #: ' + self.number + ' :acc password:' + self.password


class PersonAccount(db.Model):
    person = db.ReferenceProperty(Person, required=True, collection_name='accounts')
    account = db.ReferenceProperty(Account, required=True, collection_name='people')
