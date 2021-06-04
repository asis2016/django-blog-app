
# A Basic Django Blog App

This is a simple demonstration of Blog (app) made in Django.



## Tech Stack
Python, Django, Gunicorn, Heroku


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
