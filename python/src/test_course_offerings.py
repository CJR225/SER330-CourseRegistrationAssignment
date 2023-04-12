from course_offering_def import CourseOffering
import unittest

class Test_Course_Offering(unittest.TestCase):

        def test_courseOffering(self):

            #Arrange
            courseoffering = CourseOffering("course", "section_number", "year", "quarter")


            #Act
            courseoffering.course = 'SER330'

            #Assert
            assert courseoffering.course == 'SER330'


if __name__ == '__main__':
    unittest.main() 