from student_def import Student
import unittest

class Test_Student(unittest.TestCase):
     def test_student_init(self):

        # Arrange
        student = Student('last_name', 'first_name', 'school', 'date_of_birth', 'username')

        #Act
        student.last_name = 'Rocco'
        student.first_name = 'Chris'
        student.school = 'Quinnipiac'
        student.date_of_birth = '2/25/02'
        student.username = 'cjr225'

        #Assert
        assert student.last_name == 'Rocco'
        assert student.first_name == 'Chris'
        assert student.school == 'Quinnipiac'
        assert student.date_of_birth == '2/25/02'
        assert student.username == 'cjr225'
        assert student.__str__

if __name__ == '__main__':
    unittest.main() 

