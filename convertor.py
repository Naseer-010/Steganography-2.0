def grayscale_to_rgb_chars(grayscale_value):
    """
    Convert a grayscale value (0-255) into a list of three characters 
    representing the RGB values.
    
    Args:
        grayscale_value (int): A value between 0 and 255
        
    Returns:
        list: A list containing three characters representing the R, G, B values
    """
    # Ensure the grayscale value is within the valid range
    grayscale_value = max(0, min(255, int(grayscale_value)))
    
    # For grayscale, R = G = B = grayscale_value
    # Convert the integer value to a character using chr()
    rgb_char = chr(grayscale_value)
    
    # Return a list with the same character repeated three times
    return [rgb_char, rgb_char, rgb_char]

# Example usage
# grayscale = 120
# rgb_chars = grayscale_to_rgb_chars(grayscale)
# print(f"Grayscale value {grayscale} converted to RGB chars: {rgb_chars}")
# print(f"ASCII values of the characters: {[ord(c) for c in rgb_chars]}")