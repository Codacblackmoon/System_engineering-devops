# Fixes a faulty wordpress site
exes { 'fix-wordpress':
  command => 'bash  -c "sed -1 s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; service apache2 restart"',
  path	=> '/usr/bin:/usr/sbin:/bin'
}
