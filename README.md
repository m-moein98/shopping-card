# Shopping Card Project
this application was built to handle problems with saving and managing a shopping card using an API
the application is build in TDD method so it's all bug free
the dockerfile, postman documentation and nginx conf to run the project are available in the project root
# Technical Choices
the reason this app is build on django was the fact that it is fast to build the MVP and it's as scalable as it gets.
sqlite is chosen as database because it is just a demo of a MVP so we dont expect any large amount of data to be added to project.
in the feuture it is planned to switch to postgres as a replacement for sqlite to scale the project.

# Trade-off
this project was built without any relation to user system due to customer request which was not implementing that in the project.
the smtp email server is not configured by now but it's ready to use after configurations.

# Cloud services
the logging and backup system are provided and managed in cloud side so you cannot see anything related to logging and backup system in the codes here.

# Host
this project is hosted in this address temporarily **[click here](https://card.moein98.ir/)**
### the servers are in debug mode on purpose

# About Me
I'm available at this email address: moein1475963.mmz@gmail.com
