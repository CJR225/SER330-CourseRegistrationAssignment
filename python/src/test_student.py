import unittest

from student_def import Student
from person_def import Person
from course_def import Course
from course_offering_def import CourseOffering

class Test_Student(unittest.TestCase):
     def test_student_init(self):

        # Arrange
        
        student = student('test', 'test', 'school', '4/20/23', 'test')
       
        #Act

        #Assert
        assert student.first_name == "test"

     def test_credits(self):

      #Arrange
      total = 0
      student = student('test', 'test', 'school', '4/20/23', 'test')
      course1 = Course("CSC", 375, "Cloud Computing", 3)
      cc1 = CourseOffering(course1,"123","2023","1")
      courseOfferings = [cc1]
      student.course_list = courseOfferings

      #Act
      total = course1.credits
      print(total)
      #Assert
      assert student.credits == 3