# Increase the limit of open files
exec { 'fix--for-nginx':
  command => 'sed -i "3 a\worker_rlimit_nofile 30000;" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
