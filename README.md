# User Management API

This project creates a user management API using Flask. The API allows you to create, update, delete, and list users.

## Getting Started

These steps explain what you need to run this project on your local machine.

## Usage
You can create, update, delete, and list users using the API.

- Create User: POST /create-user
- Body: User data in JSON format (e.g., {"id": 1, "username": "example"})
- Get User Information: GET /get-user/<user_id>
- Path Param: user_id - The user's ID
- Update User: PUT /update-user/<user_id>
- Path Param: user_id - The user's ID
- Body: User data to be updated in JSON format
- Delete User: DELETE /delete-user/<user_id>
- Path Param: user_id - The user's ID
- List Users: GET /list-users

### Requirements

To run this project, you'll need the following software:

- Python (3.9 or above) (If you just run the source code this will enough)
- Docker (If you run it on a container you should pull the image file on dockerhub)
- The image link: https://hub.docker.com/repository/docker/yusufbilalusta/user-manager/general

### Installation

1. Clone the repository:

```bash
git clone https://github.com/username/project-name.git 
#To run locally:
python app.py
#To run using Docker:
docker build -t user-management-api .
docker run -p 5000:5000 user-management-api



