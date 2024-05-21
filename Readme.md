## IEC (Information Extraction for Code):
Model which soly focus on understanding and extracting necessary information from writen code. This is a text2text information extraction model.
### Inputs IEC:
- Pre-Prompt: Defining the fact that the model needs to create a kind of summary which writes about the functions/objects used/created. 
- Inputs: Soly the code of the project (assuming its written in one file). If the project is moduled into multiple files connected through imports or similar fashion, inputting the whole project folder should be possible. 
  
## IET (Information Extraction for Text):
Similarly to IEC, this is a text2text model. Its purpose is to focus on plain text of the task in hand. 
### Inputs IET:
- Pre-Prompt: Defining that the model needs extract information from the given text as input. The text should consist of the problems/tasks considering the project.
- Inputs: Text/Problems/Tasks

## GEN (Report Generator):
Text2Text with inputs of code, text, and the outputs of the previous two models. The purpose of this model is to generate an ImRAD Tex/Markdown report using the inputs. 
### Inputs GEN:
- Pre-Prompt: Author, Title and pre-prompt defining the task of writing a Tex/Markdown report, and the core structure of the latex code.
- Inputs: Code, Text/Problems/Tasks, IEC output, IET output, LaTex structure
