# Django-React-Blog
This is a "Mircro Blogging Platform" which gives all general features a blog should have.

The backend is completely build on Django using Django Rest Framework, while the frontend is completed using ReactJS.
### Features
* Login/Registration
* Minimal Design
* Create/Edit/Delete Your Posts
* View/Comment/VOTE Other Posts
* User Profile


	* Create/View/Edit/Delete A User
	* View/Edit/Create Comments To A Specific Post
	

## Backend Setup
1. Clone this repository: `git clone https://github.com/Sagorhowlader/Django-React-Blog.git`.
2. Change the current directory to `backend` folder: `cd ./Django-React-Blog/backend_blog/`.
3. Create a virutal environment and install all backend dependencies with pipenv: `pipenv install`.
4. Start the virtual environment: `pipenv shell`.
5. Change the working directory to `backend_blog` which contains the `manage.py` file: `cd ./blog_backend`.
6. Run `python manage.py makemigrations`.
7. Run `python manage.py migrate`.
8. Create a superuser: `python manage.py createsuperuser`
9. Run the server: `python manage.py runserver`.

## Frontend Setup
1. Navigate the current working directory to `blog_frontend`: `cd ./Django-React-Blog/frontend/`.
2.  Install the all frontend dependencies using npm: `npm install`.
3.  Run the server: `npm start`.

## API DOC 

Base Url: `http://127.0.0.1:8000/`

# API: GET CSRFToken 

#End-point: `accounts/csrf_cookie`
Response:  
{
    "success": "CSRF cookie set"
}


# API: Registration 
End-point: `accounts/register`
Method: POST 

Header: 
{
Content-Type: application/json 
X-CSRFToken : csrftoken 
}
Body:
{
    "username":"test",
    "password":"password",
    "re_password":"password"
}

Response body : 
{
    "success": "User created successfully"
}

##API: Login  

End-Point: `/accounts/login`
Method: POST 
Header: 
{
Content-Type: application/json 
X-CSRFToken : csrftoken 
}
Body:
{
    "username":"admin",
    "password":"password"
}

Response body: 
{
    "success": "User authenticated"
}

##API: Check Authentication  
End- Point: /accounts/authenticated
Method: GET  
Response body: 
{
    "isAuthenticated": "success"
}


##API: Deleted Account    
End-Point: `/accounts/delete`
Method: GET  
	
Response body: 
{
    "status": true,
    "massage": "Post created Successfully"
}

##API: Create Post   
End-Point : `/api/create-post`
Method: POST 
Header: 
{
Content-Type: application/json 
X-CSRFToken : csrftoken 
}
Body:
{
    "title": "Django Reacts App",
    "content”: “Create First time"
}

Response body: 
{
    "status": true,
    "massage": "Post created Successfully"
}

##API: View all Post    
End- Point: `/post/all-post-view`
Method: GET 

Response body: 
{
    {
    "id": 1,
    "body": "good",
    "updated": "2021-07-10T17:14:25.779983Z",
    "created": "2021-07-10T17:14:25.779983Z",
    "user": 2,
    "post": 1
},
{
    "id": 2,
    "body": "good",
    "updated": "2021-07-10T17:14:25.779983Z",
    "created": "2021-07-10T17:14:25.779983Z",
    "user": 2,
    "post": 1
}


}



##API: Create Comment      
End-Point: `/api/create-post-comment`

Method: POST  
Header: 
{
Content-Type: application/json 
X-CSRFToken : csrftoken 
}
Request body: 
{
    "post_id":1,
    "body":"good"

}


Response body: 
{
    "id": 2,
    "body": "good",
    "updated": "2021-07-10T17:14:25.779983Z",
    "created": "2021-07-10T17:14:25.779983Z",
    "user": 2,
    "post": 1
}

##API: Create Vote      
End- Point: `/api/create-post-comment`
Method: POST  
Header: 
{
Content-Type: application/json 
X-CSRFToken : csrftoken 
}
Request body: 
{
    "post_id":1,
}

Response body: 
{
    "value": "downvote",
    "likes": 1
}

