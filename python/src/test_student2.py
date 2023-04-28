import unittest

from student_def import Student
from person_def import Person
from course_def import Course
from course_offering_def import CourseOffering

class Test_Student2(unittest.TestCase):
    
    def test_initial(self):

        student = Student("test","test","test","test","test")

        assert student.last_name == "test"

    def test_credits(self):

        student = Student('test', 'test', 'school', '4/20/23', 'test')
        course = Course("CSC", 375, "Cloud Computing", 3)
        cc1 = CourseOffering(course,"123","2023","1")

        cc1.register_students([student])
        calCredit = student.credits()
        print(calCredit)
        
        assert calCredit == 3
