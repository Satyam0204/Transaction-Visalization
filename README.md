# Transaction-Visalization

## Run the docker containers

### Set-up enviornment variables

```bash
    cp Backend/.example.env Backend/.env
```

```bash
    docker-compose up --build -d
```

## Removing the docker conatainers

```bash
    docker-compose down
```


## Api Endpoints:
 -  /get-arbritrum-transactions - get arbitrum average transactions per block 
 - /ethereum-data/{date} - get first and last ethereum block numbers of specified date
   
