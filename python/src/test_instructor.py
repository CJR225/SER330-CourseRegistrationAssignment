import unittest

from instructor_def import Instructor
from person_def import Person
from course_def import Course
from course_offering_def import CourseOffering

class Test_Instructor(unittest.TestCase):

    def test_InstructorInit_WhenAllConditionsAreMet_Succeeds(self):

        #Arrange
        instructor = Instructor("test","test","test","4/20/23","test")
        course = Course("CSC", 375, "Cloud Computing", 3)
        cc1 = CourseOffering(course,"123","2023","1")
        cc2 = CourseOffering(course,"123","2023","1")
        cc3 = CourseOffering(course,"123","2023","1")
        courseOfferingsList = [cc1,cc2,cc3]
        instructor.course_list = courseOfferingsList

        #Act
        returnedCourses = instructor.list_courses()

        #Assert
        assert len(returnedCourses) == len(courseOfferingsList)
   