import langchain_helper as lch
import streamlit as st

st.title("LinkedIn 'About' Section Generator")

name = st.sidebar.text_area(label = "Your name", max_chars=50)
position = st.sidebar.text_area(label = "Current Job role", max_chars=50)
company = st.sidebar.text_area(label = "Company", max_chars=100)
education = st.sidebar.text_area(label = "Education qualifications", max_chars=500)
# university = st.sidebar.text_area(label = "University name", max_chars=100)
# year_of_completion = st.sidebar.text_area(label = "Year of completion of degree", max_chars=50)
work_experience = st.sidebar.text_area(label = "Please provide your detailed work experience", max_chars=2000)
skills = st.sidebar.text_area(label = "Skills", max_chars=500)
projects = st.sidebar.text_area(label = "Projects (if any)", max_chars=2000)
certifications = st.sidebar.text_area(label = "Certifications (if any)", max_chars=500)

# temperature = st.sidebar.text_area(label = "How creative you want your section to be (0 to 1)", max_chars=50)
# temperature = float(temperature)
use_emojis = st.sidebar.selectbox(
    "Use emojis in output?",
    ["Yes", "No"]
)
temperature = st.sidebar.slider(
    "How creative you want your section to be",
    min_value=0.0,
    max_value=1.0,
    value=0.75,
    step=0.01
)
# openai_api_key = st.sidebar.text_area(label = "GenAI Key", max_chars=200)


# animal_labels = {
#     "Dog": "What color is your dog?",
#     "Cat": "What color is your cat?",
#     "Hamster": "What color is your hamster?",
#     "Rat": "What color is your rat?",
#     "Snake": "What color is your snake?",
#     "Lizard": "What color is your lizard?",
#     "Cow": "What color is your cow?",
# }

# pet_color = st.sidebar.text_area(
#     label=animal_labels[animal_type],
#     max_chars=25
# )

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/rishabkumar7/pets-name-langchain/tree/main)"

if name:
    # if not openai_api_key:
    #   st.info("Please add your GenAI key to continue.")
    #   st.stop()
    response = lch.generate_linkedin_about(name, position, company, education, work_experience, skills, temperature, openai_api_key = "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", use_emojis=use_emojis,projects=projects, certifications=certifications)
    # st.text(response['linkedin_about_section'])
    st.write(response.content)