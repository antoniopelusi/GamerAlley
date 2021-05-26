# gamerAlley :video_game:
A videogames-based social network

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
    
### Installation
- Clone this repository with git clone `https://github.com/antoniopelusi/GamerAlley.git`
- Move to the `/src/GamerAlley` directory inside the project
- Create the virtual environment and install all the libraries with `pipenv install django pillow django-allauth`
- Set up the database with `python manage.py migrate` (_there is already a database with some profile, posts, comments and relationships to test the website_)
- Run the server with `python manage.py runserver`

### Additional info
- Back-end framework: `Django`
- Front-end framework: `Semantic UI`
- Used libraries: `django-allauth`, `pillow`
