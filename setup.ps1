#!ps1

docker build -t beproject .
docker run -p 5000:5000 --name beproject beproject