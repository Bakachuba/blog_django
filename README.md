## Запуск через Docker
docker-compose up --build

## Применение миграций 
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


## URLS
API





GET /api/creators/: Получить список создателей (юзеры).
POST /api/creators/: Создать нового создателя.

PUT /api/creators/: Обновить создателя.

PATCH /api/creators/: Частично обновить создателя.

DELETE /api/creators/: Удалить создателя.




GET /api/posts/: Получить список постов.

POST /api/posts/: Создать новый пост.

PUT /api/posts/: Обновить пост.

PATCH /api/posts/: Частично обновить пост.

DELETE /api/posts/: Удалить пост.



GET 

/api/comments/: Список комментариев.

POST 

/api/comments/: Создать новый комментарий.

PUT 

/api/comments/: Обновить комментарий.

PATCH 

/api/comments/: Обновить часть комментария.

DELETE 

/api/comments/: Удалить комментарий.



GET 

/api/categories/: Список категорий.

POST

/api/categories/: Создать новую категорию.

PUT 

/api/categories/: Полностью обновить категорию.

PATCH 

/api/categories/: Обновить часть категории.

DELETE 

/api/categories/: Удалить категорию.

POST

/api/post-view-counts/: Просмотр поста.


WebSocket 

ws://:8000/ws/notifications/: Получать уведомления о создателях.

## Models

● Один к одному (OneToOne) 
Post <-> PostViewCount

● Один ко многим (ForeignKey) 
Comment -> Post

● Многие ко многим (ManyToMany)
Post <-> Category

● Многие к одному (обратная связь)
User <- Post, Comment

## Models Visualisation Scheme 

![img_3.png](img_3.png)