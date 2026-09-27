# python Quiz Game
A simple quiz game built with python 
## Table of contents



- [Features](#features)
- [Project Structure](#project-structure)
- [Requirments](#requirments)
- [Installation](#installation)
- [Envoirment Setup](#envoirment-setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licence](#licence)
- [Author](#author)

## Features
- Quiz system
  - Asks the player multiple question
  - Cheks the answers automaticlly
  - Calculates the final score
- Result storage
  - Saves quiz result to a file `results.txt`
- Admin mode
  - akse for the admin password
  - checks if the password is correct
  - keeps the  private information password outside the main python file 
  - loads the password from `.env`
 

## Project Structure
```text
python.quiz_game/

│   main.py
|   question.py
|   .env_ezample
│   .gitignore
│   requirments.txt
│   
│   README.md
```
### File Description
- `main.py` - main file used to run quiz game
- `question.py` - stores questions and answers
- `requirments.txt` - lists the python pachages needed for the project
- `.env_ezample` - show the envoirment variables needed by the project
- `.gitignore` - tells git which files and folders shold not be tracked
- `README.md` - contains the project ducumantation
## Requirments
before running the project, make sure you have:
- `python 3`
- `python-dotenv`
  

## Installation
1. open a terminal in the project folder.
2. check that python is installed: 
```bash
python --version
```

3. install the python packages:
```bash
pip install -r requirments.txt
```

## Envoirment Setup
1. create a `.env` file from `.env.example`
```bash
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with your own password
```text
QUIZ_ADMIN_PASSWORD = your_password_here
```
4. save the file
> Do not commit your `.env` file because it may contain private information

## Usage
1. open a terminal in the project folder
2. run the quiz game
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you choose `yes`, enter the password from your `.env` file
5. enter your name
6. answer the questions
7. see your final score and massage
8. your result is saved in `result.txt`

## Example Output
```text
do u want to open admin mode?   yes/no:  no

whats your name? alex

welcome

what language are we usingc++

wrong

what command starts a  git? git init

correct

what command starts a  git status? git log 

--oneline

wrong

your score is:  1 out of  3
```
## Roadmap
- [x] add multiple quiz questions
- [x] calculate the final score
- [x] save resultes to a file
- [x] add admin mode
- [ ] add more quiz questions
- [ ] add difficultly levels
- [ ] add timer
## Contributing

## Licence

## Author
create by [roham mirzaei](https://github.com/roham-m)