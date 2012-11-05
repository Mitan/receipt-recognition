from django.http import HttpResponse
from models import *
import datetime

def visitors(request):
    visitor = Visitor()
    visitor.ip = request.META['REMOTE_ADDR']
    visitor.put()
    result = ""
    visitors = Visitor.all()
    visitors.order("-added_on")
    for visitor in visitors:
        result += visitor.ip + u" visited on " + unicode(visitor.added_on) + u""

    return HttpResponse(result)


def main_page(request):
    return HttpResponse("Welcome to StudFinance server.")


def hello(request):
    return HttpResponse("Hello world!!!")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def get(request, name_):
    p = Person.gql("WHERE name = :1", name_).get()
    if not p:
        return HttpResponse('Nothing found')
    else:
        str = p.toString()
        for relation in PersonAccount.gql("Where person = :1", p):
            str += relation.account.toString()
        return HttpResponse(str)


def add_user(request, name_):
    answer = 'User already exists'
    if not Person.gql("Where name = :1", name_).get():
        Person(name=name_).put()
        answer = 'New user was added'
    return HttpResponse(answer)


def add_to_user(request, name_, num_, pass_):
    p = Person.gql("Where name = :1", name_).get()
    if not p:
        return HttpResponse('This user does not exists')
    a = Account.gql("WHERE number = :1 AND password = :2", num_, pass_).get()
    if not a:
        a = Account(number=num_, password=pass_, parent=p)
        a.put()
    if not PersonAccount.gql("WHERE person = :1 AND account = :2", p, a).get():
        PersonAccount(person=p, account=a).put()
        return HttpResponse('A new account to "' + name_ + '" was added.')
    else:
        return HttpResponse('User already has this account.')


def delete_user(request, name_):
    p = Person.gql("Where name = :1", name_).get()
    if not p:
        return HttpResponse('There is no user with name = ' + name_)
    PersonAccount.gql("WHERE person = :1", p).get().delete()
    p.delete()
    Answer = 'User was cleared'
    return HttpResponse(p.toString() + ' was cleared.')


def del_acc_from_user(request, name_, num, passw):
    p = Person.gql("WHERE name = :1", name_).get()
    if not p:
        return HttpResponse('There is no user with name = ' + name_)
    a = PersonAccount.gql("WHERE person = :1 AND account = :2", p,
        Account.gql("WHERE number = :1 AND password = :2", num, passw).get()).get()
    if not a:
        return HttpResponse('This user does not have this account.')
    a.delete()
    return HttpResponse("User's account deleted.")


    #!password hashing