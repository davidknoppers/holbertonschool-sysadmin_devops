# executes a basic pkill of process killmenow
exec { 'kill_process':
  command => '/usr/bin/pkill -f killmenow',
}
