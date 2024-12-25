


# import requests
# from bs4 import BeautifulSoup
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.util import ngrams
# nltk.download('stopwords', download_dir='./nltk_data')
# nltk.download('punkt_tab') 

# import streamlit as st # type: ignore
# from feedback_tab import feedback_tab

# nltk.download('stopwords')
# nltk.download('punkt')


# st.title('SEO Analyzer')
# url = st.text_input('Enter URL')

# def apply_custom_styles():
#     """Applies custom CSS styles to the Streamlit app."""
#     custom_css = """
#     <style>
#         /* Change background color */
#         body {
#             background-color: #B7A83A;
#         }

#         /* Add a background image */
#         .stApp {
#             background-image: url('https://your-image-url.com/image.jpg');
#             background-size: cover;
#             background-position: center;
#         }

#         /* Change text and header colors */
#         h1, h2, h3, h4, h5, h6 {
#             color: #3C5E7D;
#         }

#         /* Customize button colors */
#         button {
#             background-color: #3C5E7D !important;
#             color: white  !important;
#             border: none !important;
#         }
        
#         /* Customize input field colors */
#         input {
#             background-color: #EFEDE8 !important;
#             color: #69582D !important;
#         }
#         # rgba(255, 255, 255, 0.8)
#         /* Add transparency to the main container */
#         .block-container {
#             background-color: ;
#             padding: 20px;
#             border-radius: 15px;
#         }
#     </style>
#     """
#     st.markdown(custom_css, unsafe_allow_html=True)

# # here i will call the function in the beginning of my app
# apply_custom_styles()





# def seo_analysis(url):
# #here i'm saving the warnings in my lists
#     good = []
#     bad = []
# # Send a get request
#     response = requests.get(url)
# # check the response status code
#     if response.status_code != 200:
#         st.error("Error: Unable to access the website.")
#         return

# # here I'm parsing the html content
#     soup = BeautifulSoup(response.content, 'html.parser')

# # here I'm extracting the title and description
#     title = soup.find('title').get_text()
#     description = soup.find('meta', attrs={'name': 'description'})['content']

# # Check if the title and description exist using boolean logic
#     if title:
#         good.append("Title Exists! Great!")
#     else:
#         bad.append("Title does not exist! Add a Title")

#     if description:
#         good.append("Description Exists! Great!")
#     else:
#         bad.append("Description does not exist! Add a Meta Description")

# # here we are grabbing the headings
#         hs = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
#         h_tags = []
#         for h in soup.find_all(hs):
#             good.append(f"{h.name}-->{h.text.strip()}")
#             h_tags.append(h.name)

#         if 'h1' not in h_tags:
#             bad.append("No H1 found!")

# # we will extract the images without Alt
#     for i in soup.find_all('img', alt=''):
#         bad.append(f"No Alt: {i}") 

# # Extract keywords
# # Grab the text from the body of html
#     bod = soup.find('body').text

# # Extract all the words in the body and lowercase them in a list
#     words = [i.lower() for i in word_tokenize(bod)]

# #extract the bigrams from the tokens
#     bi_grams = ngrams(words, 2)
#     freq_bigrams = nltk.FreqDist(bi_grams)
#     bi_grams_freq= freq_bigrams.most_common(10) #contains the 10 most commob bigrams in our text


# # Grab a list of stop words in the language applied
#     sw = nltk.corpus.stopwords.words('english')
#     new_words = []

# # Put the tokens which are not stopwords and are actual words (no punctuation) in a new list
#     for i in words:
#         if i not in sw and i.isalpha():
#             new_words.append(i)

# # Extract the fequency of the words and get the 10 most common ones
#     freq = nltk.FreqDist(new_words)
#     keywords= freq.most_common(15)

# # Print the results
#     tab1, tab2, tab3, tab4, tab5 = st.tabs(['keywords', 'Bigrams', 'Good', 'Bad', 'Feedback'])
#     with tab1:
#         for i in keywords:
#             st.text(i)
#     with tab2:
#         for i in bi_grams_freq:
#             st.text(i)
#     with tab3:
#         for i in good:
#             st.success(i)
#     with tab4:
#         for i in bad:
#             st.text(i)
#     with tab5:
#         feedback_tab()


    
# # Call the function to see the results
# seo_analysis(url) # this is for the user to input a url of their choosing

# #Adding more informaiton to describe the apps use and importance
# st.title("Importance of this Analyzer")
# st.write("An SEO (Search Engine Optimization) analyzer is a critical tool for businesses, marketers, and website owners aiming to enhance their online presence. Here are the key benefits and importance of an SEO analyzer.")
# st.write("Improve Website Visibility")
# st.write("Boost Organic Traffic")
# st.write("Enhance User Experience(UX)")
# st.write("Competitive Edge")
# st.write("Diagnose SEO Issues")
# st.write("Supports Strategic Decision-Making")
# st.write("Cost-Effective Marketing")



# st.write("An SEO analyzer is vital for ensuring a website is optimized to reach its full potential, providing valuable insights that drive traffic, improve user experience, and ultimately contribute to the growth of the business. It empowers website owners to stay competitive in the ever-changing digital landscape.")


