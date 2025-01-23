class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
    @staticmethod
    def courses_trail(trail):
        if trail == "python":
            courses = ["Python Basics", "Python Advanced", "Python Projects"]
        elif trail == "Automação com Python":
            courses = ["Web Scraping", "Selenium", "Python Projects"]
        else:
            courses = ["A definir"]
        return courses
print(Course.courses_trail("python"))

#F097