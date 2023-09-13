# VSCode Demo

VSCode is a very powerful IDE owned by Microsoft. It has helped me and many of my colleagues to code much more efficiently. It minimizes the need to have many different programs and tabs open while developing code. In this demo I will describe a set of VSCode features that are very useful to any developer, and have been particularly useful to me as a Data Scientist. 

## Glossary

* Prerequisites
* Environment Management
    * Conda
    * Attaching VSCode Directly to Docker Container
* Python
    * Running Python Script
    * Running IPython Notebook
    * Debugging Python Script
    * Debugging IPython Notebook
* Source Control Extension
    * Terminal commands
    * User interface
* SQL
    * Set up SQL DB
    * View DB from VSCode
* Github Copilot
    * Setup instructions
    * Copilot examples
* Tips and Tricks
* References

## Prerequisites

1. Install VSCode
2. Clone the repository
    * https://github.com/tchase56/vscode_demo
3. Install Environment Resources
    * Conda Option
        * Install Conda
    * Docker Option
        * Install Docker or Rancher
4. Install VSCode Extensions using extensions button
    * Python Section 
        * Python
        * HTML Preview
    * For Docker Environment Option
        * Docker
        * Remote-Containers
    * For SQL
        * SQLite 
        * SQLite Viewer
    * For Copilot
        * GitHub Copilot
        * GitHub Copilot Labs

![Screenshot](images/extensions_button.png)

## Environment Management

### Option 1: Conda

#### Initial Setup

1. Open VSCode
2. Open a terminal
    * A terminal can be spawned by dragging from the bottom of the VSCode screen
2. Create Conda Environment
    * `conda create --name vscode_demo python=3.10.12`
3. Activate the environment
    * `conda activate vscode_demo`
4. Install the necessary python libraries
    * `conda install -c anaconda jupyter=1.0.0`
    * `conda install -c anaconda scikit-learn=1.3.0`
    * `conda install -c anaconda sqlalchemy=1.4.39`
    * `conda install -c anaconda numpy=1.25.2`
    * `conda install -c anaconda pandas=2.0.3`
    * `conda install -c anaconda ipykernel=6.25.0`
    * `conda install -c anaconda typing=3.10.0.0`

#### After Setup

1. Activate the environment
    * `conda activate vscode_demo`

### Option 2: Attaching VSCode Directly to Docker Container

#### Attach VSCode to Container Initial Setup

1. Open VSCode
2. Open a terminal
    * A terminal can be spawned by dragging from the bottom of the VSCode screen
3. Build image from Dockerfile
    * `docker image build -t vscode_demo_image .`
4. Build a container from the image
    * `docker run -d -t --name vscode_demo_container vscode_demo_image`
5. Attach VSCode to container
    * click on the docker extension button 
    * open the containers tab
    * right click on vscode_demo_container and select "attach visual studio code"
6. Install the necessary VSCode extensions in the container (same as above)
7. Reconfigure github inside of container
    * git config
        * `git config user.email "*****"`
        * `git config user.name "****** ******"`
    * if necessary set up your ssh-keychains again

#### Attach VSCode to Container After Setup

1. Attach VSCode to container
    * click on the docker extension button 
    * open the containers tab
    * right click on vscode_demo_container and select "attach visual studio code"

## Python

### Running Python Script

1. Open python/python_script.py from the explorer
    * Click on the file explorer button
    * Select VSCODE_DEMO as the home directory of the explorer
    * Open python_script.py

![Screenshot](images/file_explorer_python_script.png)

2. Make sure VSCode is using the correct form of Python
    * Open .py file 
        * ensure the language Python is chosen in the lower right hand corner of the screen
        * Click on the python version button in the lower right hand corner of the screen and ensure "'vscode_demo':conda" is selected

![Screenshot](images/python_version_script.png)

