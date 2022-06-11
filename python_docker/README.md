To run the Docker you have to follow these steps:

docker build . -t webapp_sp_netflix
docker run -p 80:3000 webapp_sp_netflix

Then open your browers and you should be able to type "localhost" to see the result.