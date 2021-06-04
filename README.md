
# A Basic Django Blog App

This is a simple demonstration of Blog (app) made in Django framework.



## Tech Stack
Docker 20.10.6, Python 3.8, Django 3.2.3, Whitenoise, Gunicorn, Heroku


## Demo

[https://basic-blog-app-amaharjan.herokuapp.com/](https://basic-blog-app-amaharjan.herokuapp.com/)


## Environment Variables

To run this project, you will need to add the following environment variables:

`SECRET_KEY` `django-insecure-jhrq9t==0!ysg^6*ut@ort)!@wohm)g^k(xn@515$$=h39(6b(e`

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/asis2016/django-blog-app.git
```

Go to the project directory

```bash
  cd django-blog-app
```

Start the project

```bash
  docker build .
```

```bash
  docker-compose up -d
```

## Running Tests

To run tests, run the following command

```bash
  docker-compose exec web python manage.py test
```

## Running the project locally

Goto [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Running Django Administration

Goto [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- username: root
- password: root

  
## Demo with Screenshots

[index](https://basic-blog-app-amaharjan.herokuapp.com/)

![index](/screenshots/a.png)

### Read a post
[/post/{id}/](https://basic-blog-app-amaharjan.herokuapp.com/post/1/)

![read](/screenshots/b.png)

### Edit the post
[/post/{id}/edit/](https://basic-blog-app-amaharjan.herokuapp.com/post/1/edit/)

![edit](/screenshots/c.png)

### Delete the post
[/post/{id}/delete/](https://basic-blog-app-amaharjan.herokuapp.com/post/1/delete/)

![delete](/screenshots/d.png)

### Create a post
[/post/new/](https://basic-blog-app-amaharjan.herokuapp.com/post/new/)

![create](/screenshots/e.png)



  
## Roadmap

- This project doesn't include authentication and authorization. These features can be found on [django-newspaper-app](https://github.com/asis2016/django-newspaper-app).

  
## Feedback

If you have any feedback, please reach out to us at hello@amaharjan.com
