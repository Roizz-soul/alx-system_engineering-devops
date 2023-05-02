# installing nginx and adding to header using puppet
exec { 'Nginx install with custom header response':
command => 'sudo apt-get update -y && sudo apt-get install nginx -y && 
            echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html && 
			header="\\\t\tadd_header X-Served-By $HOSTNAME;" && 
			sudo sed -i "/^\tlocation.*/a $header" /etc/nginx/sites-available/default && 
            sudo service nginx restart',
provider => shell,
}
