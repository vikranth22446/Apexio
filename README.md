# Apexio
Running the code.
```sh
make up
```

The server will start at `http://localhost:80/`

## Development Environment
The code is locally deployed via docker-compose.yaml file. 
Type `make` to see the list of commands and their descriptions.
To view the graphql server go to `http://localhost:80/graphql`

### Sample Data
Load sample data to the local database via using the following command:
```sh
make load_demo_data
```

### Debugging and Adding libraries
Many of the make commands exists as shortcuts, but can be manually run from inside these shells.

Access the shell environments of backend. This is useful when running commands and for installing python dependencies.
```
make backend_shell
```
The frontend is currently run locally. 
### Running background jobs
We use celery to run background jobs
```
make run_celery
```
### Local Issues with migrations
```
make clean_db_cache
```

## Deployment
We are currently deploying via bitbucket ci pipelines with information found in
bitbucket-pipelines.yaml file. Every time a change is pushed to a branch we check it and then
deploy it to the servers via terraform. Check out the deploy/ folder to learn more.

## Built With
Backend:
* [Flask](http://flask.pocoo.org/) - The web framework used
* [React](https://reactjs.org/) - Frontend
* [GraphQL](https://graphql.org/) - Frontend Query Language
