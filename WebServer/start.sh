sudo mkdir /var/www/FLASKAPPS
sudo cp -r $PWD/* /var/www/FLASKAPPS

sudo chown -R www-data:www-data /var/www/FLASKAPPS
sudo chmod -R 755 /var/www/FLASKAPPS

sudo systemctl restart apache2
