### Instructions to run Github Search app:

- Create python3 virtual environment. 
- Activate virtual env in terminal and change directory to project root folder.
- Run "pip install -r requirements.txt" to install flask and other requirements for this project.
- For Github enterprise search, set GE_HOSTNAME environment variable.
- Generate Github Access Token and set GE_ACCESS_TOKEN environment variable.
- To run Github search:
    - Go to search.py file and replace the value of SEARCH_KEYWORD variable with the one you want.
    - In you terminal enter these commands:
        - python
        - from search import search_github
        - search_github()