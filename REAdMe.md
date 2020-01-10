to start the app-
1. build 
`docker-compose build`

2. run
`docker-compose up -d`

3. initialize db
`docker-compose ps`
- it should show the running containers
- pick the web-container name

`docker-compose exec -it "web-container name" sh`

- now you should the inside the containers

`python initialize_db.py`

- Open postman 
<server_ip>:6542/articles
choose method post -
headers add content/type : application/json 
`{
"title": "sample note esdit 7d",
"create_at": "2017-08-23 00:00",
"create_by": "apcelent",
"description": "sample notes edit",
"priority": 4
}`

- You can add more articles in same format.
- open browsers 
<server_ip>:6542/articles

- All the created articles should be visible to you.

 To run tests
- get inside the container
run
``pytest kbm/tests.py``
