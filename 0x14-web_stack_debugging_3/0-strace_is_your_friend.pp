# partial fix for downed server
exec { 'hacky_html_addition':
  command => 'echo "Holberton School ooh ool" > index.html'
  path    => '/var/www/html',
}
