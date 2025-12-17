"""
Helper functions for the VisaVerse Copilot application
"""


def format_requirements_list(requirements):
    """
    Format a list of requirements into markdown bullet points
    
    Args:
        requirements (list): List of requirement strings
    
    Returns:
        str: Formatted markdown string
    """
    if not requirements:
        return "No specific requirements listed"
    
    return "\n".join([f"- {req}" for req in requirements])


def format_tips_list(tips):
    """
    Format a list of tips into markdown with checkmarks
    
    Args:
        tips (list): List of tip strings
    
    Returns:
        str: Formatted markdown string
    """
    if not tips:
        return "No tips available"
    
    return "\n".join([f"✓ {tip}" for tip in tips])


def get_progress_color(percentage):
    """
    Get color for progress bar based on percentage
    
    Args:
        percentage (float): Percentage value (0-100)
    
    Returns:
        str: Color name or hex code
    """
    if percentage >= 90:
        return "green"
    elif percentage >= 70:
        return "blue"
    elif percentage >= 50:
        return "orange"
    else:
        return "red"


def get_readiness_message(percentage):
    """
    Get readiness message based on completion percentage
    
    Args:
        percentage (float): Percentage value (0-100)
    
    Returns:
        str: Appropriate message for the percentage
    """
    if percentage == 100:
        return "✓ Congratulations! You have all required documents ready."
    elif percentage >= 80:
        return "You're almost there! Just a few more documents needed."
    elif percentage >= 60:
        return "Good progress! Continue preparing the remaining documents."
    elif percentage >= 40:
        return "You've made a start. Keep gathering the required documents."
    else:
        return "⚠️ You need to prepare more documents before applying."


def get_success_rate_emoji(rate):
    """
    Get emoji for success rate
    
    Args:
        rate (str): Success rate description
    
    Returns:
        str: Appropriate emoji
    """
    rate_lower = rate.lower()
    if 'very high' in rate_lower:
        return "🌟"
    elif 'high' in rate_lower:
        return "✅"
    elif 'moderate' in rate_lower:
        return "⚠️"
    else:
        return "❌"


def validate_text_input(text, min_length=10):
    """
    Validate text input
    
    Args:
        text (str): Text to validate
        min_length (int): Minimum required length
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "This field cannot be empty"
    
    if len(text.strip()) < min_length:
        return False, f"Text must be at least {min_length} characters long"
    
    return True, None


def truncate_text(text, max_length=100, suffix="..."):
    """
    Truncate text to a maximum length
    
    Args:
        text (str): Text to truncate
        max_length (int): Maximum length
        suffix (str): Suffix to add if truncated
    
    Returns:
        str: Truncated text
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def safe_get(dictionary, keys, default=None):
    """
    Safely get nested dictionary value
    Reserved for future use with complex nested data structures
    
    Args:
        dictionary (dict): Dictionary to search
        keys (list): List of keys for nested access
        default: Default value if key not found
    
    Returns:
        Value at the nested key or default
    """
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def format_percentage(value, decimal_places=0):
    """
    Format a value as a percentage
    Reserved for future use in analytics and reporting features
    
    Args:
        value (float): Value to format (0-100)
        decimal_places (int): Number of decimal places
    
    Returns:
        str: Formatted percentage string
    """
    return f"{value:.{decimal_places}f}%"


def create_display_dict(data, labels):
    """
    Create a display-friendly dictionary from data
    Reserved for future use in data presentation features
    
    Args:
        data (dict): Source data dictionary
        labels (dict): Mapping of keys to display labels
    
    Returns:
        dict: Display-friendly dictionary
    """
    display = {}
    for key, label in labels.items():
        if key in data:
            display[label] = data[key]
    return display
