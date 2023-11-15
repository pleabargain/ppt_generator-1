"""
Target Schema :

slide_data = [
    ["Ethics in Design",
     "Integrating Ethics into Design Processes"],

    ["Introduction",
     "User-Centered Design",
     "Transparency and Honesty",
     "Data Privacy and Security",
     "Accessibility and Inclusion",
     "Social Impact and Sustainability",
     "Ethical AI and Automation",
     "Collaboration and Professional Ethics"],

    ["Introduction",
     "Ensuring responsible decision-making in design.",
     "Moral obligation to prioritize user well-being.",
     "Promoting trust, inclusivity, and positive social impact."],

    ["User-Centered Design",
     "Prioritize needs and experiences of users.",
     "Design with empathy and user feedback.",
     "Respect user privacy and ensure informed consent.",
     "Avoid manipulative practices and prioritize inclusivity."],

    ["Transparency and Honesty",
     "Be transparent about design intentions and limitations.",
     "Disclose risks and biases in the design.",
     "Avoid deceptive practices and false advertising.",
     "Establish trust through clear and accurate communication."],

    ["Data Privacy and Security",
     "Safeguard user data with strong privacy measures.",
     "Collect only necessary data with explicit consent.",
     "Regularly assess and update security measures.",
     "Establish data retention policies and allow user data deletion."],

    ["Accessibility and Inclusion",
     "Design interfaces accessible to users with disabilities.",
     "Provide alternative formats for content.",
     "Consider diverse cultural and cognitive backgrounds.",
     "Test designs with a diverse group of users."],

    ["Social Impact and Sustainability",
     "Consider broader social and environmental implications.",
     "Promote sustainability by reducing waste and energy consumption.",
     "Avoid designs contributing to inequality or harm.",
     "Engage in socially responsible collaborations."],

    ["Ethical AI and Automation",
     "Ensure fairness and accountability in AI algorithms.",
     "Audit and monitor AI systems for bias and discrimination.",
     "Be transparent about AI-driven decision-making processes.",
     "Anticipate and mitigate potential negative impacts."],

    ["Collaboration and Professional Ethics",
     "Foster a collaborative and inclusive work environment.",
     "Respect intellectual property rights and avoid plagiarism.",
     "Uphold professional standards and codes of ethics.",
     "Be open to feedback and continuous learning."],
]
"""

# ADDITIONAL STEP At each step , search for the appropriate content , fetch top 3 results , use RAG on that

# Generate Title and Subtitle given Topic

# Given topic title and subtitle generate table of content for 7 slides

# Iterate over TOC , for each sub topic given the topic title and subtitle , generate 5 points or sentences , each of 100 characters in length

# Format at each step to proper list

import re
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="dolphin2.1-mistral",
             temperature="0.6")

llm_low_temp = Ollama(model="dolphin2.1-mistral",
                      temperature="0")


def extract_items(text):
    pattern = r'<<\s*"([^"]+)"\s*\|\s*"([^"]+)"\s*>>'
    matches = re.findall(pattern, text)
    return [item for match in matches for item in match]


print(extract_items(llm("""
You are a text summarization and formatting specialized model that fetches relevant information

For the topic "Ethics in Business" suggest a presentation title and a presentation subtitle it should be returned in the format :
<< "title" | "subtitle >>

example :
<< "Ethics in Design" | "Integrating Ethics into Design Processes" >>
""")))