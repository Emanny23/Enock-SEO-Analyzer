
import streamlit as st





def feedback_tab():
    """Displays the feedback tab in the Streamlit app."""
    st.header("Feedback")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.radio("Rate this SEO Analyzer:", [1, 2, 3, 4, 5], horizontal=True)
    feedback = st.text_area("Share your comments:")
    
    if st.button("Submit Feedback"):
        if feedback.strip():
            # Save feedback and display sentiment
            save_feedback(selected, feedback)
            st.success(f"Thank you for your feedback! You selected {sentiment_mapping[selected - 1]} star(s).")
        else:
            st.warning("Please enter feedback before submitting.")

def save_feedback(rating, feedback):
    """Save feedback to a local file (or database)."""
    with open("feedback.csv", "a") as file:
        file.write(f"{rating}, {feedback}\n")
