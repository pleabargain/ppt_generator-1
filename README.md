
#  original idea inspired by 
https://github.com/Govind-S-B/ppt_generator

# better version
https://github.com/pleabargain/ppt_generator-1


# PPT Generator
A local LLM assisted powerpoint generation tool 

## Why  
Idea generation with Ollama running locally. This will be useful for generating ideas for presentations. It will pull the available local models and let you select one.

# What
Don't expect a lot of features. 


I did add a language option. It's not perfect but it's a start.

It's a simple tool to generate (generic) powerpoint content. It doesn't support images and there is no styling to speak of. It's just a simple tool to generate ppt content. There all kinds of things that can be added to it.

* add image generation
* add styling
* add speaker notes
* add slide numbers
* add slide layouts
* reference color palettes



## Running Locally
install [ollama](https://ollama.ai/download)
and have it up and running with command `ollama serve` ( applicable to some systems only )  



```
ollama pull llama3.2
```


clone the repo and move into the directory

```
git clone https://github.com/pleabargain/ppt_generator-1
```


```
cd ppt_generator
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


run the streamlit app

```
python -m streamlit run main.py
```

