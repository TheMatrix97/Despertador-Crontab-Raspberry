<?php
$data = htmlspecialchars($_POST['data']);
$tmp = exec("python python/delete-line-cron.py $data",$salida);
echo '<script language="javascript">alert("Se ha eliminado la fila");</script>'; 
header("Location: http://192.168.1.49/test/testtabla.php");
?>