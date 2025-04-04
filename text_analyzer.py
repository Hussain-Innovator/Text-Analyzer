import streamlit as st
import textstat

# UI Title
st.title("📑 Text Analyzer")

# User Input
text = st.text_area("Enter your text here:", height=200)

if text:
    # Word and Character Count
    words = len(text.split())
    chars = len(text)

    # Vowel & Consonant Count
    vowels = sum(1 for char in text.lower() if char in "aeiou")
    consonants = sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")

    # Readability Score
    readability = textstat.flesch_reading_ease(text)

    # Display Analysis
    st.subheader("📊 Text Analysis Results:")
    st.write(f"🔢 **Word Count:** {words}")
    st.write(f"🔠 **Character Count:** {chars}")
    st.write(f"🔡 **Vowel Count:** {vowels}")
    st.write(f"🔤 **Consonant Count:** {consonants}")
    st.write(f"📖 **Readability Score:** {readability:.2f}")

    # Search and Replace Feature
    st.subheader("🔍 Find & Replace")
    search_word = st.text_input("Word to Find:")
    replace_word = st.text_input("Replace With:")
    if st.button("Replace"):
        modified_text = text.replace(search_word, replace_word)
        st.text_area("Modified Text:", modified_text, height=200)

    # Case Conversion
    st.subheader("🔠 Case Conversion")
    if st.button("Convert to UPPERCASE"):
        st.text_area("Uppercase Text:", text.upper(), height=200)
    if st.button("Convert to lowercase"):
        st.text_area("Lowercase Text:", text.lower(), height=200)

    # Download Processed Text
    st.subheader("📥 Download Processed Text")
    st.download_button("Download as TXT", text, file_name="analyzed_text.txt")