3. Running the script
    * Using the play button 
        * When you open a python script there will be a play button in the upper right hand corner of the screen
            * Press this play button to run the script
            * Note: here you cannot use command line args
    * Terminal Commands
        * A terminal can be spawned by dragging from the bottom of the VSCode screen
            * if there is no terminal put a cursor at the top of the blue ribbon at bottom of VSCode
            * Once the arrow forms click and drag upwards
        * cd into the folder that contains python_script.py
        * Run the terminal command to run the script
            * `python python_script.py <alpha> <l1_ratio>`   
    * Display
        * Plots will not display if a script is ran that contains a plot. 
        * Plots generated in a script must be explicitly saved for later viewing. 

![Screenshot](images/)

![Screenshot](images/)

### Running IPython Notebook

1. Open python/python_notebook.ipynb from the explorer

![Screenshot](images/)

2. Make sure Ipython Notebook is using the correct form of Python (Conda 3.10.12)
    * Click on the python version button in the top right corner of VSCode and select Conda 3.10.12
        * Every notebook has a python environment associated with it

![Screenshot](images/)

3. Running the notebook
    * Running a single cell
        * Click the play button to the left of the cell
        * or click a cell to highlight, then press shift+enter
    * Running all cells
        * Click the "Run All" button at the top of the notebook

![Screenshot](images/)

![Screenshot](images/)

4. Display
    * Print statements and plots will display below the cell being run

![Screenshot](images/)

### Debugging Python Script

