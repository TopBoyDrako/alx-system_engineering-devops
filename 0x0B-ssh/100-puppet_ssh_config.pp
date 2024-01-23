# This will set up my client SSH configuration file so I can
# connect to a server without typing a password.

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
