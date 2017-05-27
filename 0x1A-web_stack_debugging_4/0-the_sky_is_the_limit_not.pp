# change the ulimit for our nginx server

  file { '/etc/default/nginx':
    ensure  => file,
    path    => '/etc/default/nginx',
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    content => 'ULIMIT="-n 4096"',
  }
exec { 'nginx':
      command => '/etc/init.d/nginx restart'
