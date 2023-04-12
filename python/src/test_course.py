from course_def import Course
import unittest

class Test_Course(unittest.TestCase):
    def test_course(self):

        #Arrange
        course = Course('department', 'number', 'name', 'credits')
        credits = 3
        number = 330
        #Act
        course.department = 'SER'
        course.number = number
        course.credits = credits
        course.name = 'Quality Assurance'

        #Assert
        assert course.department == 'SER'
        assert course.number == number
        assert course.credits == credits
        assert course.name == 'Quality Assurance'
        assert course.__str__ 

if __name__ == '__main__':
    unittest.main() 