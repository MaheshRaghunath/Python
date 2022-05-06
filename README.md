# Python

Run the application stack
Now that we have our docker-compose.yml file, we can start it up!

Make sure no other copies of the app/db are running first (docker ps and docker rm -f <ids>).

Start up the application stack using the docker-compose up command. We’ll add the -d flag to run everything in the background.

# $ docker-compose up -d

stoop and remove

# docker-compose stop && docker-compose rm -f

rebuid the docker Imag

# docker-compose up --build