1. Debugger settings
    * Click on the debugger extension button on the left of the window
    * Add a break point in your code and this will open some additional "BREAKPOINTS" options at the bottom of the debugger windowt
        * to the left of the numbers in the .py file click and a red circle will appear
    * Make sure "Uncaught Exceptions" and "User Uncaught Exceptions" are checked
    * Then remove the breakpoints you used to bring up the breakpoint options (if you don't want the code to stop there)

![Screenshot](images/)

2. Catching a bug placed in imported function
    * Create bug to track
        * in python_functions.py change np.sqrt to np.sqt
    * Debugging python script
        * Click on the debugger extension on the left side of screen
        * click on the script you want to debug
        * then click on the blue "Run and Debug" button in the extension
        * the debugger opens the problematic file, highlights the section with the issue (in this case an incorrect function name)
3. Variable exploration while debugging
    * After running debugger and while at a breakpoint
    * VARIABLES tab in the debugger extension 
        * Here you can see the variables in the namespace of the breakpoint
        * When debugging you can right click on the variable and open that variable in the "data viewer" (this is very useful for DataFrames)
        * it is also worth noting that more complicated instances such as class instances are viewable in the VARIABLES tab, with the ability to click through the parameters
    * DEBUG CONSOLE
        * Select the DEBUG CONSOLE at the bottom of the screen next to the TERMINAL button 
        * here you have the ability to query the variables in the namespace of this break point
            * Typing "actual" returns the "actual" argument to the "eval_metrics" function at the time of the break point
    * Stop debugger
        * Click the stop button at the top of the screen

![Screenshot](images/)

![Screenshot](images/)

![Screenshot](images/)

![Screenshot](images/)

![Screenshot](images/)

![Screenshot](images/)

### Debugging IPython Notebook

1. Debugger settings
    * follow the instructions for "debugger settings" in the "Debugging Python Script" section
2. Catching a bug placed in imported function
    * Create bug to track
        * in python_functions.py change np.sqrt to np.sqt
    * Debugging IPython Notebook
        * At the problematic cell click the dropdown by the play button
        * Select "Debug Cell"
        * The debugger opens the problematic file, highlights the section with the issue, and gives you the ability to query through the debugger at this break point (in this case an incorrect function name)
3. Vairable exploration while debugging
    * follow the instructions for "Variable exploration while debugging" in the "Debugging Python Script" section

![Screenshot](images/)

## Source Control Extension

### Terminal Commands

1. you can do all of your normal git commands through the terminal at the bottom of the screen
2. stage file
    * git commit file_name
3. commiting changes
    * git commit -m "commit message"
4. push changes to repository
    * git push origin branch_name

![Screenshot](images/)

### User Interface

1. click on the "source control" extension button on the left side of the window

![Screenshot](images/)

2. click on a modified file (highlighted yellow) to see the diffs between the current saved version and the last commit
    * how the changes are displayed
        * click on the file in the "source control" extension
        * The old committed file is on the left, and the saved new version is on the right
        * Deletions are highlighted in red and additions are highlighted in green
    * Tip
        * I find it helpful to double check the diffs before staging to ensure there isn't anything unexpected (from say a cat on your keyboard...)
    * Python Script
    * Ipython Notebook

![Screenshot](images/)

![Screenshot](images/)

3. Stage file
    * click on the "+" button to the right of a file to stage changes

![Screenshot](images/)

4. commiting changes
    * after staging 
    * type a commit message
    * then click on the blue "commit" button

![Screenshot](images/)

5. push changes to repository
    * after commiting the "Sync Changes" button will appear
    * press the "Sync Changes" button to both pull and push commits from the active branch

![Screenshot](images/)

![Screenshot](images/)

## SQL

### Set up SQL DB

1. download sqlite
    * Download the SQLite extension in VSCode
    * command+shift+p search and select "Developer: Reload Window"
    * if another db is selected in the bottom right of VSCode you may need to click that and select SQLite
2. Create a table in the SQLite DB
    * Create the table by selecting the first command in mysql.sql, right click, and select "Run Selected Query"
        * It will prompt you to choose a DB 
            * choose the db from the repo "mydb.db"
        * this creates an empty table named "example_table" in the SQLite DB
    * populate the table by selecting the second command in mysql.sql, right click and select "Run Selected Query"
3. Query the table we created
    * query our table by highlighting the third command in mysql.sql, right clicking, and selecting "Run Selected Query"

![Screenshot](images/)

### View DB from VSCode

1. Download the SQLite Viewer extension in VSCode
    * After setting up our DB and creating the "example_table" table, right click on mydb.db
        * select "open with..." and then select "sqlite viewer" 
        * here we can see the details of the table we created
        * if there were more tables they would all be available here for viewing
2. This is fairly similar to more complex VSCode DB tools such as the Snowflake extension, or the SQLTools extension

![Screenshot](images/)

## Github Copilot

### Setup Instructions

1. Install the GiHub Copilot extension, and connect to your GitHub
2. In your GitHub account sign up for the Copilot trial
    * As of writing the first month is free, then it is $10 a month or $100 per year
3. Configure the data sharing information for GitHub Copilot
    * If you are worried about incorporating public code into your repo I suggest not allowing suggestions matching public code
    * If you are worried about GitHub using your code snippets for training models I suggest you not allow GitHub to use code snippets for product improvement
4. Install the GitHub Copilot Labs Extension

### Copilot Examples

1. Writing code from a comment

![Screenshot](images/)

2. Automatically generate docstrings

![Screenshot](images/)

3. Translating code in GitHub Copilot Labs
    * example translating pandas to sql

![Screenshot](images/)

## Tips and Tricks

1. Hover on a function to reveal the docstring

![Screenshot](images/)

2. Jump to source of function
    * Hold down command and then click a function
        * This will open the source file of that function
3. Jump back to the previous location in the editor
    * if you have jumpted to a function you can quickly jump back
        * you can click go -> back 
        * or you can press "ctr -"

![Screenshot](images/)

4. Type in multiple places at once
    * type on multiple lines (aligned)
        * "option+command+uparrow(or downarrow)"
    * type on multiple lines (not aligned)
        * "option+click"

![Screenshot](images/)

![Screenshot](images/)

5. Open variables in IPython notebook
    * Click on the "Variables" button at the top of the notebook
        * You can see all the variables initialized in the notebook
    * Click on the button to the left of "results_df" to open the Data Viewer

![Screenshot](images/)

![Screenshot](images/)




# References

1. Introduction to MLFlow for MLOps Part 2: Docker Environment
    * https://medium.com/p/53516ce45266
2. Configure SQLite for VSCode
    * https://www.google.com/search?q=sqlite+library+vscode&rlz=1C5GCEM_enUS1067US1068&oq=sqlite+library+vscode&aqs=chrome..69i57j33i160.3585j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:4f8f26c5,vid:JrAiefGNUq8,st:0
3. Setting up SSH Keychains
    * https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account


