# finedr

## Run container
`docker-compose up -d`  
Now, django should be accessible on `http://localhost:8080`  
Admin page is: `http://localhost:8080/admin`

## Install as a snap
Run `snapcraft` to build finedr snap package.  
It will generate a file e.g. `finedr_0.1_amd64.snap`  
Install the snap:  
`sudo snap install finedr_0.1_amd64.snap --devmode --dangerous`  
It will be automatically started as a daemon. Check with:  
`snap logs finedr.django-backend`
