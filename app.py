def greet(name):
    """
    A simple greeting function that returns a hello message.
    
    Args:
        name (str): Name of the person to greet
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name} from Charbel Toumieh!"

def calculate_grade(score):
    """
    Calculate letter grade from numerical score.
    
    Args:
        score (float): Numerical score between 0 and 100
        
    Returns:
        str: Letter grade
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
        
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
        
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def validate_email(email):
    """
    Simple email validation.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    if not isinstance(email, str):
        return False
        
    if '@' not in email or '.' not in email:
        return False
        
    local, domain = email.split('@')
    
    if not local or not domain:
        return False
        
    if '.' not in domain:
        return False
        
    return True


if __name__ == "__main__":
    print(greet("World"))
    print(calculate_grade(85))
    print(validate_email("test@example.com"))