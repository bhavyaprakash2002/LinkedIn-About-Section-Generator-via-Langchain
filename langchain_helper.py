import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def generate_linkedin_about(name, position, company, education, work_experience, skills, temperature, openai_api_key, use_emojis, projects, certifications):
    # llm = OpenAI(temperature = temperature, openai_api_key=openai_api_key)
    llm=ChatGroq(groq_api_key="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",model_name="llama-3.1-8b-instant",temperature=temperature)

    emoji_instruction = (
    "Please use emojis wherever appropriate to make it engaging."
    if use_emojis == "Yes"
    else "Do not use any emojis in the output.")

    prompt_template_name = PromptTemplate(
        input_variables = ['name', 'position', 'company', 'education', 'work_experience', 'skills', 'temperature', 'emoji_instruction', 'certifications', 'projects'],

        template = "You are an expert linkedIn optimizer. My name is {name}. I am currently working as {position} at {company}. My educational qualifications are {education}. I am giving you my work experience {work_experience}. Here are the skills that I am expert in {skills}. {emoji_instruction}. I have also created some {projects} which showcase my expertise. I have these {certifications}. I want you to write a very professional linkedIn 'About' section for me. Please use emojis wherever necessary to make it fun to read. Also, please do not generate anything on your own. The section should contain every information provided to you. Please use {temperature} level of creativity in creating your answers, this scale is between 0 to 1. The flow should be like, you should write an overview first, then go into details. Overview->It should mention my key skills along with current job title and company. Details-> You should start with highlighting my work experience, then projects, then education (for the education it is not necessary to mention the grades) and then certifications. When writing work experience avoid writing the exact same format that I have given. Try to combine the work experiences from each organization into 2-3 lines maximum. If there is a single organization mentioned, then explain the work experience into 4-5 lines. If any of the information is not given like education or work experience, or anything else, please don't mention anything about those in the output."
    )

    # name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="linkedin_about_section")
    chain = prompt_template_name | llm
    response = chain.invoke({'name': name, 
                           'position': position,
                           'company': company,
                           'education':education,
                        #    'university':university,
                        #    'year_of_completion':year_of_completion,
                           'work_experience':work_experience,
                           'skills':skills,
                           'temperature':temperature,
                           'openai_api_key':openai_api_key, 
                           'emoji_instruction': emoji_instruction,
                           'certifications': certifications,
                           'projects':projects
                           })
    
    return response


if __name__ == "__main__":
    print(generate_linkedin_about("Bhavya", "Analyst", "Bain", "B.Tech", '''DATA ANALYST | Bain Capability Network | Gurgaon, India	July 2025 – present
•	Machine Learning & Predictive Modeling
o	Built machine learning models for large-scale datasets, generating probability to identify high-likelihood buyers.
o	Owned end-to-end ML pipeline including EDA, feature engineering, modeling, validation, and performance evaluation on ~3M data points, improving model accuracy, robustness, and interpretability.
•	Agentic AI & Advanced Analytics Innovation
o	Contributed to development of Agentic AI based solution to define Ideal Customer Profiles (ICPs) by combining qualitative and quantitative data for improved customer targeting.
o	Designed a web-search driven agent to enrich dataset of ~700K rows with external qualitative signals, enabling inference of ICP criteria beyond structured internal datasets.
o	Architected a data driven agent to identify ICPs from historical dataset, leveraging past performance patterns to improve targeting accuracy by 15%.
•	Delivery, Quality & Stakeholder Management
o	Ensured on-time, high-quality delivery of client-ready outputs by adhering to strict deadlines and producing polished, insight-driven slides, improving communication effectiveness and reducing iteration cycles by 15%.
o	Clearly communicated analytical workstreams and daily outputs to stakeholders, balancing technical depth with clarity to ensure alignment on objectives, insights, and next steps.
''', '''•	Programming Languages: Python, SQL
•	Analytics Tools: Tableau, Alteryx, Excel
•	AI & ML: Statistics, Machine Learning, Agentic AI, Prompt Engineering
•	Soft Skills: Effective Communication, Business Acumen
''','0.5', "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", "Yes", 'google', 'Project alpha'))
