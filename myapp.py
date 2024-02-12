# Sources
# https://github.com/llmware-ai/llmware/blob/main/examples/SLIM-Agents/agent-multistep-analysis.py
# https://www.youtube.com/watch?v=0MOMBJjytkQ by AI Anytime

import streamlit as st
from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def perform_sum(text):
    #nli_model = ModelCatalog().load_model("slim-nli-tool")
    prompter = Prompt().load_model("llmware/bling-tiny-llama-v0")
    instruction = "What is a brief summary?"
    response_sum = prompter.prompt_main(instruction, context=text)
    return response_sum

def tags(text):
    tags_model = ModelCatalog().load_model("slim-tags-tool")
    response_tags = tags_model.function_call(text, get_logits=False)
    return response_tags

def topics(text):
    topics_model = ModelCatalog().load_model("slim-topics-tool")
    response_topics = topics_model.function_call(text, get_logits=False)
    return response_topics

def intent(text):
    intent_model = ModelCatalog().load_model("slim-intent-tool")
    response_intent = intent_model.function_call(text, get_logits=False)
    return response_intent

def category(text):
    category_model = ModelCatalog().load_model("slim-category-tool")
    response_category = category_model.function_call(text, get_logits=False)
    return response_category

def ner(text):
    ner_model = ModelCatalog().load_model("slim-ner-tool")
    response_ner = ner_model.function_call(text, get_logits=False)
    return response_ner


# Streamlit app layout
st.image('logo.png',use_column_width="auto")
st.title("Intensive Enterprise NLP Tasks")
st.markdown("### using only CPU resources")

# Text input
text = st.text_area("Enter text here:")

# Analysis tools selection
analysis_tools = st.multiselect(
    "Select the analysis tools to use:",
    ["Generate Tags", "Identify Topics",
     "Perform Intent", "Get Category",
     "Perform NER", "Perform Summarization"],
    ["Generate Tags"]  # Default selection
)

# Run the selected TASKS/Agents and display results in plain json format
if st.button("Analyze"):
    results = {}
    
    if "Generate Tags" in analysis_tools:
        results["Generate Tags"] = tags(text)
    if "Identify Topics" in analysis_tools:
        results["Identify Topics"] = topics(text)
    if "Perform Intent" in analysis_tools:
        results["Perform Intent"] = intent(text)
    if "Get Category" in analysis_tools:
        results["Get Category"] = category(text)
    if "Perform NER" in analysis_tools:
        results["Perform NER"] = ner(text)
    if "Perform Summarization" in analysis_tools:
        results["Perform Summarization"] = perform_sum(text)
    
    for tool, response in results.items():
        st.subheader(tool)
        st.json(response)