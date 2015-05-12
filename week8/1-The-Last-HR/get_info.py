import requests


class GetInfo:
    def __init__(self, url):
        self.url = url
        self.students = []
        self.get_info_from_url()

    def get_info_from_url(self):
        info = requests.get(self.url)

        for student in info.json():
            name = student["name"]
            github = student["github"]
            courses = []
            for course in student["courses"]:
                courses.append(course["name"])
            self.students.append({
                "name": name,
                "courses": courses,
                "github": github,
                })

    def print_obj(self):
        for x in self.students:
            print(x["name"], " --- ", x["courses"])

    def get_name_and_github(self):
        data = []
        elem_data = ()
        for x in self.students:
            elem_data = (x["name"], x["github"])
            data.append(elem_data)
        return data

    def get_courses(self):
        data_courses = set()
        for student in self.students:
            for s_c in student["courses"]:
                data_courses.add((s_c,))
        return list(data_courses)

    def get_name_courses(self):
        name_course_all = []
        name_cource_part = ()
        for x in self.students:
            name_cource_part = (x["name"], x["courses"])
            name_course_all.append(name_cource_part)
        return name_course_all

