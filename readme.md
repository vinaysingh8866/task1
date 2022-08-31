
# Stock Trading Backend

Stock Trading Backend made with Python Flask 


## API Reference

#### Authentication

```http
  POST /api/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your email  |
| `password` | `string` | **Required**. Your password  |


```http
  POST /api/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Your email  |
| `password` | `string` | **Required**. Your password  |
| `uname` | `string` | **Required**. Your user name  |

Log Out
```http
  POST /api/logout
```


Test Auth Token
```http
  POST /api/token_test
```

pass bearer token for testing token


Get new Auth token
```http
  POST /api/new_token
```
#### Tweets
Get all tweets
```http
  GET /api/all_tweets
```


Add new tweet 
```http
  GET /api/add_tweet
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. tweet title |
| `content` | `string` | **Required**. tweet content  |


Delete tweet 
```http
  GET /api/delete_tweet/<tid>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `tid` | `string` | **Required**. tweet id |

Get User tweets
```http
  GET /api/user_tweets
```
Delete tweet 
```http
  GET /api/update_tweet/<tid>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `tid` | `string` | **Required**. tweet id |
| `content` | `string` | **Required**. new tweet content |

## Installation

Install requirements

```bash
  pip3 install -r requirements.txt
```
    
## Running Tests

To run tests, run the following command

```bash
  python3 test.py
```


## Deployment

To deploy this project run

```bash
  npm run deploy
```


## Run Locally

Start the server

```bash
  python3 app.py
```

