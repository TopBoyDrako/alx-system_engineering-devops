# I installed flask from pip3 using Puppet

package { 'python3-pip':
  ensure   => installed,
}

exec { 'install flask':
  command  => '/usr/bin/pip3 install flask==2.1.0',
  provider => 'shell',
  require  => Package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  require  => Package['python3-pip'],
  provider => 'pip'
}
