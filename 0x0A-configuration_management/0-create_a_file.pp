# Here I am creating a file in /tmp

file { '/tmp/school':
  content => 'I love Puppet',
  ensure  => 'file',          
  mode    => '0744',
  owner   => 'www.data',
  group   => 'www.data',
}
