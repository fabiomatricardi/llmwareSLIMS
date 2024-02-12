<img src="https://github.com/fabiomatricardi/llmwareSLIMS/raw/main/logo.png" width=900>

# Go Open, go Lean: LLMWare now can boost your AI-powered enterprise.
### Budget-friendly Efficiency: LLMWare makes AI Back-Office dreams a Reality with a herd of new SLIMs models.
Repo of the code from the Medium article

This repo will work only with python version < 3.12

Create a new directory and a virtual environment

```
mkdir llmware
cd llmware
python -m venv venv
```

Activate the venv and install the following packages

```
source venv/bin/activate  #activate the venv on Mac/Linux
venv\Scripts\activate  #activate the venv on Windows
pip install llmware
pip install streamlit
```


Download then 2 files in the project directory:
- myapp.py
- logo.png

In the terminal, the the venv active run the following command
```
streamlit run myapp.py
```


During the first execution the application will download the models on your local machine <br>
in the cache HuggingFace directory, something like this:

```
C:\Users\User\.cache\huggingface\hub
```

<img src="https://github.com/fabiomatricardi/llmwareSLIMS/raw/main/cacheDIR.png" width=700>



