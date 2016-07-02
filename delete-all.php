<?php 
include 'config_conn.php';
mysql_connect($server,$user,$password);
mysql_select_db($database);
$query = "DELETE FROM horas";	
mysql_query($query);
$tmp = exec("python python/deleteallcron.py",$salida);
?> 