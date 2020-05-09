DATAMODEL

The database contains only one model: user (for testing purposes of the flask program). 
The user contains a few attributes:
•	Id of user
•	Name of the user
•	List of id’s of friends of the user.

The data is hard-coded into the python code.
The data is a simulation of a social network, where each user has an id, a name 
and, for example, a list of hist friends, represented by the corresponding id.
This way we can send all the users at once, or send each user individually by their id

What has been done:
• created a flask rest api server, which returns some stubbed database
• created docker image of the program
• uploaded the image to docker
• made a screencast of the uploading process of the image