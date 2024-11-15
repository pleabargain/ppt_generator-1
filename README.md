
#  original idea inspired by 
https://github.com/Govind-S-B/ppt_generator



# PPT Generator
A local LLM assisted ppt generation tool 

## Why  
Idea generation with Ollama running locally. This will be useful for generating ideas for presentations. And also for generating ppt content. It will pull the available local models and let you select one.


## Running Locally
install [ollama](https://ollama.ai/download)
and have it up and running with command `ollama serve` ( applicable to some systems only )  



```
ollama pull llama3.2
```



install the required python dependencies
```
pip install -r requirements.txt
```

maybe these too

```
pip install -U langchain-community
pip install -U langchain-ollama
```




clone the repo and move into the directory
```
git clone 
cd ppt_generator
```
install the required python dependencies
```
pip install -r requirements.txt
```
run the streamlit app

```
python -m streamlit run main.py
```
