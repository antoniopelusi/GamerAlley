# gamerAlley :video_game:
A videogames-based social network


![](https://img.shields.io/badge/HTML-red) ![](https://img.shields.io/badge/Python-blue) ![](https://img.shields.io/badge/Javascript-yellow) ![](https://img.shields.io/badge/CSS-purple)

![](https://img.shields.io/badge/Open_Source-GPL--3.0-darkgreen)

---
#### Full documentation about functionality and screenshots available on the file `Gameralley.pdf` in this repository

---
### Features:
- **Profile**
    - Create account
    - Login
    - Logout
    - Update info
    

- **Post**
    - Create post
    - Edit post
    - Delete post
    - Upvote
    - Add image
    - Add genre tag
    - Write comments
    

- **Genre tags**
    - Search for a videogames genre or click on the tag in a post
    

- **Relationship**
    - Send friend request
    - Accept friend request
    - Remove friend

---
### Additional info
- Back-end framework: `Django`
- Front-end framework: `Semantic UI`
- Used libraries: `django-allauth`, `pillow`

---
### Installation
- Clone this repository with `git clone https://github.com/antoniopelusi/GamerAlley.git`
- Move to the `GamerAlley/GamerAlley` directory inside the project
- Create the virtual environment and install all the libraries with `pipenv install django pillow django-allauth`
- To activate this project's virtualenv run `pipenv shell`
- Set up the database with `python manage.py makemigrations` and `python manage.py migrate` (_there is already a database with some profile, posts, comments and relationships to test the website_)
- Run the server with `python manage.py runserver`

---
### Login in the website (_Preloaded accounts on the database, only for testing purposes_):
_email_ | _password_ to login in GamerAlley

**Admin account:** (_can enter in the Django_ `admin/` _page_)
- antoniopelusi@email.com | **passwordantonio**


**User accounts:** (_only for GamerAlley login_)
- marcobianchi@email.com | **passwordmarco**
- annabianchi@email.com | **passwordanna**
- valentinorossi@email.com | **passwordvale**
- giorgiobruni@email.com | **passwordgiorgio**
- michelagialli@email.com | **passwordmichela**
