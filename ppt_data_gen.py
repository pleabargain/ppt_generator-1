import re
from langchain_ollama import OllamaLLM


def extract_items(input_string):
    # Find the text inside the << >>
    content = re.search(r'<<(.+?)>>', input_string)

    if content:
        content = content.group(1)
    else:
        return []

    # Split the content by the | separator and remove whitespace
    items = [item.strip() for item in content.split('|')]

    # Remove the quotes from each item
    items = [re.sub(r'^"|"$', '', item) for item in items]

    return items


def slide_data_gen(topic, num_slides, model, language="English"):
    llm = OllamaLLM(model=model, temperature="0.4")

    slide_data = []

    point_count = 5

    # Generate title and subtitle
    title_subtitle = extract_items(llm.invoke(f"""
    You are a text summarization and formatting specialized model that fetches relevant information
    For the topic "{topic}" suggest a presentation title and a presentation subtitle in {language}. It should be returned in the format :
    << "title" | "subtitle" >>
    """))

    # Check if title and subtitle were extracted correctly
    if len(title_subtitle) < 2:
        raise ValueError("Failed to extract title and subtitle from the model's response.")

    slide_data.append(title_subtitle)

    # Generate table of contents
    toc = extract_items(llm.invoke(f"""
    You are a text summarization and formatting specialized model that fetches relevant information
    For the presentation titled "{slide_data[0][0]}" and with subtitle "{slide_data[0][1]}" for the topic "{topic}"
    Write a table of contents containing the title of each slide for a {num_slides} slide presentation in {language}.
    It should be of the format :
    << "slide1" | "slide2" | "slide3" | ... | >>
    """))

    slide_data.append(toc)

    for subtopic in slide_data[1]:
        data_to_clean = llm.invoke(f"""
        You are a content generation specialized model that fetches relevant information and presents it in clear concise manner
        For the presentation titled "{slide_data[0][0]}" and with subtitle "{slide_data[0][1]}" for the topic "{topic}"
        Write the contents for a slide with the subtopic {subtopic} in {language}.
        Write {point_count} points. Each point 10 words maximum.
        Make the points short, concise and to the point.
        """)

        cleaned_data = llm.invoke(f"""
        You are a text summarization and formatting specialized model that fetches relevant information and formats it into user specified formats
        Given below is a text draft for a presentation slide containing {point_count} points, extract the {point_count} sentences and format it as:
        << "point1" | "point2" | "point3" | ... | >>
        """)
        
        slide_data.append([subtopic] + extract_items(cleaned_data))

    return slide_data
