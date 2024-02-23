# Creating a file in /tmp that satisfies the below requirements

$doc_root = '/tmp/school'

file {$doc_root:
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
