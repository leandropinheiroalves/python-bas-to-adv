"""Aula 06: Linux - MariaDB Server + MySQL Workbench

[comandos]
sudo apt-get update
sudo apt-get install mariadb-server

sudo mysql -u root

USE mysql;
UPDATE user SET plugin='' WHERE User='root';
FLUSH PRIVILEGES;
exit

sudo apt-get install mysql-workbench

"""
