from course_offering_def import CourseOffering
from course_def import Course
from student_def import Student
import unittest

class Test_Course_Offering(unittest.TestCase):

        def test_VerifyCanRegisterStudents_WhenAllconditionsAreMet_ReturnsTrue(self):

            #Arrange
            course = Course("CSC", 375, "Cloud Computing", 3)
            cc = CourseOffering(course,"123","2023","1")
            student1 = Student("Test","test","school","4/20/2023","test")
            student2 = Student("Test","test","school","4/20/2023","test")
            student3 = Student("Test","test","school","4/20/2023","test")
            studentsList = [student1, student2,student3]

            #Act
            cc.register_students(studentsList)

            #Assert
            assert len(cc.register_students) ==len(studentsList)
            assert len(student1.course_list) != 0
        
            

