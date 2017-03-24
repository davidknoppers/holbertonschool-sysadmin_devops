# makes sure puppet-lint is installed on a given server
package { 'puppet-lint':
  ensure   => 'latest',
  provider => 'gem'
}
