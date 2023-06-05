import psycopg2

connection = psycopg2.connect(
    database="CallGrandma", 
    user='postgres',
    password='root',
    host='localhost', 
    port='5432'
)

cursor = connection.cursor()
class Contacts:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    def save(self):
        query = f'''INSERT INTO people (person_name, city) VALUES ('{self.name}', '{self.city}')'''
        cursor.execute(query)
        connection.commit()
    @classmethod
    def get_by_name(cls, name):
        query = f'''SELECT city FROM people 
        WHERE person_name = '{name}' '''
        cursor.execute(query)
        result=cursor.fetchone()
        result_str=str(result[0])
        return result_str
    
    # @classmethod
    # def check_by_name(cls, name):
    #     query = f'''SELECT person_name FROM people WHERE person_name = '{name}')'''
    #     result=cursor.execute(query)
    #     connection.commit()
    #     print(result)
    #     return query
        
    # def update(self, new_city):
    #     query = f'''UPDATE people SET city = {new_city}
    #     WHERE person_name = '{self.name}' '''
    #     cursor.execute(query)
    #     connection.commit()
        
    # def delete(self):
    #     query = f'''DELETE people WHERE person_name = '{self.new_name}'
    #     WHERE person_name = '{self.name}' '''
    #     cursor.execute(query)
    #     connection.commit()
    @classmethod
    def inlist(cls):
        listname=[]
        query = f'''SELECT person_name FROM people '''
        cursor.execute(query)
        result=cursor.fetchall()
        listname.append(result)
        return listname

# Sara = Contacts('Sara', 'Berlin')
# Joe = Contacts('Joe', 'London')
# Sara.save()
# Sara.get_by_name('Sara')
# # Sara.delete()

# Joe.update('Stambul')
# Joe.save()

# print(Contacts.get_by_name('Sara')) # Show city
# print(Contacts.inlist())
