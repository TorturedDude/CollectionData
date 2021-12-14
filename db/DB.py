import json

class DB:

    path1 = '/Users/artemgolovanov/Desktop/OlegLab4/db/users.json'
    path2 = '/Users/artemgolovanov/Desktop/OlegLab4/db/employees.json'
    dataUsers = {}
    dataUsers['Users'] = []
    dataFilms = {}
    dataFilms['Employee'] = []

    def GetUser(self, login, password):

        with open(self.path1, 'r') as file:
            data = json.load(file)

        for i in data['Users']:
            if (i['login'] == login)and(i['password'] == password):
                flag = True

        return flag



    def WriteUser(self, user):

        with open(self.path1, 'r') as file:
            data = json.load(file)

        self.dataUsers['Users'] = data['Users']

        self.dataUsers['Users'].append(
            {
                'name' : user.Name,
                'login' : user.Login,
                'password' : user.Password
            })

        with open(self.path1, 'w') as file:
            json.dump(self.dataUsers, file)

        pass

    def WriteEmployee(self, film):

        with open(self.path2, 'r') as file:
            data = json.load(file)

        self.dataFilms['Employee'] = data['Employee']

        self.dataFilms['Employee'].append(
            {
                'name' : film.Name,
                'department' : film.Department,
                'phone' : film.Phone
            })

        with  open(self.path2, 'w') as file:
            json.dump(self.dataFilms, file)

        pass

    def GetAllEmployees(self):

        with open(self.path2, 'r') as file:
            data = json.load(file)

        return data