#!/bin/bash

cd /etc/apache2/sites-available
touch $1.conf

cat <<EOT >> $1.conf
<VirtualHost *:80>
ServerName ${1}.recraftrelic.com
ServerAlias www.${1}.recraftrelic.com
ProxyPass         / http://localhost:${2}/
ProxyPassReverse  /  http://localhost:${2}/
</VirtualHost>
EOT

a2ensite $1.conf
sudo service apache2 restart

sudo certbot --apache -d $1.recraftrelic.com -d www.$1.recraftrelic.com