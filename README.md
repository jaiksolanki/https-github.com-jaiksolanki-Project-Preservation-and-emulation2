# BE PROJECT

Cloud Kubernetes And Docker by jai solanki .

## Setup Command

**For Linux**

```./setup.sh```

**For Windows**

```.\setup.ps1```

**REDIS SERVER**
```
$ wget http://download.redis.io/releases/redis-4.0.9.tar.gz
$ tar xzf redis-4.0.9.tar.gz
$ cd redis-4.0.9
$ make
$ redis-server
```

**Celery**
```
$ cd beproject/app/
$ celery worker -A app.celery --loglevel=info
```
