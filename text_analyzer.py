# text_analyzer.py

def word_and_character_count(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count

def vowel_count(text):
    vowels = 'aeiouAEIOU'
    count = {v: text.count(v) for v in vowels}
    return count

def search_and_replace(text, search_word, replace_word):
    return text.replace(search_word, replace_word)

def convert_case(text, to_upper=True):
    if to_upper:
        return text.upper()
    else:
        return text.lower()

def average_word_length(text):
    words = text.split()
    total_characters = sum(len(word) for word in words)
    if len(words) > 0:
        return total_characters / len(words)
    return 0

def check_for_python(text):
    return "Python" in text

def main():
    print("Welcome to the Text Analyzer!")
    
    # Take user input
    text = input("Enter your text: ")

    # Word and Character Count
    word_count, char_count = word_and_character_count(text)
    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")

    # Vowel Count
    vowel_counts = vowel_count(text)
    print("Vowel Counts:")
    for vowel, count in vowel_counts.items():
        print(f"{vowel}: {count}")

    # Average Word Length
    avg_word_length = average_word_length(text)
    print(f"Average Word Length: {avg_word_length:.2f}")

    # Search and Replace Example
    search_word = input("Enter a word to search for: ")
    replace_word = input("Enter a word to replace it with: ")
    replaced_text = search_and_replace(text, search_word, replace_word)
    print(f"Text after replacement: {replaced_text}")

    # Convert Text to Uppercase or Lowercase
    case_choice = input("Do you want to convert text to uppercase (Y/N)? ").lower()
    if case_choice == 'y':
        print("Uppercase Text: ", convert_case(text, True))
    else:
        print("Lowercase Text: ", convert_case(text, False))

    # Check if "Python" exists in text
    if check_for_python(text):
        print('The word "Python" is present in the text.')
    else:
        print('The word "Python" is not found in the text.')

if __name__ == "__main__":
    main()
