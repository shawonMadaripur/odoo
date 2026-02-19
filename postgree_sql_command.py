1 : opening the postgresql?
=> sudo -u postgres psql

2 : check how many user have ?
=> \du

3 : How to reset the password ?
=> Alter Role user_name with Password ‘password’

4 : How to get out from postgres ?
=> \q

5 : to show the database List ?
=> \l

6 : How to run the project ?
=> python3 odoo-bin -c odoo.conf
=> ./odoo-bin -c odoo.conf

7 : If i want to run specific database ?
=> ./odoo-bin -c odoo.conf -d database_name

8 : কোনো ফাইলের ভিতরের content (লেখা) terminal এ দেখার জন্য।
=> cat /opt/odoo19/odoo.conf

# : How to delete database ?
=> DROP DATABASE database_name;