import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

import streamlit as st # type: ignore
from feedback_tab import feedback_tab

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


st.title('SEO Analyzer')
url = st.text_input('Enter URL')

with st.sidebar:
    st.header("Customize Colors")
    background_color = st.color_picker("Background Color", value="#B7A83A") # set default color
    text_header_color = st.color_picker("Text/Header Color", value="#3C5E7D") # set default color
    button_color = st.color_picker("Button Color", value="#3C5E7D") # set default color
    input_color = st.color_picker("Input Field Color", value="#EFEDE8") # set default color
    input_text_color = st.color_picker("Input Text Color", value="#69582D") # set default color



def apply_custom_styles():
    """Applies custom CSS styles to the Streamlit app."""
    custom_css = """
    <style>
        /* Change background color */
        body {
            background-color: #B7A83A;
        }

        /* Add a background image */
        .stApp {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }

        /* Change text and header colors */
        h1, h2, h3, h4, h5, h6 {
            color: #3C5E7D;
        }

        /* Customize button colors */
        button {
            background-color: #3C5E7D !important;
            color: white  !important;
            border: none !important;
        }
        
        /* Customize input field colors */
        input {
            background-color: #EFEDE8 !important;
            color: #69582D !important;
        }
        # rgba(255, 255, 255, 0.8)
        /* Add transparency to the main container */
        .block-container {
            background-color: ;
            padding: 20px;
            border-radius: 15px;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# here i will call the function in the beginning of my app
apply_custom_styles()





def seo_analysis(url):
#here i'm saving the warnings in my lists
    good = []
    bad = []
# Send a get request
    response = requests.get(url)
# check the response status code
    if response.status_code != 200:
        st.error("Error: Unable to access the website.")
        return

# here I'm parsing the html content
    soup = BeautifulSoup(response.content, 'html.parser')

    # here I'm extracting the title and description
    title = soup.find('title').get_text() if soup.find('title') else None # if it exists the get the text, if not it is none

    description_tag = soup.find('meta', attrs={'name': 'description'}) # find meta description
    if description_tag:
        description = description_tag['content']
        good.append("Description Exists! Great!")
    else:
        description = None
        bad.append("Description does not exist! Add a Meta Description")

    # Check if the title and description exist using boolean logic
    if title:
        good.append("Title Exists! Great!")
    else:
        bad.append("Title does not exist! Add a Title")


# here we are grabbing the headings
    hs = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    h_tags = []
    for h in soup.find_all(hs):
        good.append(f"{h.name}-->{h.text.strip()}")
        h_tags.append(h.name)

    if 'h1' not in h_tags:
        bad.append("No H1 found!")

# we will extract the images without Alt
    for i in soup.find_all('img', alt=''):
        bad.append(f"No Alt: {i}") 

# Extract keywords
# Grab the text from the body of html
    bod = soup.find('body').text

# Extract all the words in the body and lowercase them in a list
    words = [i.lower() for i in word_tokenize(bod)]

#extract the bigrams from the tokens
    bi_grams = ngrams(words, 2)
    freq_bigrams = nltk.FreqDist(bi_grams)
    bi_grams_freq= freq_bigrams.most_common(10) #contains the 10 most commob bigrams in our text


# Grab a list of stop words in the language applied
    sw = nltk.corpus.stopwords.words('english')
    new_words = []

# Put the tokens which are not stopwords and are actual words (no punctuation) in a new list
    for i in words:
        if i not in sw and i.isalpha():
            new_words.append(i)

# these variables extract the fequency of the words and get the 10 most common ones
    freq = nltk.FreqDist(new_words)
    keywords = freq.most_common(15)

# here we print the results
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['keywords', 'Bigrams', 'Good', 'Bad', 'Feedback'])
    with tab1:
        for i in keywords:
            st.text(i)
    with tab2:
        for i in bi_grams_freq:
            st.text(i)
    with tab3:
        for i in good:
            st.success(i)
    with tab4:
        for i in bad:
            st.text(i)
    with tab5:
        feedback_tab()


    
# here I call the function to see the results
if url:
    seo_analysis(url) # this is for the user to input a url of their choosing

#I'm adding more informaiton to describe the apps use and importance
st.title("Importance of this Analyzer")
st.write("An SEO (Search Engine Optimization) analyzer is a critical tool for businesses, marketers, and website owners aiming to enhance their online presence. Here are the key benefits and importance of an SEO analyzer.")
st.write("Improve Website Visibility")
st.write("Boost Organic Traffic")
st.write("Enhance User Experience(UX)")
st.write("Competitive Edge")
st.write("Diagnose SEO Issues")
st.write("Supports Strategic Decision-Making")
st.write("Cost-Effective Marketing")



st.write("An SEO analyzer is vital for ensuring a website is optimized to reach its full potential, providing valuable insights that drive traffic, improve user experience, and ultimately contribute to the growth of the business. It empowers website owners to stay competitive in the ever-changing digital landscape.")