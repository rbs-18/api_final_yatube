# api_yatube
## DESCRIPTION
API service for social network Yatube. Users can published their posts, comment on posts, subscribe to other users.

## ENDPOINTS

 ### JWT TOKEN
 

 - #### GETTING TOKEN

 `/api/v1/jwt/create/` `POST`
 
*Request sample*
```
{
    "username": "string", (required field)
    "password": "string"  (required field)
}
```
*Responses*

200, 400, 401

 - #### REFRESHING TOKEN

`api/v1/jwt/refresh/` `POST`

*Request sample*
```
{
    "refresh": "string" (required field)
}
```
*Responses*

200, 400, 401

 - #### CHECKING TOKEN

`api/v1/jwt/verify/` `POST`

*Request sample*
```
{
    "token": "string" (required field)
}
```
*Responses*

200, 400, 401
### POSTS
 - #### GETTING LIST OF POSTS

 `api/v1/posts/` `GET`
 
 *Query parameters*
 
 offset - page number for showing after
 limit - amount of posts
 
*Responses*

200
- #### CREATING NEW POST

 `api/v1/posts/` `POST` (only for authorized users)

*Request sample*
```
{
    "text": "string", (required field)
    "image": "string",
    "group": 0 (id)
}
```
*Responses*

200, 400, 401

- #### GETTING, PATCHING, PUTTING, DELETING POST

 `api/v1/posts/{post_id}/` `GET` `PUT` `PATCH` `DELETE` (patching, putting, deleting only for author of post)

*Responses*

200, 404 - for GET
200, 400, 401, 403, 404 - for PUT
200, 400, 401, 403, 404 - for PATCH
204, 401, 403, 404 - for DELETE
### GROUPS

- #### GETTING GROUPS

 `api/v1/groups/` `GET`
 
*Responses*

200

- #### GETTING CERTAIN GROUP

 `api/v1/groups/{group_id}/` `GET`
 
*Responses*

200, 404

### COMMENTS

- #### GETTING ALL COMMENTS FOR POST

 `api/v1/posts/{post_id}/comments/` `GET`
 
*Responses*

200, 404
- #### CREATING NEW COMMENT

 `api/v1/posts/{post_id}/comments/` `POST` (only for authorized users)

*Request sample*
```
{
    "text": "string" (required field)
}
```
*Responses*

201, 400, 401, 404

- #### GETTING, PATCHING, PUTTING, DELETING POST

 `api/v1/posts/{post_id}/` `GET` `PUT` `PATCH` `DELETE` (patching, putting, deleting only for author of comment)

*Responses*

200, 404 - for GET
200, 400, 401, 403, 404 - for PUT
200, 400, 401, 403, 404 - for PATCH
204, 401, 403, 404 - for DELETE

 ### FOLLOWS
 - #### GETTING ALL FOLLOWS OF USER

 `api/v1/follow/` `GET` (only for authorized users)

*Query parameters fo getting*
 
 search - user search possible

*Responses*

200, 401

 - #### SUBSCRIBING TO USER

 `api/v1/follow/` `POST` (only for authorized users)
 
*Request sample*
```
{
    "following": "string" (required field)
}
```
*Responses*

201, 400, 401


## TECHNOLOGY

- Python 3.8
- Django 2.2
- Django Rest Framework 3.12

## HOW TO START PROJECT
Clone repository and going:
```
git clone ...
cd api_yatube/
```
Create and activate virtual environment:
```
python -m venv venv
source venv/Script/activate
python -m pip install --upgrade pip
```
Install dependencies from file requirements.txt:
```
pip install -r requirements.txt
```
Make migrations:
```
python manage.py migrate
```
Run project:
```
python manage.py runserver
```
# AUTHORS
*Kozhevnikov Aleksei*
