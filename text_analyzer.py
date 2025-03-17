import streamlit as st
import re
import string
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from textstat import flesch_reading_ease

# Streamlit UI Title
st.title("📖 Text Analyzer")

# User input for text paragraph
text = st.text_area("Enter your paragraph:", height=150)

if text:
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
    
    # Search and Replace Feature
    search_word = st.text_input("Search for a word:")
    replace_word = st.text_input("Replace with:")
    modified_text = text.replace(search_word, replace_word) if search_word and replace_word else text
    
    # Most Frequent Words
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(5)
    
    # Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Dark Mode Toggle
    dark_mode = st.checkbox("🌙 Enable Dark Mode")
    if dark_mode:
        st.markdown("""<style>body { background-color: #222; color: white; }</style>""", unsafe_allow_html=True)
    
    # Display Results
    st.subheader("🔍 Analysis Results")
    st.write(f"**Total Words:** {total_words}")
    st.write(f"**Total Characters:** {total_chars}")
    st.write(f"**Number of Vowels:** {vowel_count}")
    st.write(f"**Number of Sentences:** {sentence_count}")
    st.write(f"**Average Word Length:** {avg_word_length}")
    st.write(f"**Readability Score:** {readability_score:.2f}")
    
    # Modified Text
    if search_word and replace_word:
        st.subheader("📝 Modified Paragraph")
        st.write(modified_text)
    
    # Most Frequent Words
    st.subheader("📊 Top 5 Most Frequent Words")
    for word, freq in most_common_words:
        st.write(f"{word}: {freq} times")
    
    # Word Cloud
    st.subheader("☁ Word Cloud Visualization")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    
    # Real-time Character Counter
    st.subheader("📝 Live Character Count")
    st.write(f"Characters typed: {len(text)}")
    
    # Download Processed Text
    st.subheader("⬇ Download Processed Text")
    st.download_button("Download", modified_text, file_name="processed_text.txt")