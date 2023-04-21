# execute pkill command to kill bashscript file killmenow
exe { 'pkill':
	command => 'pkill -9 -f killmenow',
	path    => ['/usr/bin', '/usr/sbin', '/bin']
}
