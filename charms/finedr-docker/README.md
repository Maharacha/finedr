# Deploy Finedr django backend docker with juju charm

In this direcotry, run:  
`charm build .`  
Tar the content of finedr repo as e.g. `finedr.tar.gz`, go to finedr directory and run:  
`tar czf /tmp/finedr.tar.gz .`  
Go to to the directry where the build was generated and run:  
`juju deploy . --resource finedr=/tmp/finedr.tar.gz`

Useful commands:  
`juju status`  
`juju debug-log`
