# Summarization in a tick of time!

Summarization is a process of shortening the whole context of a document to a short sentence or sentences. Here we use the natural language process techniques to create a summary of the given data. More information can be found in this blog:

We compare the summarizers performance using the various nlp models for the given data:
1. In Extractive Summarization we use the models like:
  - Bert
  - XL Net
  - GPT2
  - GPT3 - yet to be implemented
  
2. And, in Abstractive Summarization we use models like:
  - Bart
  - T5

follow to below steps to see the code running:
1. Clone the repo:
```
git clone
```
2. Intall the requirements file
```
pip install -r requirements.txt
```
3. Run the file
```
python main.py
```

### Model Parameters:

The file - Summarization.py within folder Summarizer can be tuned for model or parameter change. the parameters can be changed at the following blocks: 

1. In Xlnet and GPT2
  - transformer_type
  - transformer_model_key
2. In Bart and T5
   - model
   - pipeline (more information on this can be found in this blog: )
   
   


