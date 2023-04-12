
import unittest

from person_def import Person

class Test_Person(unittest.TestCase):
    def test_PersonInit_WhenAllConditionsAreMet_Succeeds(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        person.last_name = 'Test'
        person.first_name = 'Test'
        person.school = 'QU'
        person.date_of_birth = '0/00/00'
        person.affiliation = 'student'
        person.username = 'test'

        # Assert
        assert person.last_name == 'Test'
        assert person.first_name == 'Test'
        assert person.school == 'QU'
        assert person.date_of_birth == '0/00/00'
        assert person.affiliation == 'student'
        assert person.username == 'test'


    

if __name__ == '__main__':
    unittest.main() 