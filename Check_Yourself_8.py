#                           1

class Auto:
    def ride(self):
        print('Riding on a ground')
class Boat:
    def swim(self):
        print('Floating on water')
class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim()

#                            2

class ContactList(list):
    def __init__(self, list1):
        self.list1 = list1
    def search_by_name(self,name):
        result = []
        for i in self.list1:
            if name in i:
                result.append(i)
        return result

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya'))

