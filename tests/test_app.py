import unittest
from app import greet, calculate_grade, validate_email

class TestApp(unittest.TestCase):
    def test_greet(self):
        """Test the greet function with a sample input"""
        self.assertEqual(greet("World"), "Hello, World from Charbel Toumieh!")
        
    def test_greet_empty(self):
        """Test the greet function with empty string"""
        self.assertEqual(greet(""), "Hello,  from Charbel Toumieh!")
        
    def test_greet_special_chars(self):
        """Test the greet function with special characters"""
        self.assertEqual(greet("@#$"), "Hello, @#$ from Charbel Toumieh!")

    def test_calculate_grade_A(self):
        """Test grade calculation for A grade"""
        self.assertEqual(calculate_grade(95), 'A')
        self.assertEqual(calculate_grade(90), 'A')

    def test_calculate_grade_B(self):
        """Test grade calculation for B grade"""
        self.assertEqual(calculate_grade(85), 'B')
        self.assertEqual(calculate_grade(80), 'B')

    def test_calculate_grade_C(self):
        """Test grade calculation for C grade"""
        self.assertEqual(calculate_grade(75), 'C')
        self.assertEqual(calculate_grade(70), 'C')

    def test_calculate_grade_D(self):
        """Test grade calculation for D grade"""
        self.assertEqual(calculate_grade(65), 'D')
        self.assertEqual(calculate_grade(60), 'D')

    def test_calculate_grade_F(self):
        """Test grade calculation for F grade"""
        self.assertEqual(calculate_grade(55), 'F')
        self.assertEqual(calculate_grade(0), 'F')

    def test_calculate_grade_invalid_type(self):
        """Test grade calculation with invalid input type"""
        with self.assertRaises(TypeError):
            calculate_grade("not a number")

    def test_calculate_grade_invalid_range(self):
        """Test grade calculation with out of range values"""
        with self.assertRaises(ValueError):
            calculate_grade(-1)
        with self.assertRaises(ValueError):
            calculate_grade(101)

    def test_validate_email_valid(self):
        """Test email validation with valid emails"""
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name@domain.co.uk"))

    def test_validate_email_invalid(self):
        """Test email validation with invalid emails"""
        self.assertFalse(validate_email("invalid_email"))
        self.assertFalse(validate_email("@domain.com"))
        self.assertFalse(validate_email("user@"))
        self.assertFalse(validate_email("user@domain"))
        self.assertFalse(validate_email(123))  # Invalid type

if __name__ == "__main__":
    unittest.main()