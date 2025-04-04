import re
from collections import Counter
from textstat import flesch_reading_ease

# Function to analyze the text
def analyze_text(text):
    # Word and Character Count
    words = text.split()
    total_words = len(words)
    total_chars = len(text)
    
    # Vowel Count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    
    # Sentence Count
    sentences = re.split(r'[.!?]', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Average Word Length
    avg_word_length = round(total_chars / total_words, 2)
    
    # Readability Score
    readability_score = flesch_reading_ease(text)
    
    # Most Frequent Words
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(5)
    
    # Results
    results = {
        "total_words": total_words,
        "total_chars": total_chars,
        "vowel_count": vowel_count,
        "sentence_count": sentence_count,
        "avg_word_length": avg_word_length,
        "readability_score": readability_score,
        "most_common_words": most_common_words,
    }
    
    return results

# Function to display results
def display_results(results):
    print(f"Total Words: {results['total_words']}")
    print(f"Total Characters: {results['total_chars']}")
    print(f"Number of Vowels: {results['vowel_count']}")
    print(f"Number of Sentences: {results['sentence_count']}")
    print(f"Average Word Length: {results['avg_word_length']}")
    print(f"Readability Score: {results['readability_score']:.2f}")
    
    print("\nTop 5 Most Frequent Words:")
    for word, freq in results['most_common_words']:
        print(f"{word}: {freq} times")

# Main Function
if __name__ == "__main__":
    # User input for text
    text = input("Enter your text to analyze: ")

    # Analyze the text
    results = analyze_text(text)
    
    # Display the analysis results
    display_results(results)
