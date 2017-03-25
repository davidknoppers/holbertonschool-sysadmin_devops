# it took me all day and Swati's help to find one extra 'p'
exec { 'remove_typo':
  command => "sed -ie 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin'],
}
