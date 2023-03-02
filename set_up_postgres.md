# Install postgres

https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart

sudo apt install postgresql postgresql-contrib


## Start service:

sudo systemctl start postgresql.service

## Switch to postgres user

sudo -i -u postgres

Or open postgres directly:

sudo -u postgres psql

## Open postgres command prompt

psql

## Exit postgress 

\q

## Switch back to main user

exit
